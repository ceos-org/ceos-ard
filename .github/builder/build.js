/**
 * Run as follows:
 * node build.js ar
 * or
 * node build.js sar-nrb
 */

const fs = require('fs');
const path = require('path');
const yaml = require('js-yaml');

const type = process.argv[2];

const TBL_NL = '<br />';

function dereference(obj, filePath) {
  if (Array.isArray(obj)) {
    return obj.map(x => dereference(x, filePath));
  }
  else if (obj && typeof obj === 'object') {
    if (obj.$ref) {
      const absPath = path.resolve(path.dirname(filePath), obj.$ref);
      return readYamlFile(absPath);
    }
    else {
      const result = {};
      for (const key of Object.keys(obj)) {
        result[key] = dereference(obj[key], filePath);
      }
      return result;
    }
  }
  return obj;
}

function readYamlFile(filePath) {
  const obj = yaml.load(fs.readFileSync(filePath, 'utf8'));
  return dereference(obj, filePath);
}

function replaceVariables(tpl, variables, filePath) {
  return tpl.replaceAll(/\{\{\s*([^\s}]+)\s*\}\}/g, (_, m1) => {
    if (m1.startsWith('include:')) {
      const absPath = path.resolve(path.dirname(filePath), m1.substr(8));
      return fs.readFileSync(absPath, 'utf8');
    }
    else {
      return variables[m1];
    }
  });
}

function formatAuthors(authors) {
  return authors.map(author => {
    const authorLine = [author.name, author.organization, author.country]
      .filter(x => Boolean(x))
      .join(', ');
    return `- ${authorLine}`;
  }).join("\n");
}

function formatHistory(history) {
  return history.map(entry => {
    return `| ${entry.version} | ${entry.date} | ${entry.changes.join('; ')} | ${entry.authors.join(', ')} |`;
  }).join('\n');
}

function formatTerms(terms) {
  return terms.map(term => {
    return `| ${term.term} | ${term.description} |`;
  }).join('\n');
}

function formatReferences(references) {
  return references.map((reference, i) => {
    // todo: support "supports"
    return `${i+1}. ${reference.citation}`;
  }).join('\n');
}

function noRequirements(reqs) {
  return !reqs || (Array.isArray(reqs) && (reqs.length === 0 || !reqs.some(req => req.type !== 'note')))
}

function formatRequirement(reqs, defaultText) {
  if (noRequirements(reqs)) {
    return defaultText;
  }
  let noteNo = 0;
  return reqs.map(req => {
    const text = (req.description || "").replaceAll(/(\r\n|\r|\n)/g, TBL_NL);
    if (req.type === 'note') {
      return `*Note ${++noteNo}: ${text}*`;
    }
    else {
      return text;
    }
  }).join(TBL_NL + TBL_NL);
}

function formatRequirementSummaries(requirementGroups) {
  // todo: use jinja template instead
  let r = '';
  for(const i in requirementGroups) {
    const group = requirementGroups[i];
    r += `
### ${group.title}

| Requirement | Threshold | Target |
| :---------- | :-------: | :----: |
`;
    for(const j in group.requirements) {
      const req = group.requirements[j];
      const title  = `${parseInt(i)+1}.${parseInt(j)+1} ${req.title}`;
      const minimum = noRequirements(req.requirements.minimum) ? 'Not Required' : '';
      const desired = '';
      r += `| ${title} | ${minimum} | ${desired} |\n`;
    }
  }
  return r;
}

function formatRequirements(requirementGroups) {
  // todo: use jinja template instead
  let r = '';
  for(const i in requirementGroups) {
    const group = requirementGroups[i];
    r += `### ${group.title}\n\n`;
    if (group.description) {
      r += `*${group.description}*\n\n`;
    }

    r += `|  #  | Item | Threshold (Minimum) Requirements | Target (Desired) Requirements |\n`;
    r += `| :-: | :--: | :------------------------------- | :---------------------------- |\n`;
    for(const j in group.requirements) {
      const num  = `${parseInt(i)+1}.${parseInt(j)+1}`;
      const req = group.requirements[j];
      const minimum = formatRequirement(req.requirements.minimum, 'Not required.');
      const desired = formatRequirement(req.requirements.desired, 'As threshold');
      r += `| **${num}** | **${req.title}** | ${minimum} | ${desired} |\n`;
    }
  }
  return r;
}

function main(entryPoint, target) {
  const documentPath = path.resolve(entryPoint, 'document.yaml');
  const templatePath = path.resolve(entryPoint, 'template.md');
  const variables = readYamlFile(documentPath);
  fs.writeFileSync(target + '.yaml', yaml.dump(variables));
  variables.authors = formatAuthors(variables.authors);
  variables.history = formatHistory(variables.history);
  variables.terms = formatTerms(variables.terms);
  variables.requirements_summary = formatRequirementSummaries(variables.requirements);
  variables.requirements = formatRequirements(variables.requirements);
  variables.references = formatReferences(variables.references);
  const tpl = fs.readFileSync(templatePath, 'utf8');
  const result = replaceVariables(tpl, variables, templatePath);
  fs.writeFileSync(target + '.md', result);
  return result;
}

main(path.resolve(__dirname, `../../new/pfs/${type}/`), type);
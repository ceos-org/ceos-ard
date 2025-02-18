# Contributing

Pull Requests are the primary method of contributing to CEOS-ARD, and everyone is welcome to submit 
proposals.

We consider everyone using the Product Family Specifications to enrich their data to be a 'contributor',
as CEOS-ARD is really about the end result of more interoperable data, not just creating a specification for the sake of it.
So if you want to help then the best thing you can do is make new ARD available, build software that uses the specification, or give feedback.

## Submitting Pull Requests

Any proposed changes to the specification should be done as pull requests,
ideally after discussing the changes in an issue before.

All pull requests should submit clean Markdown, which is checked by the continuous integration
system. Please use `npm test` locally, as described in the [next section](#checking-files), 
to ensure that the checks on the pull request succeed.

All pull requests additionally require a review of a CEOS-ARD team members.

## Development / Authoring

1. Install Python + Pandoc + Tex
2. Install CEOS-ARD CLI: `pip install ceos-ard --user`
3. Validate building blocks: `ceos-ard validate`
4. Generate document: `ceos-ard build SR -o SR.md`
5. Generate Word document with Pandoc: `pandoc SR.md -s -f markdown_mmd+definition_lists -o SR.docx -C --bibliography=SR.bib`
6. Generate HTML / PDF: todo

## Release Process

The CI already already creates Editor's Drafts. These can be used to create releases.

Use that file, check whether everything looks good and then create PDF from it.

These two files can then be uploaded to the CEOS-ARD website.

Also make sure to update the tables in the README files and on the CEOS-ARD website.
In the README files make sure to add the now outdated version version to the
"Older Versions" table at the top. Also update the links and version number in
the "Released Version" section.

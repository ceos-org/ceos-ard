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

## Checking files

The same tests that runs as a check on PR's can be run locally.

You'll need npm, which is a standard part of any [node.js installation](https://nodejs.org/en/download/).
Alternatively, you can also use [yarn](https://yarnpkg.com/) instead of npm.
In this case replace all occurrences of `npm` with `yarn` below.

First, we assume you've cloned the repository to your local machine using e.g.

```bash
git clone https://github.com/ceos-org/ceos-ard
```

> \[!NOTE]
> If you don't have write permissions to the <https://github.com/ceos-org/ceos-ard> repository,
> you need to [fork the repository](https://github.com/ceos-org/ceos-ard/fork) first.
> Once you have forked it, use the URL of your newly created repository instead of the repository in
> the ceos-org GitHub organisation.

Afterwards, change into the `ceos-ard` folder and there into the `.github` folder:

```bash
cd ceos-ard/.github
```

You'll need to install everything with npm once:

```bash
npm install
```

To check the Markdown run:

```bash
npm test
```

It will either say for all documents that no issues were found or list specific issues that need to be adressed.
You can run this command as often as you like until you solved all issues.

If you don't know what to do, you can try to let the tool fix the issues for you:

```bash
npm run format
```

Ideally it would fix all issues. You can check it by running the tests again.

## Creating Word Documents

After PR's have been merged, the CI also creates and published the Editor's Draft of the Markdown files as Word Document.
You'll find the links in the README file of each Specification.

If you want to check the Word files yourself locally, you can use the same tools that also run the CI.

You'll need [Pandoc](https://pandoc.org/installing.html).

First, we assume you've cloned the repository to your local machine using e.g.

```bash
git clone https://github.com/ceos-org/ceos-ard
```

Afterwards, change into the `ceos-ard` folder:

```bash
cd ceos-ard
```

You can now run the following commands to create the Word files:

- Aquatic Reflectance:
  ```bash
  pandoc --standalone --shift-heading-level-by=-1 --from=gfm --reference-doc=.github/pandoc-template.docx --lua-filter=.github/pagebreak.lua --output=CEOS-ARD_PFS_Aquatic-Reflectance_latest.docx --resource-path=Specifications/Aquatic-Reflectance Specifications/Aquatic-Reflectance/PFS.md
  ```
  You can open the file `CEOS-ARD_PFS_Aquatic-Reflectance_latest.docx`.

- Nighttime Lights Surface Radiance:
  ```bash
  pandoc --standalone --shift-heading-level-by=-1 --from=gfm --reference-doc=.github/pandoc-template.docx --lua-filter=.github/pagebreak.lua --output=CEOS-ARD_PFS_Nighttime-Lights-Surface-Radiance_latest.docx --resource-path=Specifications/Nighttime-Lights-Surface-Radiance Specifications/Nighttime-Lights-Surface-Radiance/PFS.md
  ```

- Surface Reflectance:
  ```bash
  pandoc --standalone --shift-heading-level-by=-1 --from=gfm --reference-doc=.github/pandoc-template.docx --lua-filter=.github/pagebreak.lua --output=CEOS-ARD_PFS_Surface-Reflectance_latest.docx --resource-path=SpecificationsSurface-Reflectance Specifications/Surface-Reflectance/PFS.md
  ```

- Surface Temperature:
  ```bash
  pandoc --standalone --shift-heading-level-by=-1 --from=gfm --reference-doc=.github/pandoc-template.docx --lua-filter=.github/pagebreak.lua --output=CEOS-ARD_PFS_Surface-Temperature_latest.docx --resource-path=Specifications/Surface-Temperature Specifications/Surface-Temperature/PFS.md Specifications/Surface-Temperature/annex-1-card4l-requirement-examples.md
  ```

- Synthetic Aperture Radar:
  ```bash
  pandoc --standalone --shift-heading-level-by=-1 --from=gfm --reference-doc=.github/pandoc-template.docx --lua-filter=.github/pagebreak.lua --output=docs/CEOS-ARD_PFS_Synthetic-Aperture-Radar_latest.docx --resource-path=Specifications/Synthetic-Aperture-Radar Specifications/Synthetic-Aperture-Radar/PFS.md Specifications/Synthetic-Aperture-Radar/annex-1.1-general-processing-roadmap.md Specifications/Synthetic-Aperture-Radar/annex-1.2-topographic-phase-removal.md Specifications/Synthetic-Aperture-Radar/annex-2-polarimetric-radar.md Specifications/Synthetic-Aperture-Radar/annex-3-ocean-radar-backscatter-example.md Specifications/Synthetic-Aperture-Radar/annex-4-geocoded-single-look-complex-example.md
  ```

For Aquatic Reflectance for example, you could now open the file `CEOS-ARD_PFS_Aquatic-Reflectance_latest.docx`.

## Release Process

The CI already already creates Editor's Drafts. These can be used to create releases.

Use that file, check whether everything looks good and then create PDF from it.

These two files can then be uploaded to the CEOS-ARD website.

Also make sure to update the tables in the README files and on the CEOS-ARD website.
In the README files make sure to add the now outdated version version to the
"Older Versions" table at the top. Also update the links and version number in
the "Released Version" section.

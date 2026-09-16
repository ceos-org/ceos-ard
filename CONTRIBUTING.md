# Contributing

Pull Requests are the primary method of contributing to CEOS-ARD, and everyone is welcome to submit proposals.

We consider everyone using the Product Family Specifications to enrich their data to be a 'contributor',
as CEOS-ARD is really about the end result of more interoperable data, not just creating a specification for the sake of it.
So if you want to help then the best thing you can do is make new ARD available, build software that uses the specification, or give feedback.

## Submitting Pull Requests

Any proposed changes to the specification should be done as pull requests,
ideally after discussing the changes in an issue before.

All pull requests additionally require a review of a CEOS-ARD team members.

## Development / Authoring

1. [Install the CEOS-ARD CLI](https://github.com/ceos-org/ceos-ard-cli?tab=readme-ov-file#installation)
2. Validate building blocks: `ceos-ard validate`
3. Generate the documents for a specific PFS (e.g. `SR`): `ceos-ard generate SR`
4. Generate all documents: `ceos-ard generate-all`

Visit the [CEOS-ARD Editor](https://editor.ceos-ard.moregeo.it/) to draft and propose edits to Product Family Specifications (PFS) and their constituent building blocks in the CEOS-ARD GitHub repository. A short video tutorial is available [here](https://www.youtube.com/watch?v=jKMhHR6M5DU).

## Release Process

To release a specific PFS document, create a GitHub Release with a tag following the pattern `<PFS>-v<major>.<minor>.<patch>`, e.g. `SR-v5.0.1`.
See [VERSIONING.md](VERSIONING.md) for how to determine whether a release is a major, minor, or patch version.

The release workflow will automatically:

1. Generate the release documents (PDF, HTML, DOCX) using the CEOS-ARD CLI.
   This includes the document history, which is compiled from the `changes` of the PFS document and of all building blocks that are used by the PFS.
   The changes are grouped by the previous GitHub releases of the PFS based on their dates, so make sure that all changes have been recorded before creating the release.
2. Attach the generated files to the GitHub Release.

Every pull request is checked automatically for missing changelog entries:
each changed building block (and PFS document) must have a new entry in its `changes` list.
You can run the check locally with `ceos-ard check-changes --base main`.

After the release is published, get the newly generated PFS documents from the
[Releases page on the ceos-ard GitHub repository](https://github.com/ceos-org/ceos-ard/releases).

Upload these documents to the CEOS-ARD website.

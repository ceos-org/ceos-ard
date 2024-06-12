---
name: 'Optical: Surface Temperature [ST]'
about: 'Report an issue or propose a change for the Optical PFSes, which applies for
  Surface Temperature [ST] products. '
labels:
- Optical
- 'Optical: ST'
- needs discussion
body:
  - type: input
    id: version
    attributes:
      label: PFS Version
      description: What version of the PFS are you referring to?
      placeholder: 0.0
  - type: input
    id: req-no
    attributes:
      label: Requirement number(s)
      description: Which requirement number(s) are you referring to?
      placeholder: 0.0
    validations:
      required: false
  - type: textarea
    id: description
    attributes:
      label: Description
      description: Please describe the issue or proposal.
      placeholder: Add your description here...
    validations:
      required: true

---



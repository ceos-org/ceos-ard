---
name: SAR - Polarimetric Radar [POL]
about: 'Report an issue or propose a change for the SAR PFS, which applies for the
  Polarimetric Radar [POL] products. '
labels:
- SAR
- 'SAR: GLSC'
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



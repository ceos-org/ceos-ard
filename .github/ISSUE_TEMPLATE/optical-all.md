---
name: Optical - All Products
about: Report an issue or propose a change for the Optical PFSes, which applies to more
  than one product type.
labels:
- Optical
- needs discussion
body:
  - type: input
    id: version
    attributes:
      label: PFS Version(s)
      description: What version(s) of the PFSes are you referring to?
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



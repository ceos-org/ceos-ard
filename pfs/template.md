---
title: CEOS-ARD - {{ type }} - {{ title }}
---

![](assets/CEOS_logo_colour_black_text_right.png)

# CEOS-ARD - {{ type }} - {{ title }}

&nbsp;

> CEOS Analysis Ready Data (CEOS-ARD) are satellite data that have been processed to a minimum set of requirements and organized into a form that allows immediate analysis with a minimum of additional user effort and interoperability both through time and with other datasets.

&nbsp;

**Product Family Specification:**
{{type}}, {{ title }} ({{ id }})

**Applies to:**
{{ applies_to }}

&#12;

## Document History

{{ history }}

## Contributing Authors

{% for org in authors -%}
- {{ org.name }}{%- if org.country -%}, {{ org.country }}{%- endif -%}
{%-   for member in org.members %}
  - {{ member }}
{%-   endfor %}
{% endfor %}

&#12;

## Glossary

{% for term in glossary %}
{{ term.term }}
:   {{ term.description }}
{% endfor %}

&#12;

## Introduction

### When can a product be called CEOS-ARD?

The CEOS-ARD branding is applied to a particular product once:

- that product has been assessed as meeting CEOS-ARD requirements by the agency responsible for production and distribution of the product, and
- that assessment has been peer reviewed by the CEOS Working Group on Calibration and Validation.

Agencies or other entities considering undertaking an assessment process should contact <ard-contact@lists.ceos.org>.

A product can continue to use CEOS-ARD branding as long as its generation and distribution remain consistent with the peer-reviewed assessment.

### What is the difference between Threshold and Goal?

Products that meet all threshold requirements should be immediately useful for scientific analysis or decision-making.

Products that meet Goal requirements will reduce the overall product uncertainties and enhance broad-scale applications. For example, the products may enhance interoperability or provide increased accuracy through additional corrections that are not reasonable at the _threshold_ level.

Goal requirements anticipate continuous improvement of methods and evolution of community expectations, which are both normal and inevitable in a developing field. Over time, Goal specifications may (and subject to due process) become accepted as _threshold_ requirements.

{% for section in introduction -%}
### {{ section.title }}

{{ section.description }}

{% endfor -%}
&#12;

## Requirements

{% for block in requirements -%}
### {{ block.category.title }}

{{ block.category.description }}

{%   for requirement in block.requirements -%}
#### {{ requirement.title }} (`{{ requirement.id }}`)

{%     for type in ['goal', 'threshold'] -%}
{%       if requirement[type] -%}
##### {{ type|title }} requirements

{{ requirement[type].description }}

{%         if requirement[type].notes -%}
**_Notes:_**
{%           for note in requirement[type].notes -%}
{{ loop.index }}. _{{ note }}_
{%           endfor %}
{%         endif -%}
{%       endif -%}
{%     endfor -%}
{%     if editable -%}
##### Assessment

- Threshold Self-Assessment:
- Target Self-Assessment:
- Self-Assessment Explanation/ Justification:
- Recommended Requirement Modification:

{%     endif -%}
{%   endfor -%}
{% endfor -%}

{%- if references %}
&#12;

## References

{%   for reference in references %}
- {{ reference }}
{%   endfor %}

{% endif %}

{%- if annexes %}
&#12;

## Annexes

{%   for annex in annexes -%}
### {{ annex.title }}

{{ annex.description }}
{%-   endfor %}

{% endif %}

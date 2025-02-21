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

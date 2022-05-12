---
layout: page
title: Style Guide
permalink: /styleguide/
hidden: true
sitemap: false
---

# `h1` Heading

## `h2` Heading

### `h3` Heading

#### `h4` Heading

##### `h5` Heading

###### `h6` Heading

The base type is 15px over 1.6 line height (24px).

**Bolded**

*Italicized*

<a>Colored</a>

_Underlined_

Ordered list

- One
- Two
- Three
  + nested
  + nested
- Four

Unordered list

1. One
1. Two
1. Three
  - one
  - two
  - three
1. Four
    1. Four one
    2. Four two

```python
import python

python.do_great_things()
```

## alerts

{{ site.data.alerts.tip }}
<p>Example Tip</p>
{{ site.data.alerts.end }}


{{ site.data.alerts.note }}
<p>Example Note</p>
{{ site.data.alerts.end }}


{{ site.data.alerts.note }}
<p>Example Important</p>
{{ site.data.alerts.end }}


{{ site.data.alerts.warning }}
<p>Example Warning</p>
{{ site.data.alerts.end }}

## callouts

{{ site.data.alerts.callout_default }}
<p>Callouts Default</p>
{{ site.data.alerts.end }}


{{ site.data.alerts.callout_danger }}
<p>Callouts Danger</p>
{{ site.data.alerts.end }}


{{ site.data.alerts.callout_primary }}
<p>Callouts Primary</p>
{{ site.data.alerts.end }}


{{ site.data.alerts.callout_success }}
<p>Callouts Success</p>
{{ site.data.alerts.end }}


{{ site.data.alerts.callout_info }}
<p>Callouts Info</p>
{{ site.data.alerts.end }}


{{ site.data.alerts.callout_warning }}
<p>Callouts Warning</p>
{{ site.data.alerts.end }}

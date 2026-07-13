---
title     : Measurements format
layout    : default
permalink : /reference/measurements-format/
---

A data format to store definitions of font-level and glyph-level measurements.
{: .lead}

* Table of Contents
{:toc}


Data structure
--------------

A measurement establishes a link between two points and returns the distance between them.

The order of the points matters: a measurement can be positive or negative.

### Font-level measurements

- A font may contain multiple font-level measurements.
- Font measurement names must be unique.
- The order of the font measurements matters.

| attribute   | description                                            |           |
|-------------|--------------------------------------------------------|-----------|
| name        | name of the measurement                                | required  |
| glyph 1     | name of the glyph containing the 1st measurement point | required  |
| point 1     | index or shortcut of 1st measurement point             | required  |
| glyph 2     | name of the glyph containing the 2nd measurement point | required  |
| point 2     | index or shortcut of 2nd measurement point             | required  |
| direction   | direction of measurement                               | required  |
| parent      | parent measurement                                     | optional  |
| description | description of this measurement                        | optional  |
{: .table .table-hover }

<div class="alert alert-warning my-4 rounded-0" role="alert" markdown=1>
The attribute *glyph 2* can be made optional. If it is omitted, we assume *glyph 2* to be the same as *glyph 1*.
{: .card-text }
</div>

### Glyph-level measurements

- A glyph may contain multiple glyph-level measurements.
- Glyph measurement names are related to font-level measurements.
- Glyph measurement names must **not** be unique.
- Glyph measurement identifiers are created from the index or name of its two points.
- The order of glyph measurements follows the order of font measurements.

| attribute | description                             |
|-----------|-----------------------------------------|
| name      | name of the measurement                 |
| point 1   | index or name of 1st measurement point  |
| point 2   | index or name of 2nd measurement point  |
| direction | direction of measurement                |
{: .table .table-hover }

### Direction keys

The direction of measurement must be one of the following characters:

| characters | description            |
|------------|------------------------|
| x          | horizontal measurement |
| y          | vertical measurement   |
| a          | angled measurement     |
{: .table .table-hover }

The order of the points in a measurement matters: the sign of the measured value indicates its direction. Some measurements are by definition negative, for example the descender value or a bottom overshoot.

### Point IDs

Points can be identified by a **number** (point index) or a **letter** (reference point).

#### Point indexes

Contour points are identified by their index (an integer).

#### Reference points

Font-level vertical metrics are also available using the following shortcut characters:

| character | description | y-position            |
|-----------|-------------|-----------------------|
| A         | ascender    | `font.info.ascender`  |
| B         | baseline    | `0`                   |
| C         | cap height  | `font.info.capHeight` |
| D         | descender   | `font.info.descender` |
| X         | x-height    | `font.info.xHeight`   |
{: .table .table-hover }

<div class="alert alert-warning my-4 rounded-0" role="alert" markdown=1>
In addition to the standard (latin) vertical metrics values above, custom reference points can be defined – for example alignment zones for other scripts, or additional alignment points for latin.
{: .card-text }
</div>


Python example
--------------

### Font-level measurements

The key for font-level measurements is the name of the measurement.

```python
fontMeasurements = {
    'XTUC' : {
        'glyph 1'   : 'H',
        'point 1'   : 11,
        'glyph 2'   : 'H',
        'point 2'   : 8,
        'direction' : 'x',
        'parent'    : 'XTRA',
    },
    # more font-level measurements here ...
}
```

### Glyph-level measurements

The key for glyph-level measurements is an identifier created from the two point IDs.

```python
glyphMeasurements = {
    "a" : {
      f'{ptID1} {ptID2}' : {
          'name'      : 'XTRA',
          'direction' : 'x',
      },
      # more glyph-level measurements here ...
    },
    # more glyphs here ...
}
```

<div class="alert alert-warning my-4 rounded-0" role="alert">
The current glyph-level measurement format has one limitation: a pair of points can only have one measurement attached to it. It should be possible to have both x and y measurements for same pair of points though (for example, the width and height of a serif). The format can be updated in the future to address this issue.
</div>

<div class="alert alert-warning  my-4 rounded-0" role="alert" markdown=1> 
### Custom reference points

There is no standard or character limit for custom point names. Short letter codes are preferable for quicker typing and reading.

```python
customPoints = {
    # additional vertical metrics for latin
    'O' : {
        'y' : 640,
        'description' : 'old style figures top',
    },
    # custom vertical metrics for arabic
    'AS' : {
        'y' : 1600,
        'description' : '[arabic] sky',
    },
    'AT' : {
        'y' : 800,
        'description' : '[arabic] tooth',
    },
    'AE' : {
        'y' : -400,
        'description' : '[arabic] earth',
    },
    # more custom points here ...
}
```
</div>


JSON format
-----------

Measurements can be stored in standalone JSON files using the format below.

The same set of measurement definitions can be used to measure all sources in a designspace.

```json
{
  "font": {
    "XTUC": {
      "direction": "x",
      "glyph 1": "H",
      "point 1": "11",
      "glyph 2": "H",
      "point 2": "8",
      "parent": "XTRA"
    },
    /* more font-level measurements here ... */
  },
  "glyphs": {
    "n": {
      "0 20": {
        "direction": "x",
        "name": "XOLC"
      },
      "11 12": {
        "direction": "x",
        "name": "XOLC"
      },
      "13 19": {
        "direction": "x",
        "name": "XTLC"
      },
      /* more glyph-level measurements here ... */
    },
    /* more glyphs here ... */
  },
}
```

---
title     : BlendsInstancer
layout    : default
permalink : /reference/tools/variable/blends-instancer/
---

A tool for previewing and instantiating blended glyphs in reference sources.
{: .lead}


<div class='row'>
<div class='col-4' markdown='1'>
![]({{ site.url }}/images/variable/BlendsInstancer.png){: .img-fluid}
</div>
<div class='col-8' markdown='1'>
designspace…
: Open a dialog to select a designspace file.

reload
: Reload the previously selected designspace file.

show deltas
: Show deltas for each point in relation to the blended glyph.

show distance
: Show x and/or y distance of each delta.

selection only
: Show the distance visualization only for selected points.

instantiate
: Instantiate the blended glyph in the selected layer.

targer layer
: Select layer in which the glyph will be instantiated.

preview
: Turn the visualisation on/off.
</div>
</div>


Display
-------

![]({{ site.url }}/images/variable/BlendsInstancer_preview.png){: .img-fluid}



Color code
----------

| <span class='blue'>blue</span>   | neither x nor y values changing | 
| <span class='red'>red</span>     | only x or y value changing      | 
| <span class='green'>green</span> | both x and y values changing    | 
{: .table .table-hover }


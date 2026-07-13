---
layout: default
title: "Edges"
parent: "Select"
---

# Edges

<img width="200" height="200" alt="Edges component icon" src="../../images/Edges_400.png" />

<div class="component-grid" markdown="1">

<div class="component-box box-desc" markdown="1">
Get specific edges from a Brep geometry. It allows you to filter for:

* Naked edges
* Smooth edges
* Sharp edges

The component can also organize these curves into continuous loops.
</div>

<div class="component-box box-menu" markdown="1">
## Menu Options

**Naked**  
Get the unjoined edges

**Smooth**  
Get the joined edges that are smoothly connected

**Sharp**  
Get the joined edges that are sharply connected

**Loop**  
Organize these curves into continuous loops.

**Highlight Naked Edges**  
Useful for finding gaps between surfaces that are not joined
</div>

<div class="component-box box-in" markdown="1">
## Inputs

**Brep**  
The main brep

**Tolerance**  
Tolerance
</div>

<div class="component-box box-out" markdown="1">
## Outputs

**Edge Curves**  
Edge curves of the Brep

**Edge Numbers**  
The number id of each edge
</div>

</div>

---
layout: default
title: "Optimize"
parent: "3D Tools"
---

# Optimize

<img width="200" height="200" alt="Optimize component icon" src="../../images/Optimize_400.png" />

<div class="component-grid" markdown="1">

<div class="component-box box-desc" markdown="1">
Cleans and simplifies Brep geometry.  The specific methods of optimisation are in the menu, so that you only apply those that are necessary.
</div>

<div class="component-box box-menu" markdown="1">
## Menu Options

**Shrink Face**  
Any face that extends beyond edges is reduced to match the size of it's trims
(It's a little technical, but helps prevent unintended results when working with faces)

**Merge Edges**  
Merges fragmented edges

**Merge Faces**  
Any co-planar faces will be merged into a single flat surface"

**Solid Orient**  
Makes sure the surfaces are pointing outward

**Compact**  
Compact the Brep
</div>

<div class="component-box box-in" markdown="1">
## Inputs

**Brep**  
The main brep
</div>

<div class="component-box box-out" markdown="1">
## Outputs

**Brep**  
The optimized brep
</div>

</div>

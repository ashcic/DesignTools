---
layout: default
title: "Resize"
parent: "Transform"
---

# Resize

<img width="200" height="200" alt="Resize component icon" src="../../images/Resize_400.png" />

<div class="component-grid" markdown="1">

<div class="component-box box-desc" markdown="1">
Resizes geometry based on target dimensions, reference objects, or both.
</div>

<div class="component-box box-menu" markdown="1">
## Menu Options

**Align**  
Align to the reference geometry

**Union**  
Treat the geometry as a single group of objects

**Match**  
Scale all dimensions proportionally to the scaling to the input dimensions
(Only works if only one dimension has an input)
</div>

<div class="component-box box-in" markdown="1">
## Inputs

**Geometry**  
Geometry to resize

**refs**  
The geometry to use as a reference

**X**  
X target sizing

**Y**  
Y target sizing

**Z**  
Z target sizing
</div>

<div class="component-box box-out" markdown="1">
## Outputs

**Geometry**  
Resized geometry

**Planes**  
Transformation base planes

**Scales**  
Applied scale factors

**Moves**  
The translation vectors used to move the geometry

**Notes**  
A description of how to use this tool
</div>

</div>

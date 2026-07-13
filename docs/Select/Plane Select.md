---
layout: default
title: "Plane Select"
parent: "Select"
---

# Plane Select

<img width="200" height="200" alt="Plane Select component icon" src="../../images/Plane_Select_400.png" />

<div class="component-grid" markdown="1">

<div class="component-box box-desc" markdown="1">
Use a Plane to select geometry.  Divide the geometry into two groups — those situated above/on a reference plane and those below it.

**Selection Levels:**

* Geometry
* Faces
* Edges
</div>

<div class="component-box box-menu" markdown="1">
## Menu Options

**Overlapping**  
Includes any part of the object that is above or on the plane.

**Strictly Inside**  
Only includes objects entirely above the plane.

**Geometry**  
Selects full geometry objects

**Faces**  
For Breps, selects certain faces

**Edges**  
For Breps, selects certain edges
</div>

<div class="component-box box-in" markdown="1">
## Inputs

**Geometry**  
The main geometry

**Plane**  
The selection plane
</div>

<div class="component-box box-out" markdown="1">
## Outputs

**Geometry Inside**  
The geometry inside the boxes

**Geometry Outside**  
The geometry outside the boxes

**Pattern**  
The index values for all the included geometry
</div>

</div>

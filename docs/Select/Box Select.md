---
layout: default
title: "Box Select"
parent: "Select"
---

# Box Select

<img width="200" height="200" alt="Box Select component icon" src="../../images/Box_Select_400.png" />

<div class="component-grid" markdown="1">

<div class="component-box box-desc" markdown="1">
Use Bounding Boxes to select geometry
</div>

<div class="component-box box-menu" markdown="1">
## Menu Options

**Overlapping**  
Includes any part of the object that is on or inside the box

**Strictly Inside**  
Only includes objects entirely inside the box

**Union**  
Treat the geometry as a single group of objects

**2D Only Checks X and Y**  
Only checks whether the box overlaps from the top view, ignoring Z

**Geometry**  
Select geometry objects

**Faces**  
Select Faces on a Brep

**Edges**  
Select Edges on a Brep
</div>

<div class="component-box box-in" markdown="1">
## Inputs

**Geometry**  
Main Geometry

**Boxes**  
The boxes or geometry used to seledt from the main geometry

**Inflate**  
Increase the size of the selection box in all dimensions
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

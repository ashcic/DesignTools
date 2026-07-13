---
layout: default
title: "Box Select"
parent: "Select"
---

# Box Select

<img width="200" height="200" alt="Box Select component icon" src="../../images/Box_Select_400.png" />


Use Bounding Boxes to select geometry

## Key Features:

**Selection Types:** Filter results by whole geometry, faces, or edges.
**Containment Modes:** Choose between 'Overlapping' and 'Strictly Inside'.
**Box Behavior:** Treat all input boxes as a single Union area or as individual selection zones.
**Advanced Options:** Use Inflate to expand the selection box size and a toggle for 2D-only checks in the X and Y dimensions.

___

## Inputs

**Geometry**
Main Geometry

**Boxes**
The boxes or geometry used to seledt from the main geometry

**Inflate**
Increase the size of the selection box in all dimensions

___

## Outputs

**Geometry Inside**
The geometry inside the boxes

**Geometry Outside**
The geometry outside the boxes

**Pattern**
The index values for all the included geometry

___

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
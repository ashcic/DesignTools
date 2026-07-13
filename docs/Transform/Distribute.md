---
layout: default
title: "Distribute"
parent: "Transform"
---

# Distribute

<img width="200" height="200" alt="Distribute component icon" src="../../images/Distribute_400.png" />


Distributes geometry across a bounding box with uniform gaps or specific alignment points.

**Distribution Modes:**

* 0 - Even Gaps
* 1 - From Left (Min)
* 2 - From Centres
* 3 - From Right (Max)

The **Order** toggle sorts items by position, and the **Align** toggle snaps the final group to the reference geometry.

___

## Inputs

**Geometry**
The objects to be distributed.

**Reference Geo (Optional)**
The geometry to use as a reference

**X**
0, 1 or 2 sets the position to left, centre or right, can also be true/false

**Y**
0, 1 or 2 sets the position to front, centre or back, can also be true/false

**Z**
0, 1 or 2 sets the position to bottom, centre or top, can also be true/false

**Insets**
The ammount to inset from the edge

___

## Outputs

**Geometry**
The updated geometry

**Moves**
The translation vectors used to move the geometry

**Notes**
A description of how to use this tool

___

## Menu Options

**Even Gaps**
Set even gaps between objects

**From Left (Min)**
Spacing is measured from the left or minimum sides

**From Centres**
Spacing is measured from the centres

**From Right (Max)**
Spacing is measured from the left or maximum sides

**Order**
Use the input order to order the geometry, rather than it's original position

**Align**
Align to the reference geometry
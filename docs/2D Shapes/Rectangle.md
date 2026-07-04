---
layout: default
title: "Rectangle"
parent: "2D Shapes"
---

# Rectangle

Creates a rectangle with customizable dimensions and corner styles. You can choose between sharp corners, chamfered edges, or various types of rounded (Arc) and blended corners.

## Key features:

**Individual Corner Control:** Set unique radii or blend values for each of the four corners.
**Corner Types:** Switch between C2 Corners, Arc Corners, Chamfered Corners, and C2 Arc Corners via the component menu.
**Geometry Outputs:** Provides the joined curve, individual segments, and corner points for further analysis.

___

## Inputs

**X**
The X Dimension

**Y**
The Y Dimension

**Radii**
You can add multiple dimensions for multiple radii

**Blends**
Control how much the corners blend into the sides

___

## Outputs

**Curves**
The rectangle as separate curves

**Joined**
The rectangle as joined curves

**Points**
The corner points

**Notes**
A description of how to use this tool

___

## Menu Options

**C2 Corners**
Smooth blend radius on each corner

**Arc Corners**
Simple arc radius on each corner

**Chamfered Corners**
Flat edge instead of an arc

**C2 Arc Corners**
Produces a C2 smooth radius in each corner that imitates an arc

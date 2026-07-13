---
layout: default
title: "Resize"
parent: "Transform"
---

# Resize

<img width="200" height="200" alt="Resize component icon" src="../../images/Resize_400.png" />


Resizes geometry based on target dimensions, reference objects, or both.

## Key Features:

**Manual Sizing:** Input numbers into X, Y, or Z to set exact target sizes.
**Reference Matching:** Input a boolean *true* to match the size of a reference object for that specific axis.
**Alignment:** Automatically aligns and centers geometry relative to a reference object's bounding box.
**Group Control:** Choose whether to resize all objects as a single unit (Union) or scale each item individually based on its own center.

___

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

___

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

___

## Menu Options

**Align**
Align to the reference geometry

**Union**
Treat the geometry as a single group of objects

**Match**
Scale all dimensions proportionally to the scaling to the input dimensions
(Only works if only one dimension has an input)

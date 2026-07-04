---
layout: default
title: "Resize"
parent: "Transform"
---

# Resize

#### Change the size of the geometry

Resizes geometry based on target dimensions, reference objects, or both.

Key features include:

* **Manual Sizing:** Input numbers into X, Y, or Z to set exact target sizes.
* **Reference Matching:** Input a boolean *true* to match the size of a reference object for that specific axis.
* **Alignment:** Automatically aligns and centers geometry relative to a reference object's bounding box.
* **Group Control:** Choose whether to resize all objects as a single unit (Union) or scale each item individually based on its own center.

___

### Inputs
**Geometry**
Geometry to resize

**refs**
The geometry to use as a reference

**x**
X target sizing

**y**
Y target sizing

**z**
Z target sizing

___

### Outputs
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

### Menu Options
**align**
"Explanation..."

**union**
"Explanation..."

**match**
"Explanation..."

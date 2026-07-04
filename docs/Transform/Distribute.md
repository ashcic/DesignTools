---
layout: default
title: "Distribute"
parent: "Transform"
---

# Distribute

#### Distribute the geometry with even gaps

Distributes geometry across a bounding box with uniform gaps or specific alignment points.

* **Geometry:** The objects to be distributed.
* **Reference Geo:** The boundary for distribution (optional). If empty, the bounding box of the input geometry is used.
* **X, Y, Z:** Use *True/False* to force the geometry to match the reference size in that dimension, or a *Number* to set a specific gap distance between objects.
* **Insets:** The amount to offset the distribution from the edges of the bounding box.

**Distribution Modes (Centre):**

* 0 - Even Gaps
* 1 - From Left (Min)
* 2 - From Centres
* 3 - From Right (Max)

The **Order** toggle sorts items by position, and the **Align** toggle snaps the final group to the reference boundary.

___

### Inputs
**Geometry**
The main geometry

**Reference Geo**
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

### Outputs
**Geometry**
The updated geometry

**Moves**
The translation vectors used to move the geometry

**Notes**
A description of how to use this tool

___

### Menu Options
**Even Gaps**
"Explanation..."

**From Left (Min)**
"Explanation..."

**From Centres**
"Explanation..."

**From Right (Max)**
"Explanation..."

**Even Gaps**
"Explanation..."

**From Left (Min)**
"Explanation..."

**From Centres**
"Explanation..."

**From Right (Max)**
"Explanation..."

**order**
"Explanation..."

**align**
"Explanation..."

**match_x**
"Explanation..."

**match_y**
"Explanation..."

**match_z**
"Explanation..."

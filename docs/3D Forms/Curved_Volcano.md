---
layout: default
title: "Curved Volcano"
parent: "3D Forms"
---

# Curved Volcano

#### Create a protursion with a curve ramped blended surface

Creates a curved, ramped protrusion from a base geometry using profile curves. This component blends a surface into a volcano-like shape with customizable transitions.

Key features: 
     * **Blending:** Uses weighted profiles to smoothly transition between the base geometry and the protrusion.
     * **Edge Control:** Adjust the angle, fillet radius, and blend weights of the top edge for specific curvature requirements.
     * **Geometry:** Supports optional external boundaries and offsets to define the shape's limits.
     * **Capping:** Includes a toggle to close (cap) the top face of the generated geometry.

___

### Inputs
**Brep**
The main geometry

**Curves**
Main profile of the volcano

**Outer**
Optional external boundary profile

**Offset**
Distance offset

**Angle**
Angle of the blend at the top edge

**Blend A**
Weight of the blend at the top

**Blend B**
Weight of the blend at the bottom

**Fillet**
Top edge fillet radius

**Blend**
Blend on the edge fillet

___

### Outputs
**Brep**
Final geometry

**Planes**
Planes for orientation

**Top Curves**
Top profiles

**Mid Curves**
Middle profiles

**Bottom Curves**
Bottom profiles

**Fillet Curves**
Fillet curves (for checking curvature)

**Side Curves**
Side curves (for checking curvature)

___

### Menu Options
**Max 32**
"Explanation..."

**High 21**
"Explanation..."

**Medium 16**
"Explanation..."

**Low 12**
"Explanation..."

**Min 7**
"Explanation..."

**cap**
"Explanation..."

**from_edge**
"Explanation..."

**start**
"Explanation..."

**loop**
"Explanation..."

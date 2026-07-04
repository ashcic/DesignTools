---
layout: default
title: "Locate"
parent: "Transform"
---

# Locate

#### Locate a plane on geometry in order to place things on it

This component helps you identify a specific face on geometry and create a local coordinate plane at a precise location on that surface. It is ideal for positioning objects accurately onto complex shapes.

**Key Features:**

 * *Face Selection:* Choose a specific face using the index input (visualized with numbered arrows).
 * *Positioning:* Place the plane using a 0-10 grid system or manually via U and V insets.
 * *Offsetting:* Move the resulting plane away from the surface along its normal direction.
 * *Multi-Object Support:* Automatically creates a bounding box to calculate positions for groups of objects.

___

### Inputs
**Geometry**
The main geometry

**face**
select a face

**Position**
0-10 chooses a position on the selected face

**Inset U**
Moves the plane in U

**Inset V**
Moves the plane in V

**Offset W**
Offsets the plane from the surface

___

### Outputs
**plane**
The final plane

**surface**
Extracted surface

**edges**
The edges of the extracted surface

**body**
The remaining, non-extracted, part of the geometry

**Notes**
A description of how to use this tool

___

### Menu Options
**simple**
"Explanation..."

**box**
"Explanation..."

**simple_centre**
"Explanation..."

---
layout: default
title: "Locate"
parent: "Transform"
---

# Locate

Locate a plane on geometry in order to place things on it

## Key Features:

 **Face Selection:** Choose a specific face using the index input (visualized with numbered arrows).
 **Positioning:** Place the plane using a 0-10 grid system and adjust manually via U and V insets.
 **Offsetting:** Move the resulting plane away from the surface along its normal direction.
 **Multi-Object Support:** Automatically creates a bounding box to calculate positions for groups of objects.

___

## Inputs

**Geometry**
The main geometry

**Face**
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

## Outputs

**Plane**
The final plane

**Surface**
Extracted surface

**Edges**
The edges of the extracted surface

**Body**
The remaining, non-extracted, part of the geometry

**Notes**
A description of how to use this tool

___

## Menu Options

**Simple**
Finds the centre using bounding box rather than UVs

**Box**
Treat the objects as a bounding box and align to one of the 6 sides

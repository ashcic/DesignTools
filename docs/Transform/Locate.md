---
layout: default
title: "Locate"
parent: "Transform"
---

# Locate

<img width="200" height="200" alt="Locate component icon" src="../../images/Locate_400.png" />

<div class="component-grid" markdown="1">

<div class="component-box box-desc" markdown="1">
Locate a plane on geometry in order to place things on it
</div>

<div class="component-box box-menu" markdown="1">
## Menu Options

**Simple**  
Finds the centre using bounding box rather than UVs

**Box**  
Treat the objects as a bounding box and align to one of the 6 sides
</div>

<div class="component-box box-in" markdown="1">
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
</div>

<div class="component-box box-out" markdown="1">
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
</div>

</div>

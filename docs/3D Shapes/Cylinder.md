---
layout: default
title: "Cylinder"
parent: "3D Shapes"
---

# Cylinder

<img width="200" height="200" alt="Cylinder component icon" src="../../images/Cylinder_400.png" />

<div class="component-grid" markdown="1">

<div class="component-box box-desc" markdown="1">
Creates an advanced cylinder or cone with customizable fillets.  I
</div>

<div class="component-box box-menu" markdown="1">
## Menu Options

**C2 Corners**  
Smooth blend fillet on each edge

**Arc Corners**  
Simple arc fillet on each edge

**Chamfered Corners**  
Flat edge instead of an arc

**C2 Arc Corners**  
Produces a C2 smooth fillet in each edge that imitates an arc

**Cap**  
Add caps to opens ends of the geometry, creating a closed brep

**Centre**  
If true, the centre of the cylinder will be at the origin
If false, the base of the cylinder will be at the origin
</div>

<div class="component-box box-in" markdown="1">
## Inputs

**Top and Bottom Radius**  
Top and Bottom Radius (add 2 values to make a cone)

**Height**  
Height of the cylinder

**Sections**  
Number of sections

**Fillets**  
Fillets at the bottom and top

**Blends**  
Blends at the bottom and top
</div>

<div class="component-box box-out" markdown="1">
## Outputs

**Brep**  
Resulting joined cylinder parts

**Profile**  
Side Profile

**Circles**  
Top and Bottom Circles

**Arcs**  
Base arcs for each section
</div>

</div>

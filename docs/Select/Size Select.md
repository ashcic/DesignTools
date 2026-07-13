---
layout: default
title: "Size Select"
parent: "Select"
---

# Size Select

<img width="200" height="200" alt="Size Select component icon" src="../../images/Size_Select_400.png" />

<div class="component-grid" markdown="1">

<div class="component-box box-desc" markdown="1">
Select geometry based on it's size.  Identifies and extracts either the **Biggest** or **Smallest** geometry from a list based on chosen measurement criteria (such as Volume, Area, or Bounding Box size).

The selected item is sent to the 'Piece' output, while all remaining objects are grouped in the 'Others' output.
</div>

<div class="component-box box-menu" markdown="1">
## Menu Options

**Box Volume (Fast)**  
Compare the bounding box volumes of each geometry

**Actual Volume**  
Compare the actual Volume of Breps

**XY Area (Fast)**  
For flat surfaces compare the sizes of the bounding rectangles

**Actual Area**  
For flat surfaces compare the actual surface area

**Biggest**  
Select the biggest

**Smallest**  
Select the biggest
</div>

<div class="component-box box-in" markdown="1">
## Inputs

**Geometry**  
The main geometry
</div>

<div class="component-box box-out" markdown="1">
## Outputs

**Piece**  
Selected geometry

**Others**  
Non-selcted geometry
</div>

</div>

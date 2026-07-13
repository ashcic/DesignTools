---
layout: default
title: "Blend_Curve"
parent: "Curve Tools"
---

# Blend_Curve

<img width="200" height="200" alt="Blend Curve component icon" src="../../images/Blend_Curve_400.png" />

<div class="component-grid" markdown="1">

<div class="component-box box-desc" markdown="1">
Creates a smooth curve between two points with precise control over the orientation at each endpoint.

**Orientation:** Define the specific direction (Vector) and rotation (Angle) for both the start and end of the curve.
**Optional Curves:** Blend into or out of existing curves to match specific radii or shapes.
**Blend Influence:** Control how much the start and end settings influence the overall curvature of the result.
</div>
<div class="component-box box-desc" markdown="1">
</div>
<div class="component-box box-in" markdown="1">
## Inputs

**Start Point**  
Point at the start

**End Point**  
Point at the end

**Start Vector**  
Vector at the start

**End Vector**  
Vector at the end

**Angle at Start**  
Angle at the start

**Angle at End**  
Angle at the end

**Start Curve**  
Optional Curve to blend with

**End Curve**  
Optional Curve to blend with

**Start Blend**  
Influence of the start vector

**End Blend**  
Influence of the end vector
</div>

<div class="component-box box-out" markdown="1">
## Outputs

**Curve**  
Blend Curve
</div>

</div>

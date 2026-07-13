---
layout: default
title: "Split Brep"
parent: "3D Tools"
---

# Split Brep

<img width="200" height="200" alt="Split Brep component icon" src="../../images/Split_Brep_400.png" />


Splits a Brep with a plane and optionally applies a filleted transition between the resulting geometry.

**Fillet:** Sets the radius of the rounded edge. Set to 0 for a sharp, clean cut.
**Blend:** Adjusts the curvature/smoothness of the fillet.
**Flip:** Reverses the final orientation of the output geometry.

___

## Inputs

**Brep**
Geometry to be split

**Plane**
Orientation of the split

**Fillet**
Radius of transition fillet

**Blend**
Blend factor (0-1)

**Flip**
Flip final geometry orientation

___

## Outputs

**Breps**
Resulting joined Breps

**Curves**
Intersection/split curves

___

## Menu Options

**Cap**
Add caps to opens ends of the geometry, creating a closed brep

**Match**
Makes the fillets of the split match each other

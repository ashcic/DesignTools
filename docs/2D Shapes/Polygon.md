---
layout: default
title: "Polygon"
parent: "2D Shapes"
---

# Polygon

<img width="200" height="200" alt="Polygon component icon" src="../../images/Polygon_400.png" />


Creates a regular polygon based on a radius and number of sides, with customizable corner treatments.

**Fillets & Blends:** Create smooth, rounded corners with adjustable size and curvature.
**Arcs:** Create perfectly circular corner joints.
**Chamfers:** Create flat, angled corners.
**C2 Corners:** Provide smooth, high-continuity transitions for organic shapes.

Outputs include the construction circle, joined curves, individual segments, fillet centers, and vertex points.

___

## Inputs

**Radius**
Radius of the construction circle

**Sides**
Number of sides

**Fillet**
Corner fillets

**Blend**
Corner fillet blends

**Match**
Match the dimensions of the construction circle

___

## Outputs

**Curves**
Individual curves

**Joined**
Joined curves

**Circle**
The construction circle

**Centres**
The centres of the fillets

**Points**
Description

___

## Menu Options

**C2 Corners**
Smooth blend radius on each corner

**Arc Corners**
Simple arc radius on each corner

**Chamfered Corners**
Flat edge instead of an arc

**C2 Arc Corners**
Produces a C2 smooth radius in each corner that imitates an arc

**Match**
Scale the polygon so that the corner radius touch the construction circle

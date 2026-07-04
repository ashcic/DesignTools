---
layout: default
title: "Optimize"
parent: "3D Tools"
---

# Optimize

Cleans and simplifies Brep geometry.  The specific methods of optimisation are in the menu, so that you only apply those that are necessary.

___

## Inputs

**Brep**
The main brep

___

## Outputs

**Brep**
The optimized brep

___

## Menu Options

**Shrink Face**
Any face that extends beyond edges is reduced to match the size of it's trims
(It's a little technical, but helps prevent unintended results when working with faces)

**Merge Edges**
Merges fragmented edges

**Merge Faces**
Any co-planar faces will be merged into a single flat surface"

**Solid Orient**
Makes sure the surfaces are pointing outward

**Compact**
Compact the Brep

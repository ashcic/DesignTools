---
layout: default
title: "Plane Select"
parent: "Select"
---

# Plane Select

<img width="200" height="200" alt="Plane Select component icon" src="../../images/Plane_Select_400.png" />

<div class="component-grid" markdown="1">

<div class="component-box box-desc" markdown="1">
使用平面选择几何体。将几何体分为两组——位于参考平面上方/上的和位于下方的。

**选择级别：**

* 几何体
* 面
* 边
</div>

<div class="component-box box-menu" markdown="1">
## 菜单选项

**Overlapping**  
包含位于平面上方或上的任何部分对象

**Strictly Inside**  
仅包含完全在平面上方的对象

**Geometry**  
选择完整几何对象

**Faces**  
对于 Brep，选择特定面

**Edges**  
对于 Brep，选择特定边
</div>

<div class="component-box box-in" markdown="1">
## 输入

**Geometry**  
主要几何体

**Plane**  
选择平面
</div>

<div class="component-box box-out" markdown="1">
## 输出

**Geometry Inside**  
盒子内的几何体

**Geometry Outside**  
盒子外的几何体

**Pattern**  
所有包含几何体的索引值
</div>

</div>

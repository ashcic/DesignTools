---
layout: default
title: "Box Select"
parent: "Select"
---

# Box Select

<img width="200" height="200" alt="Box Select component icon" src="/DesignTools/images/Box_Select_400.png" />

<div class="component-grid" markdown="1">

<div class="component-box box-desc" markdown="1">
使用包围盒选择几何体
</div>

<div class="component-box box-menu" markdown="1">
## 菜单选项

**Overlapping**  
包含盒子上或内部的任何部分对象

**Strictly Inside**  
仅包含完全在盒子内部的对象

**Union**  
将几何体视为单个对象组

**2D Only Checks X and Y**  
仅从俯视图检查盒子是否重叠，忽略 Z

**Geometry**  
选择几何对象

**Faces**  
选择 Brep 上的面

**Edges**  
选择 Brep 上的边
</div>

<div class="component-box box-in" markdown="1">
## 输入

**Geometry**  
主要几何体

**Boxes**  
用于从主要几何体选择的盒子或几何体

**Inflate**  
在所有维度上增加选择盒大小
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

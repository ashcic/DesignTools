---
layout: default
title: "Size Select"
parent: "Select"
---

# Size Select

<img width="200" height="200" alt="Size Select component icon" src="/DesignTools/images/Size_Select_400.png" />

<div class="component-grid" markdown="1">

<div class="component-box box-desc" markdown="1">
根据大小选择几何体。根据所选测量标准（如体积、面积或包围盒大小），从列表中识别并提取**最大**或**最小**几何体。

所选项目发送到“Piece”输出，而所有其余对象分组在“Others”输出中。
</div>

<div class="component-box box-menu" markdown="1">
## 菜单选项

**Box Volume (Fast)**  
比较每个几何体的包围盒体积

**Actual Volume**  
比较 Brep 的实际体积

**XY Area (Fast)**  
对于平面，比较包围矩形的大小

**Actual Area**  
对于平面，比较实际表面积

**Biggest**  
选择最大的

**Smallest**  
选择最小的
</div>

<div class="component-box box-in" markdown="1">
## 输入

**Geometry**  
主要几何体
</div>

<div class="component-box box-out" markdown="1">
## 输出

**Piece**  
选中的几何体

**Others**  
未选中的几何体
</div>

</div>

---
layout: default
title: "Optimize"
parent: "3D Tools"
---

# Optimize

<img width="200" height="200" alt="Optimize component icon" src="../../../images/Optimize_400.png" />

<div class="component-grid" markdown="1">

<div class="component-box box-desc" markdown="1">
清理并简化 Brep 几何体。具体的优化方法在菜单中，以便您仅应用必要的优化。
</div>

<div class="component-box box-menu" markdown="1">
## 菜单选项

**Shrink Face**  
任何超出边的面将缩减以匹配其修剪边的大小
(有点技术性，但有助于处理面时防止意外结果)

**Merge Edges**  
合并碎片化的边

**Merge Faces**  
任何共面的面将合并为单个平面

**Solid Orient**  
确保曲面朝外

**Compact**  
压缩 Brep
</div>

<div class="component-box box-in" markdown="1">
## 输入

**Brep**  
主要 Brep
</div>

<div class="component-box box-out" markdown="1">
## 输出

**Brep**  
优化后的 Brep
</div>

</div>

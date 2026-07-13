---
layout: default
title: "Split Brep"
parent: "3D Tools"
---

# Split Brep

<img width="200" height="200" alt="Split Brep component icon" src="/DesignTools/images/Split_Brep_400.png" />

<div class="component-grid" markdown="1">

<div class="component-box box-desc" markdown="1">
使用平面分割 Brep，并可选择在生成的几何体之间应用圆角过渡。

**Fillet：** 设置圆角边的半径。设为 0 可获得锐利、干净的切割。
**Blend：** 调整圆角的曲率/平滑度。
**Flip：** 反转输出几何体的最终朝向。
</div>

<div class="component-box box-menu" markdown="1">
## 菜单选项

**Cap**  
为几何体开口端添加封盖，创建闭合 Brep

**Match**  
使分割的圆角相互匹配
</div>

<div class="component-box box-in" markdown="1">
## 输入

**Brep**  
要分割的几何体

**Plane**  
分割方向

**Fillet**  
过渡圆角半径

**Blend**  
混合因子 (0-1)

**Flip**  
翻转最终几何体朝向
</div>

<div class="component-box box-out" markdown="1">
## 输出

**Breps**  
生成的连接 Brep

**Curves**  
相交/分割曲线
</div>

</div>

---
layout: default
title: "Sausage"
parent: "2D Shapes (ZH)"
---

# Sausage

<img width="200" height="200" alt="Sausage component icon" src="../../images/Sausage_400.png" />

<div class="component-grid" markdown="1">

<div class="component-box box-desc" markdown="1">
在输入曲线周围创建加厚、封盖的几何形状，具有可自定义的端部样式。

**主要功能：**

* 调整主体**厚度**。
* 从各种**端盖类型**中选择（圆形、平头、箭头、圆、方形或条形）。
* 控制**头部延伸**和**倒刺**的长度和缩放。

组件输出连接几何体、单独曲线和适合导出到 Adobe Illustrator 的填充。

*注意：输入曲线必须平放在 XY 平面上。*
</div>
<div class="component-box box-desc" markdown="1">
</div>
<div class="component-box box-in" markdown="1">
## 输入

**Curves**  
输入曲线（必须平放在 XY 平面上）

**Width**  
线条粗细

**Head**  
头部长度

**Barb**  
延伸大小

**Start**  
起始头部类型 ID (0=圆形, 1=平头, 2=箭头, 3=圆, 4=方形, 5=条形)

**End**  
结束头部类型 ID (0=圆形, 1=平头, 2=箭头, 3=圆, 4=方形, 5=条形)
</div>

<div class="component-box box-out" markdown="1">
## 输出

**Curves**  
单独的曲线

**Joined**  
连接的曲线

**Hatch**  
填充可作为实体对象导出到 Adobe Illustrator

**Notes**  
如何使用此工具的说明
</div>

</div>
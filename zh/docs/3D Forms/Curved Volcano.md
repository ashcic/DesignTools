---
layout: default
title: "Curved Volcano"
parent: "3D Forms (ZH)"
---

# Curved Volcano

<img width="200" height="200" alt="Curved Volcano component icon" src="../../images/Volcano_Curved_400.png" />

<div class="component-grid" markdown="1">

<div class="component-box box-desc" markdown="1">
使用轮廓曲线从基础几何体创建弯曲的斜坡状凸起。此组件将曲面混合成火山状形状，具有可自定义的过渡。
</div>

<div class="component-box box-menu" markdown="1">
## 菜单选项

**Max 32**  
32 个扇区或控制曲线平滑曲面
较慢，最适合复杂曲线

**High 21**  
21 个扇区或控制曲线平滑曲面
最适合复杂曲线

**Medium 16**  
16 个扇区或控制曲线平滑曲面
标准数量

**Low 12**  
12 个扇区或控制曲线平滑曲面
最适合简单曲线

**Min 7**  
7 个扇区或控制曲线平滑曲面
快速，最适合简单曲线

**Cap**  
为几何体开口端添加封盖，创建封闭 Brep

**From Edge**  
从几何体边缘测量偏移，使其响应几何体尺寸
</div>

<div class="component-box box-in" markdown="1">
## 输入

**Brep**  
主要几何体

**Curves**  
火山的主要轮廓

**Outer**  
可选的外部边界轮廓

**Offset**  
距离偏移

**Angle**  
顶部边缘混合角度

**Blend A**  
顶部混合权重

**Blend B**  
底部混合权重

**Fillet**  
顶部边缘圆角半径

**Blend**  
边缘圆角上的混合
</div>

<div class="component-box box-out" markdown="1">
## 输出

**Brep**  
最终几何体

**Planes**  
用于定向的平面

**Top Curves**  
顶部轮廓

**Mid Curves**  
中部轮廓

**Bottom Curves**  
底部轮廓

**Fillet Curves**  
圆角曲线（用于检查曲率）

**Side Curves**  
侧面曲线（用于检查曲率）
</div>

</div>
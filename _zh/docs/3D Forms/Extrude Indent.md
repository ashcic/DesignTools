---
layout: default
title: "Extrude Indent"
parent: "3D Forms"
---

# Extrude Indent

<img width="200" height="200" alt="Extrude Indent component icon" src="../../../images/Extrude_Indent_400.png" />

<div class="component-grid" markdown="1">

<div class="component-box box-desc" markdown="1">
这是您工作流的主力工具。它从曲线创建挤出形状、压痕或通孔。允许生成带圆角和混合的 3D 形状，以及在现有实体或空心几何体中雕刻简单的压痕。
</div>

<div class="component-box box-menu" markdown="1">
## 菜单选项

**Max 27**  
27 个扇区或控制曲线平滑曲面
较慢，最适合复杂曲线

**High 21**  
21 个扇区或控制曲线平滑曲面
最适合复杂曲线

**Medium 17**  
17 个扇区或控制曲线平滑曲面
标准数量

**Low 13**  
13 个扇区或控制曲线平滑曲面
最适合简单曲线

**Min 9**  
9 个扇区或控制曲线平滑曲面
快速，最适合简单曲线
</div>

<div class="component-box box-in" markdown="1">
## 输入

**Curves**  
主要曲线

**Brep**  
要修改的 Brep

**Fillets**  
修改边的圆角

**Blends**  
圆角的混合

**Extrude**  
挤出距离

**Inset**  
主要曲线的内缩

**Flip**  
改变方向：
- 如果挤出，flip 从中心向两侧等量挤出
- 如果压痕，flip 给出压痕的负空间
</div>

<div class="component-box box-out" markdown="1">
## 输出

**Breps**  
修改后的 Brep

**Planes**  
用于在修改后的 Brep 上放置对象的平面

**Edges A**  
顶部边缘

**Edges B**  
底部边缘

**Notes**  
如何使用此工具的说明
</div>

</div>

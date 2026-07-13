---
layout: default
title: "Distribute"
parent: "Transform (ZH)"
---

# Distribute

<img width="200" height="200" alt="Distribute component icon" src="../../images/Distribute_400.png" />

<div class="component-grid" markdown="1">

<div class="component-box box-desc" markdown="1">
将几何体沿包围盒均匀分布，或按特定对齐点分布。

**分布模式：**

* 0 - 均匀间距
* 1 - 从左侧 (最小值)
* 2 - 从中心
* 3 - 从右侧 (最大值)

**Order** 开关按位置对项目排序，**Align** 开关将最终组对齐到参考几何体。
</div>

<div class="component-box box-menu" markdown="1">
## 菜单选项

**Even Gaps**  
设置对象间的均匀间距

**From Left (Min)**  
从左侧或最小侧测量间距

**From Centres**  
从中心测量间距

**From Right (Max)**  
从右侧或最大侧测量间距

**Order**  
使用输入顺序排序几何体，而非其原始位置

**Align**  
对齐到参考几何体
</div>

<div class="component-box box-in" markdown="1">
## 输入

**Geometry**  
要分布的对象

**Reference Geo (Optional)**  
用作参考的几何体

**X**  
0、1 或 2 将位置设置为左、中或右，也可以是 true/false

**Y**  
0、1 或 2 将位置设置为前、中或后，也可以是 true/false

**Z**  
0、1 或 2 将位置设置为底、中或顶，也可以是 true/false

**Insets**  
从边缘向内缩进的量
</div>

<div class="component-box box-out" markdown="1">
## 输出

**Geometry**  
更新后的几何体

**Moves**  
用于移动几何体的平移向量

**Notes**  
如何使用此工具的说明
</div>

</div>
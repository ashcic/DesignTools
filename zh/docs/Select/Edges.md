---
layout: default
title: "Edges"
parent: "Select (ZH)"
---

# Edges

<img width="200" height="200" alt="Edges component icon" src="../../images/Edges_400.png" />

<div class="component-grid" markdown="1">

<div class="component-box box-desc" markdown="1">
从 Brep 几何体获取特定边。允许筛选：

* 裸边
* 平滑边
* 锐边

该组件还可以将这些曲线组织成连续环。
</div>

<div class="component-box box-menu" markdown="1">
## 菜单选项

**Naked**  
获取未连接的边

**Smooth**  
获取平滑连接的边

**Sharp**  
获取锐利连接的边

**Loop**  
将这些曲线组织成连续环

**Highlight Naked Edges**  
用于查找未连接的表面间隙
</div>

<div class="component-box box-in" markdown="1">
## 输入

**Brep**  
主要 Brep

**Tolerance**  
公差
</div>

<div class="component-box box-out" markdown="1">
## 输出

**Edge Curves**  
Brep 的边曲线

**Edge Numbers**  
每条边的编号 ID
</div>

</div>
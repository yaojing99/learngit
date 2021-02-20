**标题写法一，总共六级**
# 一级标题
## 二级标题
### 三级标题
#### 四级
##### 五级
###### 六级
***
**标题写法二，总共六级**
# 一级 #
## 二级 ##
### 三级 ##
#### 四级 ####
##### 五级 #####
###### 六级 ######
***
###### **标题写法三，总共两级**
一级标题
=
二级标题
-
***
**正文写法**

直接输入就可以
换行注意，要在代码中实际空一行
直接换行的话，渲染输出其实是没有换行的
***
**分割线的三种写法**

星号***
减号---
下划线___

**总结：**

对于标题，建议使用 # 号，几级标题就是几个 #；
对于段落，要按2次Enter区分，缩进用&emsp;代表一个空格；
对于分割线，建议使用三个或以上的 * 号，以免与标题混淆。
***
---
___
**代码块**

如果你写的代码是某种语言，那么可以在第一行末尾加上这个语言的名字，代码块内的代码就会执行对应的高亮语法，例如python
```
show version
show module
show inventory
show environment
show ip interface brief
show ip route
show logging
router ospf
```
```python
print('hello, world')
```
行内的代码 `show ip interface brief`
***
**有序列表**

输入数字，加一个句点，然后空格即可；可以缩进空置多级列表
1. 哈哈哈
2. 哈哈哈哈
3. 哈哈哈
   1. 哈哈哈
   2. hahaha
   3. fdafdasfda
4. fdafdasfdas
   1. fdasfdas
      1. fdakslfdasjk
      2. fdafda
         1. fdksaljk
         2. fdafdsa
      3. fdasfdas
   2. fdasfdas

**无序列表，输入 - 然后空格**
- 放大放大
- fdafda
  - 放大放大
  - 放大放大放大
    - 放大放大
    - 放大
      - 放大法师
      - fdaklfjda 
        - fdasfdas 
        - fda
          - fdafdas
***
*斜体*
**加粗**
***粗斜体***

*show version*
*show ip interface*
**router ospf**
**router bgp**
***show running-config***
***show startup-config***

大段代码块内粗斜体无效
```
**show ip interface**
**show ip route**
show running-config
show startup-config
```

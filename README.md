# CSFaceClient
`以下为辅助提示信息`
### 提示信息
1. 全部使用帕斯卡命名方式（即所有单词首字母大写）
2. 去掉window文件，一切窗口直接继承于QWidget
3. 使用settings文件，保存常量
4. 全部控件大小改用相对比例，而不是最初的绝对尺寸
5. 显示与逻辑分离
6. 静态文件放在static文件夹，临时文件放在temp文件夹
7. 压缩包存放背景图片
8. .db文件为sqlite文件 ，.vsdx文件为流程图使用visio打开，.md文件为思维导图使用xmind打开
#### 函数文档
##### database.py
NewestVisitor：  
ouput：获取到的访客列表(list)  
被线程循环调用，用于查询mysql数据库record表中是否有新数据插入，通过global 变量  currentid 记录上一次的最大rowid
，使用本此查询到的currnetid与上一次进行比较,二者差值为查询数据数量。  
  
UpdateLocalRecord：  
input：最新的访客列表(list)  
将主数据库中record表中最新加入的数据同步到sqlite数据库record表  
  
 ChangePage  
 input：页码index(int)   
 output：访客列表list(list)  
 传入当前页码，从sqlite数据库record表中查询rowid在一定范围的数据，返回数据列表  
   
 DataCount  
 查询sqlite数据库record表中全部数据总数，用于计算页码数量  
   
 input：
 
## teacherClient
1. grade.txt 用来临时保存年级信息
2. photo.png 用于缓存临时照片
## doorClient

## studentClient


##待解决问题
1. 原来的定时执行框架，在我们问题的处理中是个垃圾，弃用
3. qt与opencv的并存问题

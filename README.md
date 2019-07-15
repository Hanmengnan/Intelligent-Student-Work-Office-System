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
8. .db文件为sqlite文件 ，.vsdx文件为流程图使用visio打开，.xmind文件为思维导图使用xmind打开
9. 原来的定时执行框架，在我们问题的处理中是个垃圾，弃用
## 通用
##### database.py
NewestVisitor：  
ouput：获取到的访客列表(list)  
被线程循环调用，用于查询mysql数据库record表中是否有新数据插入，通过global 变量  currentid 记录上一次的最大rowid
，使用本此查询到的currnetid与上一次进行比较,二者差值为查询数据数量。  
  
UpdateLocalRecord：  
input：最新的访客列表(list)  
将主数据库中record表中最新加入的数据同步到sqlite数据库record表  
  
 ChangePage：  
 input：页码index(int)   
 output：访客列表list(list)  
 传入当前页码，从sqlite数据库record表中查询rowid在一定范围的数据，返回数据列表  
   
 DataCount：    
 查询sqlite数据库record表中全部数据总数，用于计算页码数量  
   
 Detail：  
 input：id  
 output：学生详细信息data(dict)  
 根据学生学号查询数据库中该学生详细信息  
   
 Getphoto：  
 input：id  
 output：True/False  
 根据学生学号获取照片的16进制字串，写到本地（对图片以16进制字串格式读写没有搞定，故采用此方式）
   
 
 #### newthread.py  
 1. usualThread为通用线程用于查询主数据库中是否有新数据插入，用以判断是否有新访客
 2. deleteThread为doorClient使用的线程，在没有访客前来时，倒数时间，清空屏幕  
   
 ### client.py  
    
    
 
## teacherClient
1. grade.txt 用来临时保存年级信息
2. photo.png 用于缓存临时照片
3. teacherWindow 界面函数
4. teacherControl 逻辑函数  
  
    UpdateGrade：  
    从grade.txt文件中读取需要显示的年级，并更新显示，更新年级之后会跳回主页  
        
    PrePage：    
    上一页，发出信号，控制翻页   
       
    BackPage：    
    同上  
        
    page_controller：  
    响应信号，改变表格内容 
         
    GetPageCount：  
    获取数据总数，计算总页数   
         
    MainPageShow：  
    显示首页
           
    ChangePage：   
    根据页码改变表格内容
        
    makeFunc：  
    闭/包处理，为了解决每个button 关联不同行的数据的问题，若简单使用循环来写，则会出现无论点击那个button都只显示最后一行数据对应信息的问题
        
    DetailSetEmpty：  
    查询不到信息的情况下，详细信息置空  
        
    PhotoSetEmpty：  
    同上，照片置空
        
    ShowFirstVisitor：  
    显示每页的首个学生的详细信息
      
    
    
    
     
      
## doorClient

## studentClient


## 待解决问题
1.  qt与opencv的并存问题

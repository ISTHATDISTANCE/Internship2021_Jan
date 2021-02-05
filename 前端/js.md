## 基本用法

分为行内，内部和外部

**和css一样**

js 代码推荐放在body标签后。最好等html元素执行完后再执行。

![](js.assets/image-20201231101832056.png)

上图为三种使用方式。

## 基础语法

### 变量

声明变量时不需要指定数据类型

![image-20201231104509391](js.assets/image-20201231104509391.png)

只有用var声明的变量才会提升

### 数据类型

![image-20201231105336087](js.assets/image-20201231105336087.png)

#### undefined

表示值不存在

1. 定义了未赋值便使用；
2. 调用函数时未传递实参；
3. 函数没有返回值，默认返回undefined；

![image-20201231105928102](js.assets/image-20201231105928102.png)

#### null

![image-20201231110028076](js.assets/image-20201231110028076.png)

#### 数值型

整形和浮点型都以64位浮点类型存储

浮点类型最高精度时17位，有误差不建议用作判断

存储时自动将1.0转换成1

#### 字符串

#### 对象

### 类型转换

#### 自动类型转换

![image-20201231111246802](js.assets/image-20201231111246802.png)

#### 函数转换

![image-20201231111453860](js.assets/image-20201231111453860.png)

#### 显示转换

![image-20201231112026737](js.assets/image-20201231112026737.png)

![image-20201231113157999](js.assets/image-20201231113157999.png)

### 运算符

![image-20201231114131410](js.assets/image-20201231114131410.png)

![image-20201231114233347](js.assets/image-20201231114233347.png)

![image-20201231114208810](js.assets/image-20201231114208810.png)

![image-20201231114522350](js.assets/image-20201231114522350.png)

#### 逻辑语句

![image-20201231114704036](js.assets/image-20201231114704036.png)

### 数组

#### 定义

![image-20201231114938158](js.assets/image-20201231114938158.png)

数组中数据类型任意

#### 基本操作

数组长度可以通过length属性得到，并可任意修改。

索引可以越界。

可以使用非正整数作为索引：称之为数组属性，不影响长度

#### 数组遍历

![image-20201231120229236](js.assets/image-20201231120229236.png)

不遍历属性

![image-20201231120242338](js.assets/image-20201231120242338.png)

不遍历undefined

![image-20201231134641647](js.assets/image-20201231134641647.png)

不遍历属性和undefined

### 数组方法

![image-20201231135633517](js.assets/image-20201231135633517.png)

### 函数

#### 定义

![image-20201231140523508](js.assets/image-20201231140523508.png)

如果使用函数声明语句具有函数名提升效果。

js没有方法重载，如果同名则覆盖。

![image-20201231141458685](js.assets/image-20201231141458685.png)

![image-20201231141527441](js.assets/image-20201231141527441.png)

![image-20201231141735510](js.assets/image-20201231141735510.png)

#### 函数的调用

1. 直接调用：函数名([参数列表])；
2. 函数调用（有返回值时用）；
3. 对象调用（函数是对象中的属性时）：对象.函数名([参数列表])；

#### 函数的返回

有返回值用return，没有则无返回值或返回undefined；

没有返回值时return则结束方法。

#### 函数的作用域

![image-20201231142612402](js.assets/image-20201231142612402.png)

JS中只有函数有作用域

### 内置对象

Array 数组对象；

Date 日期对象，用来创建和获取日期；

Math 数学对象；

String 字符串对象；

![image-20201231143348561](js.assets/image-20201231143348561.png)

![image-20201231144345521](js.assets/image-20201231144345521.png)

![image-20201231144604314](js.assets/image-20201231144604314.png)

### 对象

![image-20201231145010540](js.assets/image-20201231145010540.png)

#### 对象的创建

##### 字面量形式创建

![image-20201231145104803](js.assets/image-20201231145104803.png)

格式：键: 值

obj.key = value

##### new Object创建

![image-20201231150118768](js.assets/image-20201231150118768.png)

##### var 对象名 = Object.create(参考对象)

以参考对象为模板

#### 对象的序列化和反序列化

![image-20201231150701944](js.assets/image-20201231150701944.png)

#### this

![image-20201231151111516](js.assets/image-20201231151111516.png)

##### 在函数中使用

this可指window对象

##### 在对象中使用

![image-20201231151844643](js.assets/image-20201231151844643.png)

总结：this指调用函数的对象（全局为window）

## JS事件

### 主要内容

![image-20201231153002174](js.assets/image-20201231153002174.png)

### 事件

![image-20201231153059487](js.assets/image-20201231153059487.png)

作用：

![image-20201231153141163](js.assets/image-20201231153141163.png)

几个名词：

![image-20201231153205535](js.assets/image-20201231153205535.png)

### 事件流和事件捕获

事件流顺序：事件冒泡到事件捕获

#### 事件冒泡

![image-20201231154023516](js.assets/image-20201231154023516.png)

#### 事件捕获

![image-20201231154232950](js.assets/image-20201231154232950.png)

#### DOM事件流

![image-20201231154552212](js.assets/image-20201231154552212.png)

### 事件处理程序

以on开头

#### html事件处理程序

对html标签添加

#### DOM 0级事件处理程序

![image-20201231155148079](js.assets/image-20201231155148079.png)

![image-20201231155525387](js.assets/image-20201231155525387.png)

只能为同一个元素的同一个事件设置一个事件程序（会覆盖）

script不能写到前面

特殊情况

![image-20201231160125177](js.assets/image-20201231160125177.png)

#### DOM 2级事件处理程序

![image-20201231160424004](js.assets/image-20201231160424004.png)

addEventListener(), removeEventListener()

三个参数：事件名、事件处理程序，事件冒泡或事件捕获

example：

![image-20201231160944655](js.assets/image-20201231160944655.png)

可以为同一个元素同一个事件设置多个事件。

[常用事件网站](https://www.w3school.com.cn/jsref/jsref_events.asp)

### BOM 对象

![image-20201231163245094](js.assets/image-20201231163245094.png)

#### 系统对话框

![image-20201231163557132](js.assets/image-20201231163557132.png)

alert() 会阻止后续代码的执行

#### 打开窗口

![image-20201231164719913](js.assets/image-20201231164719913.png)

#### 关闭窗口

![image-20201231170241152](js.assets/image-20201231170241152.png)

#### 时间函数

![image-20201231174148444](js.assets/image-20201231174148444.png)

![image-20201231180719288](js.assets/image-20201231180719288.png)

### History对象

![image-20201231181057626](js.assets/image-20201231181057626.png)

### Location对象

![image-20201231181727083](js.assets/image-20201231181727083.png)

## DOM对象

![image-20201231182652363](js.assets/image-20201231182652363.png)

### 节点

![image-20201231183319581](js.assets/image-20201231183319581.png)

```html
<html>
    <head>
        <title>树！</title>
    </head>
    <body>
        <div title="属性节点">
            测试 div
        </div>
    </body>
</html>
```

![image-20201231183723449](js.assets/image-20201231183723449.png)

#### 获取节点

![image-20201231184123155](js.assets/image-20201231184123155.png)

<font color=red> 操作必须等节点初始化完毕 </font>

#### 创建和插入节点

![image-20210101154818784](js.assets/image-20210101154818784.png)

![image-20210101154917985](js.assets/image-20210101154917985.png)

newItem: 要插入的节点；existingItem: 参考节点（需要参考父节点）

parentElement.insertBefore(newChild, refChild)

![image-20210101164337628](js.assets/image-20210101164337628.png)

#### 间接查找节点

![image-20210101164525205](js.assets/image-20210101164525205.png)

children：返回元素的所有子元素

**注意：这里的文本节点包含换行符**

firstElementChild,  lastElementChild

所有以上方法包含元素节点对象

#### 删除节点

![image-20210101165610331](js.assets/image-20210101165610331.png)

## 表单

![image-20210101184637030](js.assets/image-20210101184637030.png)

### 获取表单

![image-20210101184756707](js.assets/image-20210101184756707.png)

通过name属性获得

**注意：3中的索引为表单名称**

### 获取表单元素

#### input

![image-20210101190940622](js.assets/image-20210101190940622.png)

#### 单选

![image-20210101191733827](js.assets/image-20210101191733827.png)

![image-20210101191805847](js.assets/image-20210101191805847.png)

#### 多选

![image-20210101192236773](js.assets/image-20210101192236773.png)

#### 下拉框

![image-20210101192542801](js.assets/image-20210101192542801.png)

.options：获取所有下拉选项

### 提交表单

![image-20210101193318924](js.assets/image-20210101193318924.png)

.trim(): 去除前后空格（不去除中间空格）

### 表单校验

## JQuery

![image-20210102184007445](js.assets/image-20210102184007445.png)

![image-20210102184222960](js.assets/image-20210102184222960.png)

### JQuery核心

![image-20210102185042084](js.assets/image-20210102185042084.png)


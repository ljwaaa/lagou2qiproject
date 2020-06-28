##  简介
拉钩二期项目实战演练

##  参考链接
https://github.com/ljwaaa/lagou2qiproject.git
##  python实战（一）作业
1、搭建好python,pycharm, git 环境，在本地创建一个pythoncode，和README.MD, 上传到github上，将代码github链接地址贴到作业贴下即可。
2、创建模块，模块里面创建方法，定义有参数，和无数，有返回值和无返回值的情况，并说明 无返回值的默认返回值。
##  python实战（二）作业
描述：
创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）

创建子类【猫】，继承【动物类】，

- 复写父类的__init__方法，继承父类的属性，

- 添加一个新的属性，毛发=短毛，

- 添加一个新的方法， 会捉老鼠，

- 复写父类的‘【会叫】的方法，改成【喵喵叫】
创建子类【狗】，继承【动物类】，

- 复写父类的__init__方法，继承父类的属性，

- 添加一个新的属性，毛发=长毛，

- 添加一个新的方法， 会看家，

- 复写父类的【会叫】的方法，改成【汪汪叫】
创建一个猫猫实例

- 调用捉老鼠的方法

- 打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】。
创建一个狗狗实例

- 调用【会看家】的方法

- 打印【狗狗的姓名，颜色，年龄，性别，毛发】。

使用 yaml 来管理实例的属性
##  pytest实战（一）作业
1、补全计算器（加减乘除）的测试用例
2、使用数据驱动完成测试用例的自动生成
3、conftest.py中创建fixture 完成setup和teardown
4、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】

##  pytest实战（一）作业
 ### 课后作业1
1、使用参数化数据驱动，完成加减乘除测试用例的自动生成
2、修改测试用例为check_开头，修改测试用例的执行规则，执行所有check_开头和test_开头的测试用例

### 课后作业2
控制测试用例顺序按照【加-减-乘-除】这个顺序执行,
减法依赖加法， 除法依赖乘法

### 课后作业3
注册一个命令行参数env,env默认值是test,表示测试环境，另外还有两个值 （dev,st）不同的环境读取不同的数据。

### 企业微信实战一
1.分别使用浏览器复用和cookie登录企业微信。
2.将所有的死等都封装成显式等待

### 企业微信实战二

* 完善你的PO，把显示等待等涉及到webdriver的方法封装到basepage中
* 使用PO设计模式写如下的testcase：
* 删除成员
* 导入通讯录



## Funny JSON Explorer

使用抽象工厂设计模式，能够创建相关或依赖对象的家族，不需要指定具体的类，可派生多个具体工厂类和产品类，一个工厂实例能够创建多个该工厂对应的产品实例，这里对应了领域模型中Container和Leaf的关系。将Container根据不同的style抽象成不同的具体类，再定义另一种IconFactory工厂类，抽象不同icon family类型。





![image-20240531203911405](https://gitee.com/e-year/images/raw/master/img/202406011042628.png)



添加新的风格：添加style，仅需继承Container类到一个具体类，为其编写draw函数；添加icon_family仅需继承IconFactory类和IconProduct类成一个新的icon_family类。在FunnyJsonExplorer中加入条件判断调用新的类即可

![image-20240531205533102](https://gitee.com/e-year/images/raw/master/img/202406011042524.png)

![image-20240531205554702](https://gitee.com/e-year/images/raw/master/img/202406011042213.png)

![image-20240531205620441](https://gitee.com/e-year/images/raw/master/img/202406011043074.png)

![image-20240531205654980](https://gitee.com/e-year/images/raw/master/img/202406011043592.png)

还差：

1. 说明设计模式
2. github推送
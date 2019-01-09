## 在看项目代码过程中遇到的零散问题

__all__是一个字符串list,用来定义模块中对于from XXX import * 时要对外导出的符号，即要暴露的接口，但它只对import * 起作用，对from XXX import XXX不起作用。

函数  <function XX at 0x000000>

类方法 <unbound method X.x>

实例方法  <bound method X.x of <__main__.X object at 0x.....>

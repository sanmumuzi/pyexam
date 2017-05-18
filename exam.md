# python组考核

## 1.介绍一下你觉得你写的最有趣的python程序

* 一个最最最基本的满是坑的匿名聊天室。。。

<>

## 2.解释一下@classmethod, @staticmethod, @property

### @property

* 将方法转换为属性调用。
* @property本身又可以创建@xxx.setter和@xxx.deleter
* 使用@property时，为可读属性
* 使用@xxx.setter,可以设置属性
* 使用@xxx.deleter,可以删除属性
* 使用该装饰器将可以不必再为类内不对外暴露的变量建立各种调用、赋值、删除等函数。
* property()为一个内置函数，返回一个property对象。
	
	property(fget=None, fset=None, fdel=None, doc=None) -> property attribute
* fget是一个获取属性值的函数，fset是一个设置属性值的函数，fdel是一个删除属性的函数。Property对象有三个方法，getter(), setter()和delete()，用来在对象创建后设置fget，fset和fdel。

### @classmethod
* 使用@classmethod装饰，隐藏的传递给第一个参数的是自身类，不是self，既可以从实例调用，也可以从类调用。

### @staticmethod
* 使用@staticmethod装饰，不需要参与类和实例，不带参数绑定，与普通函数相同，该装饰器使用主要是有利于组织代码，利于维护。

## 3.如何拷贝一个对象？如果有多种方法，他们的区别是什么？

* python中的copy模块拥有两个拷贝方法，一个为浅拷贝，copy.copy,另一个为深拷贝，浅拷贝相当于将原容器中的地址复制一遍，（指针指向原数据），所以改变子对象之后，浅拷贝的数据也会改变，深拷贝相当于将所有元素全部复制一遍，（全为新地址），修改原数据，不会对深拷贝的对象造成影响。

## 4.实现一个终端版本的本地音乐播放器，能够播放本地指定路径的mp3文件并联网自动匹配歌词，且能够在终端中按照对应的时间线刷新歌词。
* 并未实现联网自动匹配歌词的功能

<>

## 5.请用python3实现一个类似linux平台下的tail命令的程序，暂命名为ptail，要求至少支持 -f，-n参数并尽可能的降低读取大文件时的资源消耗。

<https://github.com/sanmumuzi/pyexam>
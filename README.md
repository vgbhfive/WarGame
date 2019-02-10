# WarGame

A war game written in python, it uses a lot of python tools, through the actual code version changes, you will learn how to use them and their advanced usage, and you will be more proficient in using Python to complete your ideas. Finally, it helps you to better control Python and use it.

### 1、 Part One
这一部分的主要目的是开发简单应用。

 1. 在这一部分我们会学习搭建Python的开发环境。
	 1. 通过官方网站下载Install Python来安装Python3.5。
	 2. 验证Python安装。
	 终端窗口运行命令： ```python -V``` 
 2. 构建我们的第一个程序。
 3. 为游戏添加一些复杂度，然后使用简单的函数改善游戏版本。
 4. 逐渐增加游戏的特性，并使用面向对象的概念重新设计代码。
 5. 简要提及Python的抽象基类。

### 2、 Part Two
第二部分的主要目的在于使用异常处理让程序更加的健壮。

 1. 学习使用Python中的异常，
 2. 使用try...except语句控制程序流。
 3. 通过异常处理来应付普通问题。
 4. 创建并使用定制的异常类。

### 3、Part Three
第三部分的主要目的是使程序模块化、打包和部署。

 1. 对前面章节中的代码进行模块化和打包。
 2. 准备并部署一个代码的发行版版本。
	 1. 在PyPI上发布包
		 Python包索引（PyPI）(https://pypi.python.org/pypi) 是一个Python社区的包发布机制。默认情况下，Python软件管理器和pip都搜索这个库进行包的安装。
	 2.  发行版本准备
		 1. 设置包路径。
			1. 在目录下创建README、LICENSE.txt、MANIFEST.in和setup.py文件。
		 2. 编写setup.py文件。
			 ``` ``` 
			  1. 通过传递不同的参数来调用setup函数。
			  2. 只有名字、版本和包是必须的字段。最后我们可以向setup函数中添加其他的一些可选元数据参数。
		 3. 更新README和LICENSE.txt文件。
			 1. LICENSE.txt中，主要保存许可证描述。
			 2. README中，用于增加关于项目的详细描述。 
		 4. 更新MANIFEST.in文件。
			 默认情况下，distutils包含一下用于创建发行版本的文件：
			 1.  顶层发布目录包含README、README.txt、setup.py和setup.cfg文件。
			 2. 软件包中所有的*.py文件都会在setup.py文件中列出。
			 3. 全部的test或test*.py文件。
			 4. libraries和ext_modles in setup.py文件中标明的C源文件。
			 5. 注：若是想添加许可证描述，在MANIFEST.in中添加以下内容：
			 ```include *.txt```
		 5. 构建一个部署就绪版本。
			 1. 切换到命令窗口界面，运行以下命令：
			 ``` cd wargame ``` 
			 ``` python setup.py sdist```
			  2. 下面是最终的输出。
			```
			F:\PycharmWorkspace\WarGameV2.0.0>python setup.py sdist
			running sdist
			running check
			reading manifest template 'MANIFEST.in'
			writing manifest file 'MANIFEST'
			creating vgbhfive_wargame-2.0.0
			creating vgbhfive_wargame-2.0.0\wargame
			making hard links in vgbhfive_wargame-2.0.0...
			hard linking LCENSE.txt -> vgbhfive_wargame-2.0.0
			hard linking README -> vgbhfive_wargame-2.0.0
			hard linking setup.py -> vgbhfive_wargame-2.0.0
			hard linking wargame\__init__.py -> vgbhfive_wargame-2.0.0\wargame
			hard linking wargame\abstractgameunit.py -> vgbhfive_wargame-2.0.0\wargame
			hard linking wargame\attackoftheorcs.py -> vgbhfive_wargame-2.0.0\wargame
			hard linking wargame\gameutils.py -> vgbhfive_wargame-2.0.0\wargame
			hard linking wargame\hut.py -> vgbhfive_wargame-2.0.0\wargame
			hard linking wargame\knight.py -> vgbhfive_wargame-2.0.0\wargame
			hard linking wargame\orcrider.py -> vgbhfive_wargame-2.0.0\wargame
			hard linking wargame\rungame.py -> vgbhfive_wargame-2.0.0\wargame
			Creating tar archive
			removing 'vgbhfive_wargame-2.0.0' (and everything under it)
			```

	 3. 上传发行版本
		 1. 在PyPI上测试网站上注册账号。
		 2. 创建一个.pypirc文件。
			 .pypric（以点开头的）文件居右特定的格式：
			 ```
			 [distutils]
			 index-servers=
			 pypitest
			 [pypitest]
			 repository = https://testpypi.python.org/pypi
			 username=<add username>
			 password=<add password>
			 ```
		 3. 注册你的项目。
		 ``` python setup.py register -r https://testpypi.python.org/pypi```
		 4. 上传包。
		 ``` python setup.py sdist upload -r pypitest```
	4. 一键更新
	    ``` python setup.py register -r pypitest sdist upload -r pypitest```
	6. 安装自己的发行版本代码
		``` pip install -i https://testpypi.python.org/pypi yourpackagename```
 3. 建议一个私有的Python仓库。
	 1. 安装pypiserver
		  ```pip install pypiserver```
	 2. 创建一个新的源代码发行版本
		   1. 需要修改name、url和description字段信息。
		   2. ``` python steup.py sdist```
	 3. 启动本地服务
		```pypi-server -p 8081 ./dist```
	 4. 安装私有发行版。
	    ```pip install -i http://localhost:8081 yourpackagename```
 4. 制作增量发布。
	 1. 打包上传新的版本。
		  1. 将setup.py文件中的版本号进行更新。
		  2.  ``` python setup.py sdist upload -r pypitest```
	 2. 升级已经安装的版本。
		``` pip install -i https://testpypi.python.org/pypi wargame --upgrade```
 5. 将你的代码接入版本控制工具。
	 1. 安装并使用Git。 

### 4、 Part Four
第四部分的主要目的是将代码文档化并且进行代码分析。

 1. 理解reStructuredText格式，书写文档字符串。
	 1. 大体上，总有三个层次的文档。最外层，可能是项目级别或者发行版本级别的文档。第二层则是API级别的文档。第三层是以代码注释的形式出现的。
	 Sphinx是一个Python用来创建项目和API级别文件文档的生成工具。
	 文档字符串的目的就是简要地堆代码进行描述。
	  2. reStructuredText简介及使用
	 reStructuredText定义了一组简单的标记语法，主要用于Python文档，他是Python的文档处理系统docutils的一部分。
	 RST常用的特性，官网（http://docutils.sourceforge.net/rst.html ）。
	 常见的文档字符串风格主要有RST、谷歌文档字符串以及numpydoc，使用stubs可以将他们之间轻松的转换。
	 stubs不能使用pip进行安装，但是可以通过Github获取源码，通过Github上的主页的安装说明进行安装。
	  3. 使用Sphinx生成文档
	  
 2. 学习使用Sphinx文档生成器创建HTML文档。
	 1. 使用pip安装Sphinx
			 ``` pip install Sphinx```
			 这个命令一共可以创建4个脚本：sphinx-autogen、sphinx-apidoc、sphinx-build和sphinx-quickstart。
			 对于实现代码的高亮显示，可以通过pip安装Pygments的工具来实现。
	2. 运行sphinx-quickstart
			 这个脚本可以快速的使用Sphinx，并且他会建立一个用于存放文档文件的目录和配置文件conf. py。
			 这个脚本运行后，会提出几个问题，根据自己的选择回答即可。
	 3. 更新conf. py
		     
	4. 运行sphinx-apidoc
		     语法如下：
		     ``` sphinx-apidoc [options] -o <outputdir> <rsourcedir> []pathname ...]```
		     在终端窗口运行以下命令：
		     ``` sphinx-apidoc -o source/ ../```
	5. 建立文档
			 在终端界面中输入以下命令：
		     ``` sphinx-build source build```
 3. 学习Python编码标准。
	 1. PEP8
		 编码标准是编写优质代码的指南。
		 详细信息可以查看官方文档（https://www.python.org/dev/peps/pep-0008/ ）。
 4. 使用Pylint评估代码的规范程度。
	 1. 使用IDE进行代码分析
		 Pycharm社区版就提供了很好的代码检测工具。
	 2. Pylint
		 1. 通过pip安装Pylint 
				``` pip install pylint```
		 2. Pylint实践
			``` pylint module_name.py```
			运行代码之后就会出现一份完整的报告，通过报告就可以知道具有哪些错误信息。

### 5、 Part Five
 1. 



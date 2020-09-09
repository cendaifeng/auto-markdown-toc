<a href='https://www.python.org'><img src='https://img.shields.io/badge/python-3.8-yellow.svg?style=flat-square'></a> [![HitCount](http://hits.dwyl.com/cendaifeng/auto-markdown-toc.svg)](http://hits.dwyl.com/cendaifeng/auto-markdown-toc)

# auto-markdown-toc

自动扫描 markdown 文件中的标题，并为它生成目录，以适配 GitHub 页面



## 使用

- 将代码克隆后，将 `md_toc.py` 置入 markdown 文件所在文件夹

- 打开命令行 `cd` 到该目录

- 输入运行命令

  ```powershell
  > python md_toc.py your_markdown.md
  ```

- 运行完毕后，在当前文件夹会新生成一个带有目录的 markdown 文件

## 测试和效果

![image-20200909122517997](C:\Users\Administrator\git_dir\auto-markdown-toc\README.assets\image-20200909122517997.png)

![image-20200909130234909](C:\Users\Administrator\git_dir\auto-markdown-toc\README.assets\image-20200909130234909.png)

## 特性

- 在**标题索引**上的处理：

  被替换为空串的字符有 **`` .*(（[【)）]】#?@$& ``**

  根据 GFM 编写，已在 Windows 平台上通过大部分字符串测试。如有疏漏或是在其他平台上有相关测试结果欢迎在 issue 上指出或者直接 ``pull request`` 
  
- 能够正确识别出标题级数并输出相对应的缩进

## 常见错误

- 未输入参数

  > ```
  > ==== haven`t input a filename after .py ====
  > e.g. "python md_toc.py MyMD.md
  > ```

- 在其他目录通过绝对或相对路径访问（不建议），易造成生成文件位置或文件名有误等

  > ```
  > ==== ' md_name ' is not found in current path ====
  > in this path ONLY: ...
  > ```
	
	请直接 `cd` 



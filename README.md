# axutongxue-bookmarks
转换阿虚同学的储物间为可以直接导入为浏览器书签的HTML文件
源文件来源：https://github.com/axutongxue/axutongxue.github.io/blob/main/index.html

初期思路（已经过时）：
请用Python处理original.html
替换前八行为以下内容：
<!DOCTYPE NETSCAPE-Bookmark-file-1>
<!-- This is an automatically generated file.
     It will be read and overwritten.
     DO NOT EDIT! -->
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<TITLE>Bookmarks</TITLE>
<H1>Bookmarks</H1>
<DL><p>
删除最后37行

替换所有的：
fa fa-apple为🍎
fa fa-laptop为💻
fa fa-linux为🐧
fa fa-windows为🪟
fa fa-android为🤖
fa fa-file-text-o为📄
fa fa-ban为🚫
fa fa-youtube-play为📺
fa fa-shopping-cart为🛒
fa fa-quote-left为📝
fa fa-link为🗂️
fa fa-gift为🎁
fa fa-exclamation-triangle为⚠️

从第九行开始遍历每一行：
如果有📄、🚫、📺、🛒、📝、🗂️、🎁、⚠️，则将其赋到一个「class」变量上；
将第一个">与</a或</i><a>与<中的非空字符赋到「description」变量上
将第一个网址赋到「main-link」上，如果有第二个链接，将其赋到「alt-link」变量上，并定义「alt-link-string」为「 备：alt-link」（不包含引号但包含「备」字前面的括号）。如果一个链接都没有，则将「https://separator.mayastudios.com/index.php?t=horz」赋到main-link上
如果有🍎、💻、🐧、🪟、🤖，将其赋到一个「platform」变量上。platform可以包含多个字符，且顺序要与原字符串一致。比如原字符串包含</a><i class="🤖"></i><i class="🍎"></i>，则platform为🤖🍎
如果含有notes="A"（其中A为任意字符），则将（A）赋到「notes」变量上

如果：
1. description不存在或为空：保留此行

2. description存在且不为空（+代表连接字符串，请保留行首的连续空格）：
2.1. 此行不包含fa fa-folder：将此行替换为：<DT><A HREF="main-link">class+description+notes+platform+alt-link-string</A>

2.2 此行包含fa fa-folder：将此行替换为：<DT><H3>description+notes</H3>

覆盖保存到temp.html

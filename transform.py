import sys
import re
from platform import platform

# 文件路径
input_file = r"index.html"
output_file = r"bookmarks-file-for-browser-import.html"

with open(input_file, "r", encoding="utf-8") as file:
    lines = file.readlines()

lines = lines[8:-37]

header_lines = [
    '<!DOCTYPE NETSCAPE-Bookmark-file-1>\n',
    '<!-- This is an automatically generated file.\n',
    '     It will be read and overwritten.\n',
    '     DO NOT EDIT! -->\n',
    '<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">\n',
    '<TITLE>Bookmarks</TITLE>\n',
    '<H1>Bookmarks</H1>\n',
    '<DL><p>\n'
]

new_lines = []
new_lines2 = []
new_lines3 = []
new_lines4 = []
new_lines5 = []
new_lines6 = []
new_lines7 = []
new_lines8 = []
new_lines9 = []
new_lines10 = []
new_lines11 = []
new_lines12 = []
new_lines13 = []
new_lines14 = []
new_lines15 = []
new_lines16 = []
new_lines17 = []
new_lines18 = []
new_lines19 = []
new_lines20 = []
new_lines21 = header_lines

for line in lines:
    new_line = line.replace("fa fa-apple", "🍎")
    new_lines.append(new_line)
for line in new_lines:
    new_line = line.replace("fa fa-laptop", "💻")
    new_lines2.append(new_line)
for line in new_lines2:
    new_line = line.replace("fa fa-linux","🐧")
    new_lines3.append(new_line)
for line in new_lines3:
    new_line = line.replace("fa fa-windows", "🪟")
    new_lines4.append(new_line)
for line in new_lines4:
    new_line = line.replace("fa fa-android",  "🤖")
    new_lines5.append(new_line)
for line in new_lines5:
    new_line = line.replace("fa fa-laptop", "💻")
    new_lines6.append(new_line)
for line in new_lines6:
    new_line = line.replace("fa fa-file-text-o", "📄")
    new_lines7.append(new_line)
for line in new_lines7:
    new_line = line.replace("fa fa-ban", "🚫")
    new_lines8.append(new_line)
for line in new_lines8:
    new_line = line.replace("fa fa-youtube-play", "📺")
    new_lines9.append(new_line)
for line in new_lines9:
    new_line = line.replace("fa fa-shopping-cart", "🛒")
    new_lines10.append(new_line)
for line in new_lines10:
    new_line = line.replace("fa fa-quote-left", "📝")
    new_lines11.append(new_line)
for line in new_lines11:
    new_line = line.replace("fa fa-link", "🗂️")
    new_lines12.append(new_line)
for line in new_lines12:
    new_line = line.replace("fa fa-gift", "🎁")
    new_lines13.append(new_line)
for line in new_lines13:
    new_line = line.replace("fa fa-exclamation-triangle", "⚠️")
    new_lines14.append(new_line)
for line in new_lines14:
    new_line = re.sub(r'^ {8}', '    ', line)
    new_lines15.append(new_line)
for line in new_lines15:
    new_line = line.replace("</ul></li>","</DL><p>")
    new_lines16.append(new_line)
for line in new_lines16:
    new_line = line.replace('<ul class="menu">','<DL><p>')
    new_lines17.append(new_line)
for line in new_lines17:
    new_line = line.replace('&amp;','&')
    new_lines18.append(new_line)
for line in new_lines18:
    new_line = re.sub(r'(?=>) +?','',line)
    new_lines19.append(new_line)

i = 0
for line in new_lines19:
    class_var = ""
    description = ""
    main_link = "https://separator.mayastudios.com/index.php?t=horz"
    alt_link = ""
    alt_link_string = ""
    platform = ""
    notes = ""
    notes_string = ""
    matches_1 = ""
    matches_2 = ""
    matches_3 = ""
    description_1 = ""
    description_2 = ""
    i = i + 1
    pattern_0 = re.compile(r'^ *')
    matches_0 = re.findall(pattern_0, line)
    space_part = matches_0[0]

    for symbol in ["📄", "🚫", "📺", "🛒", "📝", "🗂", "🎁", "⚠️"]:
        if symbol in line:
            class_var = class_var + symbol


    #  匹配 > 与 < 之间的最短字符
    pattern_1_1 = re.compile(r'(?<=">).+?(?=<\/a)')
    matches_1_1 = re.findall(pattern_1_1, line)
    if matches_1_1:
        description_1 = matches_1_1[0]
            # print(description_1)
    # 匹配 </i><a> 与 < 之间的最短字符
    else:
        pattern_2 = re.compile(r'(?<=</i><a>).+?(?=<)')
        matches_2 = re.findall(pattern_2, line)
        if matches_2:
            description_2 = matches_2[0]
        # print(description_2)
    description = description_1 + description_2
    if len(description) == 0:
        description = '————————'

    # 匹配第一个网址
    pattern_3 = re.compile(r'(?<=<a HREF=").+?(?=")')
    matches_3 = re.findall(pattern_3, line)
    if len(matches_3) >= 1:#应该等效于if matches_3:，都是确认匹配到了，至少匹配到了一个
        main_link = matches_3[0]
        if len(matches_3) >= 2:
            alt_link = matches_3[1]
            alt_link_string = " 备：" + alt_link


    for symbol in ["🍎", "💻", "🐧", "🪟", "🤖"]:
        if symbol in line:
            platform = platform + symbol

    pattern_4 = re.compile(r'notes="(.+?)"')
    match_4 = re.findall(pattern_4, line)
    if match_4:
        # 获取第一个匹配到的字符串
        notes = match_4[0]
        notes_string = "（" + notes + "）"
    # print(description)
    class_var = re.sub(r'(?<=<).*?(?=>)', '', class_var)
    description = re.sub(r'<.*?>','', description)
    main_link = re.sub(r'(?<=<).*?(?=>)','', main_link)
    notes_string = re.sub(r'<.*?>','', notes_string)
    platform = re.sub(r'(?<=<).*?(?=>)','', platform)
    alt_link_string = re.sub(r'(?<=<).*?(?=>)','', alt_link_string)
    print(description)
    if "</DL><p>" in line:
        new_line = space_part + "</DL><p>" + '\n'
    elif '<DL><p>' in line:
        new_line = space_part + '<DL><p>' + '\n'
    elif "fa fa-folder" in line:
        new_line = space_part + '<DT><H3>' + description + notes_string + '</H3>' + '\n'
    else:
        new_line = space_part + '<DT><A HREF="' + main_link + '">' + class_var + description + notes_string + platform + alt_link_string + '</A>' + '\n'
    # if i == 12:
    #    break

    new_lines20.append(new_line)
for line in new_lines20:
    new_lines21.append(line)

with open(output_file, "w", encoding="utf-8") as file:
    file.writelines(new_lines21)
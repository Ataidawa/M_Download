# -*- coding = utf-8 -*-

# 导入要用到的库
import os
import requests

# 定义一下基本变量
fileName = []  # 存储文件名的列表
fileNa = ''
fileLink = []  # 存储文件直链的列表

# 打开文件列表并读取内容
with open('filelist.txt','r',encoding='utf-8') as f:
    sco = f.read().split('\n')  # 请以第一行为文件名，第二行为文件直链的格式填写filelist.txt
    for i in range(len(sco)):
        if i%2==0:
            fileName.append(sco[i])
        else:
            fileLink.append(sco[i])

# 创建输出文件夹，避免报错
if not os.path.exists('output'):
    os.mkdir('output')

# 写入二进制文件
for x in range(len(fileLink)):
    # 管理扩展名
    if 'm4a' in fileLink[x]:
        exName = '.mp3'
    else:
        exName = '.mp4'
    # 管理文件名
    if '|' in fileName[x]:
        fileNames = fileName[x].split('|')
        for fi in range(len(fileNames)):
            fileNa = fileNa + fileNames[fi] + ' '
        fileName[x] = fileNa
        fileNa = ''
    # 获取文件内容
    score = requests.get(fileLink[x]).content
    with open('./output/%s%s'%(fileName[x],exName),'wb') as f:
        f.write(score)
    print('%s 请求完成！ %s'%(fileName[x],fileLink[x]))
print('保存文件完成！')
非常感谢你能看到这个项目。
这个项目是为了实现批量下载猫耳FM音频的功能，但因为我技术还不够成熟，所以有很多源文件，以后可能会有更多。

-- file_download.py --
里面用到了os、requests库。你需要在此文件的同级目录中创建一个“filelist.txt”文件，第一行填写保存的音视频文件名（无需后缀），第二行填写音频文件的request URL，由于无法突破获取request URL的难关，只能手动写了。

-- GetCookies.py --
里面用到了selenium、json库。运行此文件后会调出Google Chrome窗口，提示 你有一分钟时间登录。 登录完成后请不要操作页面，程序会保存一份Cookies在同级目录中，方便以后调用。

-- GetTitles.py --
里面用到了selenium、bs4库。该文件的作用是自动填写“filelist.txt”文件中的音频文件名，运行程序后输入drama链接（播放列表URL）即可开始获取音视频的标题作为文件名。

-- main.py --
该文件为最初的版本，里面用到了selenium、bs4、os、json、requests库。运行程序后会请求输入drama链接，然后读取Cookies文件，自动开始保存音视频文件。当出现“up禁止下载”时，文件会报错。

dist文件夹
内部是我使用pyinstaller封装完成的exe，你可以直接拿来使用。在使用之前请确保您安装了Google Chrome最新版且不要删除chromedriver.exe

** 特别 **
如果您对python爬虫请求某一文件的request URL有了解，请直接对我的文件下刀！_(:з」∠)_
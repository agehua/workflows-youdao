
# agehua/workflows-youdao

使用有道翻译新版本api：[有道智云翻译 API 简介](http://ai.youdao.com/docs/doc-trans-api.s#p01)

forked from ：https://github.com/kaiye/workflows-youdao

工程内的 youdao.alfredworkflow，本质是一个压缩包。

所以你也可以自己随便修改，把整个工程压缩成一个zip包，然后修改扩展名为 .alfredworkflow，在电脑上双击 Alfred 就会识别并提示安装。

工程里的 youdaotest.py 是用来测试有道API的，可以删除。youdao.py 才是真正的执行文件，里面有 appKey 和 secretKey （建议大家配置成自己的:( ）


`下面内容原内容相同：`

使用方法，选中需要翻译的文本，按两下 `command` 键即可。选中结果后，配合以下功能键可实现不同功能：

* `enter` 同步单词到有道在线单词本（若未配置有道账号则保存至本地单词本）
* `alt + enter` 翻译至剪切板
* `shift + enter` 直接发音
* `control + enter` 打开有道翻译页面
* `command + enter` 直接在光标处打出翻译结果

## 安装

### 1、[点击下载](https://github.com/agehua/workflows-youdao/blob/master/youdao.alfredworkflow?raw=true)
提示安装界面，Category 选择 Tools。

### 2、安装后设置双击快捷键

![按两下 command 设置快捷键](https://cloud.githubusercontent.com/assets/344283/12189204/b0d21524-b5f6-11e5-9cc8-33c17561f9ee.gif)



### 3、配置有道词典账号信息

![配置账号信息](https://cloud.githubusercontent.com/assets/344283/12175374/c776aef2-b59c-11e5-90ec-20e3801ff7ed.png)

如上图所示，双击 alt 相关的 Run Script，在弹出的 Script 框中参照以上格式配置相关参数：

* `-filepath`  指定本地单词本的绝对路径，若不设置则默认为当前用户 Documents/Alfred-youdao-wordbook.xml 路径
* `-username` 有道词典用户邮箱，用于模拟登录、同步单词信息
* `-password` 有道词典用户密码



## 演示

### 英译中

![](http://ww2.sinaimg.cn/large/48910e01gw1erucr05z85g213p0kbqhn.gif)

### 中译英

![](http://ww2.sinaimg.cn/large/48910e01gw1erucrd5tnmg213p0kbk6q.gif)

### 翻译短语

![](http://ww2.sinaimg.cn/large/48910e01gw1erucrvb9a8g213p0kbqhn.gif)

### 使用浏览器搜索

![](http://ww4.sinaimg.cn/large/48910e01gw1erucsmvtkgg213l0kaqq2.gif)

### 输出结果到光标所在应用程序

![](http://ww3.sinaimg.cn/large/48910e01gw1eructbvt9rg213p0jh0wi.gif)

注：本插件 fork 自 liszd/whyliam.workflows.youdao 的 v1.2.1 版本，由于改动较大就不提 PR 了，协议保持 MIT 不变，请随意订制。
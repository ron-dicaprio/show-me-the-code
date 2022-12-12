## Python 练习册，每天一个小程序 ##


#### 说明： ####

- Python 练习册，每天一个小程序。注：将 Python 换成其他语言，大多数题目也适用
- 不会出现诸如「打印九九乘法表」、「打印水仙花」之类的题目
- 本文本文由@史江歌（shijiangge@gmail.com  QQ:499065469）根据互联网资料收集整理而成，感谢互联网，感谢各位的分享。鸣谢！本文会不断更新。
- 欢迎大家 Pull Request 出题目，贴代码（Gist、Blog皆可）:-)
- 欢迎解答, 并发送 pull request 到 [Show-Me-the-Code](https://github.com/Show-Me-the-Code/python)

> Talk is cheap. Show me the code.--Linus Torvalds

----------

**第 0000 题：**  将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
类似于图中效果

![头像](http://i.imgur.com/sg2dkuY.png?1)
```python
from PIL import Image,ImageDraw,ImageFont
def get_pic_mark():
    # 打开图片
    pic=Image.open('logo.png')
    # 初始化Draw
    draw=ImageDraw.ImageDraw(pic)
    # 定义创建字体
    fonts=ImageFont.truetype("C:\\WINDOWS\\Fonts\\Consolas\\consolaz.ttf", 108)
    draw.text((pic.width * 0.8, pic.height * 0.1), u"8", font=fonts, fill='red')
    pic.save('save.png')
    return 1
```
![icon](https://raw.githubusercontent.com/ron-dicaprio/show-me-the-code/master/save.png)  

**第 0001 题：** 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券）,使用 Python 如何生成 200 个激活码（或者优惠券）？
```python
def get_active_code(Lenth,Nums):
    active_code_list=[]
    # 取值的池子
    code_pool = "0123456789" + string.ascii_uppercase     
    for codes in range(0,Nums):
        # 定义取值长度
        # choices:放回抽样,sample:不放回抽样
        # active_code = ''.join(random.choices(code_pool,k=Lenth))
        active_code = ''.join(random.sample(code_pool,Lenth))
        if active_code in active_code_list:
            # 如果有重复的会导致生成出来active_code_list的数量少一位. 
            # todo list
            pass
        else:
            active_code_list.append(active_code)
    return active_code_list
```

**第 0002 题**：将 0001 题生成的 200 个激活码（或者优惠券）保存到MySQL 关系型数据库中。
```python
import pymysql
def exec_pymysql(str_sql):
    try:
        conn = pymysql.connect(host='127.0.0.1', user='root',db='active_codes', passwd='Gepoint',charset='utf8mb4')
        cur = conn.cursor()
        cur.execute(str_sql)
        conn.commit()
        conn.close()
        return cur.fetchall()
    except Exception as ERRORS:
        return ERRORS

str_sql1="CREATE TABLE `active_codes_pool`  ( \
    `No` int(11) NOT NULL AUTO_INCREMENT PRIMARY key, \
    `active_code` varchar(50) NOT NULL \
    ) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4;"
try:
    res1 = exec_pymysql(str_sql1)
    print(res1)
except Exception as e:
    print(e)

for active_codes in get_active_code(20,10):
    print(active_codes)
    str_sql2='insert into active_codes_pool (active_code) values ("%s") ' % (active_codes)
    try:
        res2 = exec_pymysql(str_sql2)
        print(res2)
    except Exception as e:
        print(e)
```

**第 0003 题：** 将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。
```python
import redis
# 连接redis，写到序号0的缓存库中
redis_conn=redis.Redis(host='127.0.0.1',port=6379,DB=0)

# 没装redis 未进行单元测试
for redis_value in get_active_code(20,10):
    redis_conn.lpush('code',redis_value) 

```


**第 0004 题：** 任一个英文的纯文本文件，统计其中的单词出现的个数。
```python
import string,re
def get_count():
    get_count_list=dict()
    code_pool = string.ascii_uppercase 
    content=open('D:\\script-factory\\python factory\\pyfile\\aria2c.txt','r').read().upper()
    #print(content)
    for key in code_pool:
        res = re.findall(key,content)
        print(key,':',len(res))
        get_count_list.update({key:len(res)})
        print(get_count_list)
    content.close()
    return get_count_list
```

**第 0005 题：** 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
```python
import re,os
from PIL import Image
# get filename from url address.
def get_image_from_files(url):
    pattern = re.search("([|.|\w|\s|-])*?.(jpg|png|jpeg|bmp)", url.lower())
    if not pattern:
        return False
    else:
        return True

# 获取当前目录下文件
pathdir=os.getcwd()
# 只取一级目录
for pics in os.listdir(pathdir):
    pic_path=pathdir+'\\'+pics
    # 判断是否图片
    if get_image_from_files(pic_path) == True:
        cut_pics=Image.open(pic_path)
        # cut_pics.width,cut_pics.height 828
        if cut_pics.width > 828  and  cut_pics.height > 1792:
            save_pics=cut_pics.resize((828,1792))
            save_pics.save('save_'+pic_path)
            print('file saved!')
        else:
            print(pic_path,':',cut_pics.width,'*',cut_pics.height)

    else:
        pass
```

**第 0006 题：** 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。

**第 0007 题：** 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。

**第 0008 题：** 一个HTML文件，找出里面的正文。

**第 0009 题：** 一个HTML文件，找出里面的链接。

**第 0010 题：** 使用 Python 生成类似于下图中的**字母验证码图片**

![字母验证码](http://i.imgur.com/aVhbegV.jpg)

- [阅读资料](http://stackoverflow.com/questions/2823316/generate-a-random-letter-in-python)

**第 0011 题：** 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

    北京
    程序员
    公务员
    领导
    牛比
    牛逼
    你娘
    你妈
    love
    sex
	jiangge

**第 0012 题：** 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。

**第 0013 题：** 用 Python 写一个爬图片的程序，爬 [这个链接里的日本妹子图片 :-)](http://tieba.baidu.com/p/2166231880)

- [参考代码](http://www.v2ex.com/t/61686 "参考代码")

**第 0014 题：** 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：

    {
    	"1":["张三",150,120,100],
    	"2":["李四",90,99,95],
    	"3":["王五",60,66,68]
    }

请将上述内容写到 student.xls 文件中，如下图所示：

![student.xls](http://i.imgur.com/nPDlpme.jpg)

- [阅读资料](http://www.cnblogs.com/skynet/archive/2013/05/06/3063245.html) 腾讯游戏开发 XML 和 Excel 内容相互转换

**第 0015 题：** 纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：

    {
        "1" : "上海",
        "2" : "北京",
        "3" : "成都"
    }

请将上述内容写到 city.xls 文件中，如下图所示：

![city.xls](http://i.imgur.com/rOHbUzg.png)


**第 0016 题：** 纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：

    [
    	[1, 82, 65535],
    	[20, 90, 13],
    	[26, 809, 1024]
    ]

请将上述内容写到 numbers.xls 文件中，如下图所示：

![numbers.xls](http://i.imgur.com/iuz0Pbv.png)

**第 0017 题：** 将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中，如

下所示：

    <?xml version="1.0" encoding="UTF-8"?>
    <root>
    <students>
    <!--
    	学生信息表
    	"id" : [名字, 数学, 语文, 英文]
    -->
    {
    	"1" : ["张三", 150, 120, 100],
    	"2" : ["李四", 90, 99, 95],
    	"3" : ["王五", 60, 66, 68]
    }
    </students>
    </root>

- [阅读资料](http://www.cnblogs.com/skynet/archive/2013/05/06/3063245.html) 腾讯游戏开发 xml 和 Excel 相互转换

**第 0018 题：** 将 第 0015 题中的 city.xls 文件中的内容写到 city.xml 文件中，如下所示：

    <?xmlversion="1.0" encoding="UTF-8"?>
    <root>
    <citys>
    <!--
    	城市信息
    -->
    {
    	"1" : "上海",
    	"2" : "北京",
    	"3" : "成都"
    }
    </citys>
    </root>

**第 0019 题：** 将 第 0016 题中的 numbers.xls 文件中的内容写到 numbers.xml 文件中，如下

所示：

    <?xml version="1.0" encoding="UTF-8"?>
    <root>
    <numbers>
    <!--
    	数字信息
    -->

    [
    	[1, 82, 65535],
    	[20, 90, 13],
    	[26, 809, 1024]
    ]

    </numbers>
    </root>

**第 0020 题：** [登陆中国联通网上营业厅](http://iservice.10010.com/index_.html) 后选择「自助服务」 --> 「详单查询」，然后选择你要查询的时间段，点击「查询」按钮，查询结果页面的最下方，点击「导出」，就会生成类似于 2014年10月01日～2014年10月31日通话详单.xls 文件。写代码，对每月通话时间做个统计。

**第 0021 题：** 通常，登陆某个网站或者 APP，需要使用用户名和密码。密码是如何加密后存储起来的呢？请使用 Python 对密码加密。

- 阅读资料 [用户密码的存储与 Python 示例](http://zhuoqiang.me/password-storage-and-python-example.html)

- 阅读资料 [Hashing Strings with Python](http://www.pythoncentral.io/hashing-strings-with-python/)

- 阅读资料 [Python's safest method to store and retrieve passwords from a database](http://stackoverflow.com/questions/2572099/pythons-safest-method-to-store-and-retrieve-passwords-from-a-database)

**第 0022 题：** iPhone 6、iPhone 6 Plus 早已上市开卖。请查看你写得 第 0005 题的代码是否可以复用。

**第 0023 题：** 使用 Python 的 Web 框架，做一个 Web 版本 留言簿 应用。

[阅读资料：Python 有哪些 Web 框架](http://v2ex.com/t/151643#reply53)

- ![留言簿参考](http://i.imgur.com/VIyCZ0i.jpg)


**第 0024 题：** 使用 Python 的 Web 框架，做一个 Web 版本 TodoList 应用。

- ![SpringSide 版TodoList](http://i.imgur.com/NEf7zHp.jpg)

**第 0025 题：** 使用 Python 实现：对着电脑吼一声,自动打开浏览器中的默认网站。


    例如，对着笔记本电脑吼一声“百度”，浏览器自动打开百度首页。

    关键字：Speech to Text

参考思路：
1：获取电脑录音-->WAV文件
    python record wav

2：录音文件-->文本

    STT: Speech to Text

    STT API Google API

3:文本-->电脑命令

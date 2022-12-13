#-*- coding:utf-8 -*-
#!/usr/bin/env python
""" 
# 第 0000 题：**将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
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



# 第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）。
import random,string
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

# 将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
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

#str_sql="create database active_codes charset = utf8;"
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

# 将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。
import redis
# 连接redis，写到序号0的缓存库中
redis_conn=redis.Redis(host='127.0.0.1',port=6379,DB=0)

# 没装redis 未进行单元测试
for redis_value in get_active_code(20,10):
    redis_conn.lpush('code',redis_value) 

# **第 0004 题：**任一个英文的纯文本文件，统计其中的单词出现的个数。
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


# **第 0005 题：**你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone11 分辨率的大小。
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


# 使用 Python 生成字母验证码图片
# 代码需要优化
import random,string
from PIL import Image,ImageDraw,ImageFont,ImageFilter
# 字符集
#code_pool = '0123456789' + string.ascii_lowercase + string.ascii_uppercase
code_pool = string.ascii_lowercase + string.ascii_uppercase

# 使得同一个验证码中字符不重复
active_code = ''.join(random.sample(code_pool,4))

# 生成一个600*140的图片对象
verify_pics=Image.new('RGB', (600, 140), (255, 255, 255))

fonts=ImageFont.truetype("C:\\WINDOWS\\Fonts\\Consolas\\consolaz.ttf", 108)
draw=ImageDraw.ImageDraw(verify_pics)

# 定义随机颜色函数
def RandomColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# verify_pics像素填充
for x in range(verify_pics.width):
    for y in range(verify_pics.height):
        draw.point((x, y), fill=RandomColor())

# 减少三次verify_pics_height计算
verify_pics_height=verify_pics.height * 0.2
index = 1
for words in active_code:
    draw.text((verify_pics.width * 0.2 * index,  verify_pics_height), words, font=fonts, fill=RandomColor())
    index+=1

# 模糊处理一下
verify_pics = verify_pics.filter(ImageFilter.BLUR)
verify_pics.save('save.png')


# 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

f_words='北京 \
程序员 \
公务员 \
领导 \
牛比 \
牛逼 \
你娘 \
你妈 \
love \
sex \
jiangge'

input_words=input('请输入内容：\n')
Freedom=0
for word in f_words.split():
    if word in input_words:
        print('Freedom')
        Freedom=1
    else:
        pass

if Freedom==1:
    pass
else:
    print('Human Rights')

#  敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
f_words='北京 \
程序员 \
公务员 \
领导 \
牛比 \
牛逼 \
你娘 \
你妈 \
love \
sex \
jiangge'

input_words=input('请输入内容：\n')

Freedom=0
for word in f_words.split():
    if word in input_words:
        res=input_words.replace(word,'*'*len(word))
        print(res)
        Freedom=1
    else:
        pass

if Freedom==0:
    print(input_words)




# 使用 Python 实现：对着电脑吼一声,自动打开浏览器中的默认网站。
# encoding = utf-8

# use pyAudio
# brew install portaudio
# pip install pyaudio

import wave, pyaudio
from datetime import datetime
from tools import dxbaiduaudio
import webbrowser

CHUNK = 1024
FORMAT = pyaudio.paInt16
RATE = 8000
CHANNELS = 1
RECORD_SECONDS = 5

def record_wave(to_dir=None):
    if to_dir is None:
        to_dir = "./"

    pa = pyaudio.PyAudio()
    stream = pa.open(format = FORMAT,
                     channels = CHANNELS,
                     rate = RATE,
                     input = True,
                     frames_per_buffer = CHUNK)

    print("* recording")

    save_buffer = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        audio_data = stream.read(CHUNK)
        save_buffer.append(audio_data)

    print("* done recording")

    # stop
    stream.stop_stream()
    stream.close()
    pa.terminate()

    # wav path
    file_name = datetime.now().strftime("%Y-%m-%d_%H_%M_%S")+".wav"
    if to_dir.endswith('/'):
        file_path = to_dir + file_name
    else:
        file_path = to_dir + "/" + file_name

    # save file
    wf = wave.open(file_path, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(pa.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    # join 前的类型
    wf.writeframes(b''.join(save_buffer))
    wf.close()

    return file_path

def browser_open_text(text):
    if text is None:
        return

    url = "http://www.baidu.com"
    if text.startswith("谷歌") or text.startswith("google"):
        url = "http://www.google.com"
    elif text.startswith("必应") or text.startswith("bing"):
        url = "http://cn.bing.com"

    webbrowser.open_new_tab(url)

if __name__ == "__main__":
    to_dir = "./"
    file_path = record_wave(to_dir)

    text = dxbaiduaudio.wav_to_text(file_path)
    browser_open_text(text)
"""
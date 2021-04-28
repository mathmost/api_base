# coding: utf-8
import sys
from you_get import common as you_get

download_dir = r'F:\vue黑马头条'
for i in range(257):
    download_url = r'https://www.bilibili.com/video/BV1yf4y167P6?p={}'.format(i)
    sys.argv = ['you-get', '-o', download_dir, download_url]
    you_get.main()

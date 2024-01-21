import requests
from datetime import datetime
import os

def download_image(url, file_path):
    response = requests.get(url)  # 发送GET请求获取响应对象
    with open(file_path, 'wb') as f:  # 以二进制写入模式打开文件
        f.write(response.content)  # 将响应内容写入文件

def main():
    # now = datetime.now()  # 获取当前日期时间
    # date = now.date()  # 获取当前日期
    # folder = str(date)  # 文件夹名称为日期字符串
    # if not os.path.exists(folder):  # 如果文件夹不存在，则创建文件夹
    #     os.makedirs(folder)
        
    url = 'https://www.dmoe.cc/random.php?return=json'
    turl = requests.get(url).json()
    url = turl['imgurl']
    filename = url.split("/")[-1]
    # file_path = os.path.join(folder, filename)  # 构建完整的文件路径
    file_path='./'+filename
    download_image(url, file_path)

if __name__ == '__main__':
    main()

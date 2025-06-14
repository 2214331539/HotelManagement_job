git clone <你的GitHub仓库URL>
cd HotelManageSystem

# 进入后端目录
cd HotelManageSystemBackend

# 创建虚拟环境（使用Python 3.10）
python -m venv venv

# 激活虚拟环境
# Linux
# source venv/bin/activate

# 安装所有Python依赖
pip install -r requirements.txt

# 安装额外的cryptography包（用于MySQL认证）
pip install cryptography

   CREATE DATABASE IF NOT EXISTS db_hotel;
    mysql -u root -p db_hotel < db_hotel.sql

settings.py
       DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'db_hotel',
           'USER': 'root',
           'PASSWORD': '你的MySQL密码',
           'HOST': '127.0.0.1',
           'PORT': '3306',
       }
   }

   数据库迁移
   python manage.py migrate

1、数据库环境配置
mysql -u root -p
create database db_hotel
source /path/to/db_hotel.sql;
/HotelManageSystem/settings.py

D:\Conda\envs\Stock\python.exe -m venv venv#创建虚拟环境
.\venv\Scripts\activate.ps1     #激活虚拟环境
install


运行：
cd HotelManageSystemBackend
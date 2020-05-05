# PESI（[English version README](./README-EN.md)）
从终端打包Python项目到远程Docker服务器

## 使用环境（目前测试）
- Ubuntu 18.04.4 LTS /  Ubuntu 16.04.6 LTS
- Python 3.5,3.6
 
## Base on python package
- click == 7.1.1
- docker == 4.1.0
   
## 安装
    pip install pesi

## 快速上手(example)
> **注意**: 确保你要远程的Docker服务器或者本地Docker已经打开remote api端口,取决于你在setup.cfg里面的配置(
https://success.docker.com/article/how-do-i-enable-the-remote-api-for-dockerd)
    
    git clone https://github.com/pesi1874/pesi.git
    cd psei/example
    pesi init  <这一步骤会将test-project文件夹拷贝到depoly文件夹中，并重命名为app>
    pesi build  <这一步骤会使用docker sdk，先拷贝整个项目到远程docker服务器，再打包成镜像>

## 项目文件结构要求
    |-- project-name/
        |--deploy/
            |-- Dockerfile
            |-- requirements.txt
            |-- run.sh
        |--project-name/
            |--main.py
        |--setup.cfg
        
## 构建项目
    cd <python project>
    pesi init
    pesi build

## Help
    pesi --help
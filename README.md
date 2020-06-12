# PESI（[English version README](./README-EN.md)）
从终端打包Python项目到远程Docker服务器

## 使用环境（目前测试）
- Linux
- Python 3.5 / 3.6
 
## Base on python package
- click == 7.1.1
- docker == 4.1.0(已经集成在lib中)
- requests == 2.23.0
- websocket == 0.2.1
   
## 安装
```bash
    sudo pip install pesi
```

## 快速上手(example)
> **注意**: 确保你要远程的Docker服务器或者本地Docker已经打开remote api端口,取决于你在setup.cfg里面的配置(
https://success.docker.com/article/how-do-i-enable-the-remote-api-for-dockerd)

```bash
    git clone https://github.com/pesi1874/pesi.git
    cd psei/example
    pesi build
```

## 项目文件结构要求
```bash
|-- project-name/
    |--deploy/
        |-- Dockerfile
        |-- requirements.txt
        |-- run.sh
    |--project-name/
        |--main.py
    |--setup.cfg
```
        
## 构建项目
```bash
    cd <python project>
    pesi build
```


## Help
```bash
    pesi --help
```

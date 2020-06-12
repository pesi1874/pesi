# PESI
Build your python project on remote Docker server from Terminal

## Environment
- Linux
- Python 3.5 / 3.6
  
## Base on python package
- click == 7.1.1
- docker == 4.1.0(已经集成在lib中)
- requests == 2.23.0
- websocket == 0.2.1

## Installation
    sudo pip install pesi

## Quick Start(example)
> **WARNING**: Make sure you had opened remote api for docker server or local docker server,up to setup.cfg in the 
example(https://success.docker.com/article/how-do-i-enable-the-remote-api-for-dockerd)

```bash
    git clone https://github.com/pesi1874/pesi.git
    cd psei/example
    pesi build
```

## Project Dir Demand
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
            
## Build project
```bash
    cd <python project>
    pesi build
```

## Help
```bash
    pesi --help
```
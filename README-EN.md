# PESI
Build your python project on remote Docker server from Terminal

## Environment
- Ubuntu 18.04.4 LTS / Ubuntu 16.04.6 LTS
- Python 3.5,3.6
  
## Base on python package
- click == 7.1.1
- docker == 4.1.0

## Installation
    sudo pip install pesi

## Quick Start(example)
> **WARNING**: Make sure you had opened remote api for docker server or local docker server,up to setup.cfg in the 
example(https://success.docker.com/article/how-do-i-enable-the-remote-api-for-dockerd)

    git clone https://github.com/pesi1874/pesi.git
    cd psei/example
    pesi init  <this step will copy test-project to dir depoly with name app>
    pesi build  <this step will use docker-py api to build docker image on your docker server>

## Project Dir Demand
    |-- project-name/
        |--deploy/
            |-- Dockerfile
            |-- requirements.txt
            |-- run.sh
        |--setup.cfg
        |--project-name/
            |--main.py
            
## Build project
    cd <python project>
    pesi init
    pesi build

## Help
    pesi --help
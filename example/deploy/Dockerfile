FROM python:3.6.10

WORKDIR /docker-app

ADD . /docker-app

RUN chmod a+x run.sh

RUN pip install -r requirements.txt

RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' >/etc/timezone

CMD /bin/sh run.sh

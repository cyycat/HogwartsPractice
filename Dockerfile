FROM python:3.6
ADD . /code
WORKDIR /code
ADD requirements.txt /code
RUN python -m pip install -i https://mirrors.aliyun.com/pypi/simple pip -U && \
    python -m pip install -r /code/requirements.txt -i https://mirrors.aliyun.com/pypi/simple --timeout=240
CMD ["python", "mian.py"]
EXPOSE 8000
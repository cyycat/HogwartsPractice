FROM python:3.6
ADD HogwartsPractice /code/HogwartsPractice
ADD requirements.txt /code/
RUN python -m pip install -i https://mirrors.aliyun.com/pypi/simple pip -U && \
    python -m pip install -r /opt/requirements.txt -i https://mirrors.aliyun.com/pypi/simple --timeout=240
CMD ["python", "/code/HogwartsPractice/mian.py"]
EXPOSE 8000

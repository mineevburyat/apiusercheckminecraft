FROM python:3.9
WORKDIR /opt
COPY requirements.txt ./
COPY config.ini ./
COPY app/ ./app
COPY bot_logging/ ./bot_logging
COPY main.py ./
RUN pip install --no-cache-dir -r requirements.txt

# CMD [ "sh" ] 

ENTRYPOINT [ "python", "main.py"]

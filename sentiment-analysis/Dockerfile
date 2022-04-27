FROM python:3.8
RUN mkdir /app
ADD . /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["tail", "-f", "/dev/null"]
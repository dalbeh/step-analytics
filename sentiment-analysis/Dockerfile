FROM python:3.8
RUN mkdir /app
ADD ./requirements.txt /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
CMD uvicorn src.app:app --proxy-headers --host 0.0.0.0 --port 8000
# CMD ["tail", "-f", "/dev/null"]
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY AntiAnti .
EXPOSE 8000
ENV PYTHONUNBUFFERED=1
CMD ["python3", "manage.py", "runserver","0.0.0.0:8000"]
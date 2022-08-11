FROM python:3.10-buster

WORKDIR /code

COPY ./ /code
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /code/requirements.txt

# CMD ["python3", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
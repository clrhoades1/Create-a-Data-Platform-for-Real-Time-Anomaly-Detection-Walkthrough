FROM python:3.7-slim
RUN mkdir src
WORKDIR /src

COPY /service/requirements.txt /src
COPY /service/main.py /src
COPY /jupyter/data/model.joblib /src

RUN pip install -r /src/requirements.txt
CMD ["uvicorn", "main:app" ,"--host", "0.0.0.0", "--port", "8000"]
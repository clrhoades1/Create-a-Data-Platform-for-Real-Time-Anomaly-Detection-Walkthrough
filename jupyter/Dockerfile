FROM python:3.7-slim
RUN mkdir src
WORKDIR /src

COPY requirements.txt /src

RUN pip install -r /src/requirements.txt
CMD ["jupyter", "notebook", "--allow-root", "--ip", "0.0.0.0", "--no-browser"]
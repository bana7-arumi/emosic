FROM python:3.8-buster as builder
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY ./docker/cpu/requirements.txt .
RUN /usr/local/bin/python -m pip install --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt

FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED=1
ENV SHELL=/bin/bash
WORKDIR /app

COPY --from=builder /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages

# alias python='python3'
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN pip install uvicorn==0.20.0
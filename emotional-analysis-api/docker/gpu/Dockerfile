FROM nvidia/cuda:11.6.0-base-ubuntu20.04
ENV PYTHONUNBUFFERED=1
ENV SHELL=/bin/bash
WORKDIR /app

RUN apt-get update && apt-get install -y \
    python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# alias python='python3'
RUN ln -s /usr/bin/python3 /usr/bin/python

COPY ./docker/gpu/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir torch==1.12.1+cu116 torchvision==0.13.1+cu116 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu116

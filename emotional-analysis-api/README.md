![FastAPI](https://img.shields.io/badge/-FastAPI-blue.svg?logo=fastAPI&style=flat)
![docker](https://img.shields.io/badge/-Docker-EEE.svg?logo=docker&style=flat)
![Python](https://img.shields.io/badge/-Python3.8-yellow.svg?logo=python&style=flat)
![cuda](https://img.shields.io/badge/cuda-11.6.0-EEE&style=flat)
# emotional-analysis-api

This application is a `Japanese` emotion analysis webapi for microservices.

![request](/img/request.png)

GPU use is recommended, but can also work with CPU

## For GPU users

If using a GPU, install the latest drivers from [Nvidia](https://www.nvidia.co.jp/Download/index.aspx?lang=en)

*!-No need to install the CUDA tool kit in your local environment-!*

## versions

| Docker image | version |
| :---: | :---: |
| python | 3.8 |
| CUDA(Ubuntu20.04) | 11.6.0 |

| Python library | version(cpu) | version(gpu) |
| :---: | :---: | :---: |
| torch | 1.13.1 | 1.12.1+cu116 |
| transformers | 4.26.0 | " |
| fugashi | 1.2.1 | " |
| ipadic | 1.0.0 | " |
| fastapi | 0.89.1 | " |
| uvicorn | 0.20.0 | " |
| numpy | 1.24.1 | " |

# -Get Started-

## BERT Model install

[Click here](https://drive.google.com/drive/u/0/folders/1EDWTA33GOipyTcy7VFTozal1PoSNTToZ) to see the model.

![model](/img/model.png)

This machine learning model was created using one published on [Hugging Face](https://huggingface.co/)

| name | url |
| :---: | :---: |
| Pre-trained bert model and Tokenizer | [cl-tohoku/bert-base-japanese-whole-word-masking](https://huggingface.co/cl-tohoku/bert-base-japanese-whole-word-masking) |
| dataset | [tyqiangz/multilingual-sentiments](https://huggingface.co/datasets/tyqiangz/multilingual-sentiments) |

The BERT model needs to be saved in `emotional-analysis-api/app/`.

```console
$ tree .
.
├── app
│   ├── EmotionAnalysisModel
...
```

Script to download models from Google Drive.

```console
$ ./model-install.sh
```


## Build

To use a pre-built docker image, do the following

need to change the build context in docker-compose.XXX.yml

XXX is cpu or gpu

```diff
version: "3"

services:
  api:
-    build:
-      context: .
-      dockerfile: ./docker/XXX/Dockerfile
+    image: bana7/japanese-emotional-analysis-api:XXX
```

[Click here](https://hub.docker.com/repository/docker/bana7/japanese-emotional-analysis-api/general) for more information about docker images.

In BUILD, install the following Python libraries and create a Docker image.

- torch
- transformers
- fugashi
- ipadic
- fastapi
- uvicorn
- numpy

Build time takes about 10 minutes :)


#### CPU

```console
$ docker compose -f docker-compose.cpu.yml build
```

or

```console
$ make build
```

#### GPU

```console
$ docker compose -f docker-compose.gpu.yml build
```

or

```console
$ make-gpu build
```

## Run

To run the generated Docker image, type the following command.

#### CPU

```console
$ docker compose -f docker-compose.cpu.yml up -d
```

or

```console
$ make up
```

#### GPU

```console
$ docker compose -f docker-compose.gpu.yml up -d
```

or

```console
$ make-gpu up
```

## Down

To stop a running container, enter the following command.

#### CPU

```console
$ docker compose -f docker-compose.cpu.yml down
```

or

```console
$ make down
```

#### GPU

```console
$ docker compose -f docker-compose.gpu.yml down
```

or

```console
$ make-gpu down
```

# -End point-

Application is running on [http://127.0.0.1:8000](http://127.0.0.1:8000)

Since we are using FastAPI, we can access [http://127.0.0.0:8000/docs](http://127.0.0.0:8000/docs) to see the api document

# -Request-

If requesting from a client PC, do the following

```console
$ curl  -X POST -H "Content-Type: application/json" -d '{"text": "ほげ"}' http://127.0.0.1:8000/inference
```

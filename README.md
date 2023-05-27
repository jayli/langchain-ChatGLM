# 可以在 MacBook 上部署的本地知识库大模型 langchain + chatglm + chatyuan

本项目 form 自 <https://github.com/imClumsyPanda/langchain-ChatGLM>，原理和概念用法请看原文，这里只说下为什么在 MacBook 上部署大模型以及如何做？

## 介绍

和 ChatGLM 搭配最好、也是效果最好的大模型肯定是 [ChatGLM-6B](https://github.com/THUDM/ChatGLM-6B)，没有 N 卡的情况下太慢，尽管可以用 mps 给 AMD GPU 加速，在 Mac 上一次计算有两三分钟才返回。最后还是选择入门级 [ChatYuan2](https://huggingface.co/ClueAI/ChatYuan-large-v2)。如果机器可以，最好还是用 chatglm-6b。

## 硬件条件

- CPU：2.6 GHz 六核Intel Core i7
- 内存：32 GB 2667 MHz DDR4
- 显卡：AMD Radeon RX 6600 8 GB

## 软件条件

python 3.8 及以上

## 安装

  git clone git@github.com:jayli/langchain-ChatGLM.git
  cd langchain-ChatGLM
  pip install -r requirements.txt
  python cli_chatyuan.py

服务启动：

  python server.py

访问本机的 7788 端口

   curl -d "ask=helloworld" -H "Content-Type: application/x-www-form-urlencoded" -X POST http://127.0.0.1:7788/ai/langchain/

默认启动的是 chatyuan 模型。如果要用 chatGLM-6b 模型，需要手动下载，[参照这里](https://github.com/THUDM/ChatGLM-6B/issues/6#issuecomment-1471303336)
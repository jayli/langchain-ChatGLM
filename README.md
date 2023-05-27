# 可以在你的 MacBook 上部署的本地知识库大模型 langchain + chatglm + chatyuan

本项目 form 自 <https://github.com/imClumsyPanda/langchain-ChatGLM>，原理和概念用法请看原文，这里只说下为什么在 MacBook 上部署大模型以及如何做？

## 介绍

和 ChatGLM 搭配最好、也是效果最好的大模型肯定是 [ChatGLM-6B](https://github.com/THUDM/ChatGLM-6B)，没有 N 卡的情况下太慢，尽管可以用 mps 给 AMD GPU 加速，在 Mac 上一次计算有两三分钟才返回。最后还是选择入门级 [ChatYuan2](https://huggingface.co/ClueAI/ChatYuan-large-v2)。

## 硬件条件

- CPU：2.6 GHz 六核Intel Core i7
- 内存：32 GB 2667 MHz DDR4
- 显卡：AMD Radeon RX 6600 8 GB

需要说明的是，GhatGLM-6B 



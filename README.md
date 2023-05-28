# 在 MacBook 上部署的本地知识库大模型 langchain + chatglm / chatyuan

本项目 form 自 <https://github.com/imClumsyPanda/langchain-ChatGLM>，原理和概念用法请看原文，这里只说下为什么在 MacBook 上部署大模型以及如何做？

## 介绍

效果比较好的大模型肯定是 [ChatGLM-6B](https://github.com/THUDM/ChatGLM-6B)，没有 N 卡的情况下太慢，尽管可以用 mps 给 AMD GPU 加速，在 Mac 上一次计算有两三分钟才返回。这里选择入门级 [ChatYuan2](https://huggingface.co/ClueAI/ChatYuan-large-v2)。如果机器可以，最好还是用 chatglm-6b。

## 硬件条件

我的机器:

- CPU：2.6 GHz 六核Intel Core i7
- 内存：32 GB 2667 MHz DDR4
- 显卡：AMD Radeon RX 6600 8 GB
- OS：MacOS 12.6

## 软件条件

python 3.8 及以上

## 安装

### Chatyuan 模型（默认）

```
git clone git@github.com:jayli/langchain-ChatGLM.git
cd langchain-ChatGLM
pip install -r requirements.txt

# 命令行
python cli_chatyuan.py

# 启动服务
```

两个启动方式

1. 命令行方式启动：`python cli_chatyuan.py`
1. 服务方式启动：`python server.py`

启动服务后默认开启本机 8899 端口，这样访问

   curl -d "ask=helloworld1" \
        -H "Content-Type: application/x-www-form-urlencoded"  \
        -X POST http://127.0.0.1:8899/ai/langchain/

返回结果：

    {"content":"\u60a8\u9700\u8981\u9884\u5b9a\u673a\u7968\u5417?","status":200}

> 注意：
> - curl 命令中传参数不要有空格，如果需要测试最好用 postman 之类的工具
> - server 启动用的 flask，如果需要其他机器访问，修改`server.py` 中服务启动加上本地 host：`app.run(debug=False, port=8899, host="192.168.0.11")`

### ChatGLM-6b 模型

回到`langchain-ChatGLM`所在的目录，[参照这里](https://github.com/THUDM/ChatGLM-6B/issues/6#issuecomment-1471303336)的第一步 download 步骤操作

修改 `cli_chatyuan.py` 里的 `LLM_MODEL="chatglm-6b"`

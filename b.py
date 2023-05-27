









# 使用 Markdown 格式打印模型输出
from IPython.display import display, Markdown, clear_output

def display_answer(agent, query, vs_path, history=[]):
    for resp, history in local_doc_qa.get_knowledge_based_answer(query=query,
                                                                 vs_path=vs_path,
                                                                 chat_history=history,
                                                                 streaming=False):
        clear_output(wait=True)
        #display(Markdown(resp["result"]))
    return resp, history




import torch.cuda
import torch.backends

from configs import model_config

# 全局参数，修改后请重新初始化
model_config.embedding_model_dict = {
    "ernie-tiny": "nghuyong/ernie-3.0-nano-zh",
    "ernie-base": "nghuyong/ernie-3.0-base-zh",
    "text2vec-base": "../text2vec-base-chinese",
    "text2vec": "../text2vec-large-chinese",
}
model_config.llm_model_dict = {
    "chatyuan1": "../chatYuan/ChatYuan-large-v1",
    "chatyuan2": "../chatYuan/ChatYuan-large-v2",
    "chatglm-6b-int4-qe": "../chatglm-6b-int4-qe",
    "chatglm-6b-int4": "../chatglm-6b-int4",
    "chatglm-6b-int8": "../chatglm-6b-int8",
    "chatglm-6b": "../chatglm",
}
model_config.VS_ROOT_PATH = "/Users/hfy/nltk_data/"

from chains.local_doc_qa import LocalDocQA

EMBEDDING_MODEL = "text2vec-base" # embedding 模型，对应 embedding_model_dict
VECTOR_SEARCH_TOP_K = 6
LLM_MODEL = "chatglm-6b"     # LLM 模型名，对应 llm_model_dict
LLM_HISTORY_LEN = 3
DEVICE = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"
DEVICE = "mps"

local_doc_qa = LocalDocQA()

local_doc_qa.init_cfg(llm_model=LLM_MODEL,
                          embedding_model=EMBEDDING_MODEL,
                          llm_history_len=LLM_HISTORY_LEN,
                          top_k=VECTOR_SEARCH_TOP_K)



vs_path, _ = local_doc_qa.init_knowledge_vector_store("/Users/hfy/jayli/ai/local_content.txt")


# 测试未进行本地知识库接入时的结果
# for resp, history in local_doc_qa.llm._call("chatglm-6b 的局限性具体体现在哪里，如何实现改进"):
#     clear_output(wait=True)
#     display(Markdown(resp))

print("向量生成完成", vs_path)

history = []
print('问问题...')
result, history  = display_answer(local_doc_qa, query="你是谁，来自哪里?", vs_path=vs_path, history=history)
print(result["result"])
print('问问题...')
result, history  = display_answer(local_doc_qa, query="酒店算法盘货是怎么做的?", vs_path=vs_path, history=history)
print(result["result"])
print('问问题...')
result, history  = display_answer(local_doc_qa, query="火星好玩吗?", vs_path=vs_path, history=history)
print(result["result"])

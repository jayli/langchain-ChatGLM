#coding = utf-8
from IPython.display import display, Markdown, clear_output
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
    "chatyuan": "ClueAI/ChatYuan-large-v2",
    "chatglm-6b-int4-qe": "../chatglm-6b-int4-qe",
    "chatglm-6b-int4": "../chatglm-6b-int4",
    "chatglm-6b-int8": "../chatglm-6b-int8",
    "chatglm-6b": "../chatglm",
}

from chains.local_doc_qa import LocalDocQA

# 修改为你本机 nltk 目录
model_config.VS_ROOT_PATH = "/Users/hfy/nltk_data/"

EMBEDDING_MODEL = "text2vec-base" # embedding 模型，对应 embedding_model_dict
VECTOR_SEARCH_TOP_K = 6
LLM_MODEL = "chatyuan"     # LLM 模型名，对应 llm_model_dict
LLM_HISTORY_LEN = 5
HISTORY = []
DEVICE = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"

local_doc_qa = LocalDocQA()

local_doc_qa.init_cfg(llm_model=LLM_MODEL,
                          embedding_model=EMBEDDING_MODEL,
                          llm_history_len=LLM_HISTORY_LEN,
                          top_k=VECTOR_SEARCH_TOP_K)

# 你的本地知识库
vs_path, _ = local_doc_qa.init_knowledge_vector_store("/Users/hfy/jayli/ai/local_content.txt")

def display_answer(agent, query, vs_path, history=[]):
    for resp, history in local_doc_qa.get_knowledge_based_answer(query=query,
                                                                 vs_path=vs_path,
                                                                 chat_history=history,
                                                                 streaming=False):
        clear_output(wait=True)
    return resp, history

def history_cut(arr):
    global LLM_HISTORY_LEN
    if len(arr) <= LLM_HISTORY_LEN:
        return arr
    else:
        return arr[1:]

def answer(query = "", history = []):
    global local_doc_qa, HISTORY, vs_path
    result, HISTORY = display_answer(local_doc_qa,
                                     query=query,
                                     vs_path=vs_path,
                                     history=history_cut(HISTORY))
    return result["result"]

if __name__ == "__main__":
    value = input("问题1:")
    print(answer(value))
    value = input("问题2:")
    print(answer(value))
    value = input("问题3:")
    print(answer(value))

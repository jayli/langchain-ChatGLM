#coding = utf-8
from IPython.display import display, Markdown, clear_output
import torch.cuda
import torch.backends
import os
from configs import model_config
from chains.local_doc_qa import LocalDocQA

EMBEDDING_MODEL = "text2vec" # embedding 模型，对应 embedding_model_dict
VECTOR_SEARCH_TOP_K = 6
LLM_MODEL = "chatyuan"       # LLM 模型名，对应 llm_model_dict
LLM_HISTORY_LEN = 3
HISTORY = []

local_doc_qa = LocalDocQA()
local_path = os.path.dirname(__file__)
local_doc_qa.init_cfg(llm_model=LLM_MODEL,
                          embedding_model=EMBEDDING_MODEL,
                          llm_history_len=LLM_HISTORY_LEN,
                          top_k=VECTOR_SEARCH_TOP_K)

# 你的本地知识库
vs_path, _ = local_doc_qa.init_knowledge_vector_store(os.path.join(local_path,"local_content.txt"))

def display_answer(agent, query, vs_path, history=[]):
    content = ""
    last_print_len = 0
    for resp, history in local_doc_qa.get_knowledge_based_answer(query=query,
                                                                 vs_path=vs_path,
                                                                 chat_history=history,
                                                                 streaming=False):
        content = content + resp["result"]
    return content , history

def history_cut(arr):
    global LLM_HISTORY_LEN
    if len(arr) <= LLM_HISTORY_LEN:
        return arr
    else:
        return arr[1:]

def answer(query = "", history = []):
    global HISTORY
    result, HISTORY = display_answer(local_doc_qa,
                                     query=query,
                                     vs_path=vs_path,
                                     history=history_cut(HISTORY))
    return result

if __name__ == "__main__":
    while True:
        query = input("Input your question：")
        print(answer(query))




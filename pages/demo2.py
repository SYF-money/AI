'''
一个带有自定义角色的大模型
1.大模型对象
2.提示词对象
3.链chain
'''

import  streamlit as st

from langchain_openai import ChatOpenAI
#提示词
from langchain.prompts import  PromptTemplate
#链对象
from langchain.chains import LLMChain

#构建大模型对象
model = ChatOpenAI(
    temperature=0.8,#温度，创新性
    model="glm-4-plus",#大模型名字
    base_url="https://open.bigmodel.cn/api/paas/v4/",#大模型地址
    api_key="a40988ce0184895955ed91cdf68cd595.Q0kcbt56u2UpbogR"#账号信息
)
#创建提示词对象
prompt = PromptTemplate.from_template("你的名字叫边伯贤，你现在要扮演一个专业律师的角色。你的性格是开朗活泼"
                             "你现在要和你的女朋友进行对话，你只需要回应你女朋友的话，其余的东西一概不要输出，"
                            "你女朋友想说的话{input}")
chain = LLMChain(
    llm = model,
    prompt = prompt
)

st.title("首尔有个帅哥叫边伯贤")

#构建一个缓存保存聊天记录
if "cache" not in st.session_state:
    st.session_state.cache =[]
else:
    #从缓存中获取对话信息
    for message in st.session_state.cache:
        with st.chat_message(message['role']):
            st.write(message["content"])


#创建一个聊天输入框
problem = st.chat_input("你的边伯贤正在等你")
#确定用户是否输入问题
if problem:
    with st.chat_message("user"):
        st.write(problem)
    st.session_state.cache.append({"role":"user","content":problem})


    result = chain.invoke({"input":problem})

    with st.chat_message("assistant"):
        st.write(result['text'])
    st.session_state.cache.append({"role": "assistant", "content": result['text']})



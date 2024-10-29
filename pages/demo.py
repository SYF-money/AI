
import  streamlit as st

from langchain_openai import  ChatOpenAI

#构建大模型
model = ChatOpenAI(
    temperature=0.8,#温度，创新性
    model="glm-4-plus",#大模型名字
    base_url="https://open.bigmodel.cn/api/paas/v4/",#大模型地址
    api_key="a40988ce0184895955ed91cdf68cd595.Q0kcbt56u2UpbogR"#账号信息
)

st.title("AI demo小程序")
#创建一个聊天输入框
problem = st.chat_input("请输入你的问题")
#确定用户是否输入问题
if problem:
    with st.chat_message("user"):
        st.write(problem)

    result = model.invoke(problem)

    with st.chat_message("assistant"):
        st.write(result.content)



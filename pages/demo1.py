
import  streamlit as st

from langchain_openai import  ChatOpenAI



#构建大模型
model = ChatOpenAI(
    temperature=0.8,#温度，创新性
    model="glm-4-plus",#大模型名字
    base_url="https://open.bigmodel.cn/api/paas/v4/",#大模型地址
    api_key="a40988ce0184895955ed91cdf68cd595.Q0kcbt56u2UpbogR"#账号信息
)

st.title("AI 小施")

#构建一个缓存保存聊天记录
if "cache" not in st.session_state:
    st.session_state.cache =[]
else:
    #从缓存中获取对话信息
    for message in st.session_state.cache:
        with st.chat_message(message['role']):
            st.write(message["content"])


#创建一个聊天输入框
problem = st.chat_input("请输入你的问题")
#确定用户是否输入问题
if problem:
    with st.chat_message("user"):
        st.write(problem)
    st.session_state.cache.append({"role":"user","content":problem})


    result = model.invoke(problem)

    with st.chat_message("assistant"):
        st.write(result.content)
    st.session_state.cache.append({"role": "assistant", "content": problem})



import streamlit as st
from zhipuai import ZhipuAI


model = ZhipuAI(api_key="a40988ce0184895955ed91cdf68cd595.Q0kcbt56u2UpbogR")

st.title("设计")

if "cache1" not in st.session_state:
    st.session_state.cache1 = []
else:
    for message in st.session_state.cache1:
        if message['role'] == 'user':
            with st.chat_message(message['role']):
                st.write(message["content"])
        else:
            with st.chat_message(message['role']):
                st.image(message["content"], width=400)

desc = st.chat_input("请输入图片的描写")
if desc:
    with st.chat_message("user"):
        st.write(desc)
        st.session_state.cache1.append(({"role": "user", "content": desc}))

    response = model.images.generations(
        model="cogview-3-plus",  # 填写需要调用的模型编码
        prompt=desc
    )
    with st.chat_message("assistant"):
        st.image(response.data[0].url,width=300)
    st.session_state.cache1.append(({"role": "assistant", "content": response.data[0].url}))

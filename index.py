import streamlit as st

st.title("AI大模型应用产品网")
col,col1 = st.columns(2)
with col:
    st.image('https://img2.baidu.com/it/u=1713709234,2737477617&fm=253&fmt=auto&app=138&f=JPEG?w=800&h=800',width=300)
    flag = st.button("施施",use_container_width=True)
    if flag:
        st.switch_page("pages/demo3.py")

with col1:
    st.image('https://img1.baidu.com/it/u=3539579830,3023993468&fm=253&fmt=auto&app=138&f=JPEG?w=800&h=800', width=300)
    flag1 = st.button("怂怂",use_container_width=True)
    if flag1:
        st.switch_page("pages/textToimage.py")


# c1,c2,c3,c4,c5 = st.columns(5)
#
# with c1:
#     flag = st.button("基础版")
#     if flag:
#         st.switch_page("pages/demo.py")
#
# with c2:
#     flag1 = st.button("进阶版1")
#     if flag1:
#         st.switch_page("pages/demo1.py")
#
# with c3:
#     flag2 = st.button("进阶版2")
#     if flag2:
#         st.switch_page("pages/demo2.py")
#
# with c4:
#     flag3 = st.button("最终版")
#     if flag3:
#         st.switch_page("pages/demo3.py")
#
# with c5:
#     flag4 = st.button("文生图")
#     if flag4:
#         st.switch_page("pages/textToimage.py")


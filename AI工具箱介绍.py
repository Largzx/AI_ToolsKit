import streamlit as st

st.title("💼AI工具箱")

st.write("💡欢迎使用AI工具箱！请选择左侧边栏的模块开始使用。")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("#### 💭Deepseek对话系统")

with col2:
    st.markdown("#### 📑PDF问答工具")

with col3:
    st.markdown("#### 🧾脱口秀文稿生成器")

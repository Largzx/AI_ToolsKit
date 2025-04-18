import os

import streamlit as st
from langchain.memory import ConversationBufferMemory
from utils.utils_1 import Creat_model


def clear_all():
    st.session_state.clear()


def set_temperature(tp):
    if tp == "更精准":
        return 0.0
    elif tp == "通用对话":
        return 1.3
    elif tp == "更多样":
        return 1.5


st.title("✨通用聊天机器人")
with st.sidebar:
    api_way = st.radio(
        label="是否获取本地API环境变量",
        options=('是', '否'),
        index=1,
        format_func=str,
    )
    if api_way == '是':
        open_api_key = os.getenv("OPEN_API_KEY")
    else:
        open_api_key = st.text_input("请输入API密钥", type='password')

    st.markdown("[获取deepseek-API密钥](https://platform.deepseek.com/)")
    st.markdown("---")
    model_kind = st.selectbox("V3 | R1(深度思考)",
                              ["deepseek-chat", "deepseek-reasoner"],
                              index=0,
                              help="deepseek-chat是普通版本；deepseek-reasoner为推理R1")

    tp = st.radio(label="设置对话多样性：",
                  options=("更精准", "通用对话", "更多样"),
                  index=1,
                  format_func=str,
                  help='更精准会更加严谨，比如在做计算题；更多样对话更具有创意')

    temperature = set_temperature(tp)
    st.write("---")
    st.button("清空上下文开启新对话", on_click=clear_all)

if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
    st.session_state["messages"] = [{"role": "ai",
                                     "content": "我是一个聊天机器人，有疑问尽管找我😁"}]

for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input("")

if prompt:
    if api_way == '否' and not open_api_key:
        st.info("🔑请输入密钥！！")
        st.stop()
    st.session_state["messages"].append({"role": "human", "content": prompt})
    st.chat_message("human").write(prompt)

    model = Creat_model(memory=st.session_state["memory"],
                        model=model_kind,
                        openai_api_key=open_api_key,
                        temperature=temperature)
    with st.spinner("AI正在思考，请稍后....."):
            response_text = model.get_chat_response(prompt)

    msg = {"role": "ai", "content": response_text}
    st.session_state["messages"].append(msg)
    st.chat_message("ai").write(response_text)


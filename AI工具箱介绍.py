import streamlit as st

st.title("💼AI工具箱")

st.write("💡欢迎使用AI工具箱！请选择左侧边栏的模块开始使用。")

with st.sidebar:
    st.markdown("✨点击即刻使用")
    st.markdown(
        '''
        -  👨‍🦳***我的主页***
        
        [![GitHub](https://img.shields.io/badge/GitHub-FFFFFF?style=for-the-badge&logo=github&logoColor=black)](https://github.com/Largzx) 
        [![CSDN](https://img.shields.io/badge/CSDN-FFFFFF?style=for-the-badge&logo=csdn&logoColor=black)](https://blog.csdn.net/m0_63488477?spm=1011.2124.3001.5343)
        '''
    )


col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("##### 💭Deepseek对话系统")
    st.markdown(
        '''
        ---
        - 输入API进行**上下文对话**(密钥不会被保存)
         
        - 推理和通用模型可选 **（V3 or R1）**
        
        - **三种多样性**设置
         
        - 支持**清空当前上下文**对话开启新对话
        ''')

with col2:
    st.markdown("##### 📑PDF问答工具")
    st.markdown(
        '''
        ---
        - 上传PDF文档，**自动构建**向量数据库
        
        - 询问**PDF相关问题**给予回复
        
        - 可选（ qwen-max/plus/turbo ）模型
        '''
    )
with col3:
    st.markdown("##### 🧾脱口秀文稿生成器")
    st.markdown(
        '''
        ---
        - 输入自己deepseek的API密钥
        
        - 可以选择deepseek的**不同模型**
        
        - 输入稿子的话题
        
        - 选择**演讲时长**以及模型**温度参数**（即文本是否更加多样性）
        '''
    )


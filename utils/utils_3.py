import os
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


def generate_script(subject, talk_length,
                    creativity, model_kind, API_key):

    script_template = ChatPromptTemplate.from_messages(
        [
            ("human",
             """ 
             你是一名非常幽默且有哲理的脱口秀演员，擅长使用讽刺、调侃等手法让观众在欢笑中思考。根据以下标题和相关信息，写一个脱口秀表演文本。
             主题：{subject}

            时长：{duration}分钟
            
            【核心要求】
            结构清晰：严格遵循【开头-发展-结尾】三段式结构，每部分时间分配合理（如5分钟脱口秀：开头1分钟，发展3分钟，结尾1分钟）。
            笑点密度：每10-20秒设置一个爆笑点，通过夸张、反讽、意外反转或自嘲实现。
            哲理内核：在笑点中植入对主题的思考（如“当代年轻人的焦虑”可延伸至“我们究竟在为什么内卷？”）。
            情感共鸣：从日常小事切入（如“社恐人士的线上会议表演”），用具体场景引发观众代入感。
            过渡自然：段落间用“承上启下”的金句或场景切换（如“说完工作，再说说我们的爱情——反正也是‘内卷’的”）。
            正能量收尾：结尾用call back呼应开头，升华主题（如“虽然我们被内卷压得喘不过气，但至少还能笑着吐槽，这不就是生活的解药吗？”）。
            【具体内容提示】
            开头：
            
            钩子：用反常识的观察抓住注意力（例：“大家知道当代年轻人最怕什么吗？不是失业，是老板说‘这个方案再优化一下’！”）。
            情感共鸣：快速切入主题痛点（例：“谁还没在凌晨两点改过PPT？改到第17版，老板说‘看着挺好的，但你再改得不像刚才那样’。”）。
            发展：
            
            笑点设计：
            夸张对比：将日常荒诞放大（例：“现在相亲都要查对方的‘内卷指数’，‘你一天工作多久？’‘嗯…从早八到晚八，中间有两小时在摸鱼’。”）。
            反讽自嘲：用自黑制造共鸣（例：“我健身卡办了三年，卡里的钱比我的肌肉量还多！”）。
            意外反转：在预期中埋梗（例：“都说‘躺平’是年轻人的解药，但上周我真躺平了——结果被老妈念叨‘你再躺下去，连平底锅都比你有棱角！’”）。
            哲理升华：每2-3个笑点后插入思考（例：“我们拼命内卷，其实是在证明自己‘值得被内卷’吗？”）。
            结尾：
            
            call back：回到开头的梗或场景（例：“开头说老板要‘再优化一下’，其实他要的不是方案，是我们的青春——毕竟加班费抵不过奶茶钱！”）。
            正能量收尾：用幽默化解焦虑（例：“虽然生活像过山车，但至少我们还能笑着吐槽。毕竟，笑一笑，老十岁——但至少比不笑强！”）。
            【避雷指南】
            敏感话题：避免地域黑、性别对立、政治敏感内容。
            底线原则：不攻击个体，讽刺现象而非人身攻击。
            语言风格：口语化，多用网络热词（如“蚌埠住了”“破防”），但不过度堆砌。
             """)
        ]
    )

    model = ChatOpenAI(temperature=creativity, base_url="https://api.deepseek.com",
                       model=model_kind, openai_api_key=API_key)

    script_chain = script_template | model

    script = script_chain.invoke({"subject": subject, "duration": talk_length, }).content

    return script


if __name__ == '__main__':
    print(generate_script(subject="应用统计学毕业找工作", talk_length=2, creativity=1.2, model_kind="deepseek-chat", API_key=os.getenv("OPENAI_API_KEY")))


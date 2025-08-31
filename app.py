from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from openai import OpenAI
import os

load_dotenv()

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)


import streamlit as st

st.title("streamlitテストアプリリ②: LangChainを使った少し複雑なWebアプリ")

st.write("##### 動作モード1: 健康に関する質問")
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことで文字数をカウントできます。")
st.write("##### 動作モード2: 宇宙に関する質問")
st.write("身長と体重を入力することで、肥満度を表す体型指数のBMI値を算出できます。")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["健康に関すること", "宇宙に関すること"]
)

st.divider()

if selected_item == "健康に関すること":
    input_message = st.text_input(label="質問のテキストを入力してください。")
else:
    input_message = st.text_input(label="質問のテキストを入力してください。")

if st.button("実行"):
    st.divider()

    if selected_item == "健康に関すること":
        if input_message:
            st.write("##### 入力内容")
            st.write(input_message)
            # LangChainの処理をここに追加
            # 健康に関する専門家としてLLMに質問する
            response = "健康に関する質問に対する回答"
            st.write("##### LLMの回答")
            st.write(response)
            messages = [

                SystemMessage(content="あなたは健康に関する専門家です。"),
                HumanMessage(content=input_message),
            ]

    else:
        if input_message:
            st.write("##### 入力内容")
            st.write(input_message)
            # LangChainの処理をここに追加
            # 宇宙に関する専門家としてLLMに質問する
            messages = [
            SystemMessage(content="あなたは宇宙に関する専門家です。"),
            HumanMessage(content=input_message),
        ]


    result = llm(messages)
    st.write(result.content)


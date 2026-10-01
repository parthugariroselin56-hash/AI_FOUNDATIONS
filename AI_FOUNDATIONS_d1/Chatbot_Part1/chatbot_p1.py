from ollama import chat
import streamlit as st

st.set_page_config(page_title="ALEXA", page_icon="💀")
st.title("💀ALEXA-Here to talk!")
st.markdown("""
<style>
.stApp{
background-color:#C9C0BB
}
</style>
""",unsafe_allow_html=True)

personlity="You are a friendly and patient tutor.Keep the answers short.Answer within one sentence."

personality_2="You are a funny and quirky theif,Answer with in one sentences"

if "history" not in st.session_state:
    st.session_state.history=[{"role":"system","content":personlity}]
with st.sidebar:
    st.header("Chat Controls")
    if st.button("Clear chat",type="primary"):
        st.session_state.history=[{"role":"system","content":personlity}]
        st.rerun()

    if st.button("Change personality"):
        st.session_state.history=[{"role":"system","content":personality_2}]
        st.rerun()

with st.chat_message("assistant"):
    st.write("Hello, I'm demon! Ask something to get started.")

for msg in st.session_state.history[1:]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

question=st.chat_input("Type something......")
st.session_state.history.append({"role":"user","content":question})
if question:
    with st.chat_message("user"):
        st.write(question)
    try:
        with st.spinner("🤔🤔"):
            response=chat(model="llama3.2",messages=st.session_state.history)
        reply=response["message"]["content"]
        st.session_state.history.append({"role":"assistent","content":reply})

        with st.chat_message("assistant"):
            st.write(reply)
    except Exception as e:
        st.write("Unknown error.Is ollama running?")
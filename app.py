import streamlit as st
from langchain.prompts import PromptTemplate
from ctransformers import AutoModelForCausalLM

st.set_page_config(page_title='Blog Generation',layout='centered')

st.title('Blog Generator')

def generate_output(topic,no_of_words,target):
    llm = AutoModelForCausalLM.from_pretrained(model_path_or_repo_id = "model/llama-2-7b-chat.ggmlv3.q8_0.bin",
                        model_type = 'llama')
    
    template = "Write a blog on {topic} for {target} within {no_of_words} words."  

    prompt = PromptTemplate(input_variables=['topic','no_of_words','target'],template=template)

    response = llm(prompt.format(topic = topic, no_of_words = no_of_words,target = target))
    return response

topic = st.text_input("Enter topic")
col1,col2 = st.columns((5,5))
with col1:
    no_of_words = st.text_input("No of words of output")
with col2:
    target = st.selectbox('Who is this for?',('Researcher','Data Scientist','Common Person'),placeholder='Choose an option',index = None)

if st.button('Generate'):
    st.write(generate_output(topic,no_of_words,target))
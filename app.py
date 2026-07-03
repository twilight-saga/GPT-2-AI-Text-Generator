import streamlit as st
from transformers import pipeline
generator = pipeline('text-generation', model='gpt2')
st.title("GPT-2 AI Text Generator")
st.write("Generate coherent and contextually relevant text using the GPT-2.")
prompt = st.text_area("Enter your prompt:", placeholder="Example: Artificial Intelligence is.....")
max_length = st.slider("Maximum Length", min_value=20, max_value=200, value=50)
temperature = st.slider("Temperature", min_value=0.1, max_value=2.0, value=0.1, step=0.1)
if st.button("Generate Text"):
    if prompt: 
        results = generator(prompt, max_length=max_length, temperature=temperature, do_sample=True, num_return_sequences=1)
    else:
        st.warning("Please enter a prompt to generate text.")    
    st.subheader("Generated Text:")
    st.write(results[0]['generated_text'])
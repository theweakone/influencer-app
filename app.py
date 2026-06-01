import streamlit as st
import replicate
import os

st.title("AI Influencer Stüdyosu")

# API Anahtarı için kutucuk (bunu github secrets ile uğraşmamak için direkt ekrana koyduk)
api_key = st.text_input("Replicate API Anahtarını Gir:", type="password")
os.environ["REPLICATE_API_TOKEN"] = api_key

uploaded_file = st.file_uploader("Bir fotoğraf yükle", type=["jpg", "png"])
prompt = st.text_input("Ne yapsın? (Örn: Paris'te kahve içiyor)", "A realistic person, natural skin, 8k")

if st.button("Üret"):
    if api_key and uploaded_file:
        st.write("Üretiliyor, lütfen bekle...")
        output = replicate.run(
            "zsxkib/instantid-flux:latest",
            input={"image": uploaded_file, "prompt": prompt}
        )
        st.image(output)
    else:
        st.error("API anahtarını ve fotoğrafı eklediğinden emin ol!")

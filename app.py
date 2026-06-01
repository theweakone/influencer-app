import streamlit as st
import replicate
import os

st.title("AI Influencer Stüdyosu")

# API Anahtarı girişi
api_key = st.text_input("Replicate API Anahtarını Gir:", type="password")
if api_key:
    os.environ["REPLICATE_API_TOKEN"] = api_key

uploaded_file = st.file_uploader("Bir fotoğraf yükle", type=["jpg", "png"])
prompt = st.text_input("Ne yapsın?", "A realistic photo of a person in a sunny street, natural skin, 8k")

if st.button("Üret"):
    if api_key and uploaded_file:
        try:
            st.write("Üretiliyor, lütfen bekle...")
            
            # Herkesin erişebildiği stabil model
            output = replicate.run(
                "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
                input={
                    "prompt": prompt,
                    "num_output": 1,
                    "aspect_ratio": "9:16",
                    "output_format": "webp"
                }
            )
            st.image(output[0])
        except Exception as e:
            st.error(f"Hata: {str(e)}")
    else:
        st.error("API anahtarını gir ve fotoğraf yükle!")

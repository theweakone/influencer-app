import streamlit as st
import replicate
import os

st.title("AI Influencer Stüdyosu")

# API Anahtarı girişi
api_key = st.text_input("Replicate API Anahtarını Gir:", type="password")
if api_key:
    os.environ["REPLICATE_API_TOKEN"] = api_key

uploaded_file = st.file_uploader("Bir fotoğraf yükle", type=["jpg", "png"])
prompt = st.text_input("Ne yapsın?", "A realistic photo of the person, walking in a sunny street, casual outfit, natural skin texture, 8k")

if st.button("Üret"):
    if api_key and uploaded_file:
        try:
            st.write("Üretiliyor, lütfen bekle...")
            
            # InstantID için en güncel ve stabil model adresi
            output = replicate.run(
                "adirik/instantid:e809311e97588e3678087799d55a5b57f12e84c568f188981f9f59516634c4d5",
                input={
                    "image": uploaded_file, 
                    "prompt": prompt,
                    "controlnet_weight": 1.0,
                    "ip_adapter_weight": 0.8
                }
            )
            st.image(output)
        except Exception as e:
            st.error(f"Hata: {str(e)}")
    else:
        st.error("Lütfen API anahtarını gir ve bir fotoğraf yükle!")

import streamlit as st
import replicate
import os

st.title("AI Influencer Stüdyosu")

api_key = st.text_input("Replicate API Anahtarını Gir:", type="password")
if api_key:
    os.environ["REPLICATE_API_TOKEN"] = api_key

uploaded_file = st.file_uploader("Bir fotoğraf yükle", type=["jpg", "png"])
prompt = st.text_input("Ne yapsın?", "A realistic photo of the person, walking in a sunny street, casual outfit, natural skin texture, 8k")

if st.button("Üret"):
    if api_key and uploaded_file:
        try:
            st.write("Üretiliyor, lütfen bekle...")
            
            # Burada dosyayı geçici olarak kaydedip Replicate'e veriyoruz
            output = replicate.run(
                "zsxkib/instantid-flux:latest",
                input={
                    "image": uploaded_file, 
                    "prompt": prompt,
                    "controlnet_weight": 1.0,
                    "ip_adapter_weight": 0.8
                }
            )
            st.image(output)
        except Exception as e:
            st.error(f"Bir hata oluştu: {str(e)}")
    else:
        st.error("Lütfen API anahtarını gir ve bir fotoğraf yükle!")

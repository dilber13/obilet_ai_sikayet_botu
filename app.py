import streamlit as st
from kategorilendirici import kategori_tahmin_et
from yanit_uretici import yanit_uret

st.set_page_config(page_title="Şikayet İşleme Botu", layout="centered")

st.title("🧠 Obilet AI Şikayet Yardımcısı")
st.write("Aşağıya müşteri şikayetini girin. Sistem otomatik olarak kategorisini tahmin eder ve yanıt üretir.")

# Giriş alanı
sikayet = st.text_area("✍️ Şikayet mesajını giriniz:")

if st.button("📤 Gönder"):
    if sikayet.strip() == "":
        st.warning("Lütfen bir şikayet metni giriniz.")
    else:
        with st.spinner("Kategori tahmin ediliyor..."):
            kategori = kategori_tahmin_et(sikayet)
        with st.spinner("Yanıt hazırlanıyor..."):
            yanit = yanit_uret(sikayet)

        st.success("✅ İşlem Tamamlandı")

        st.subheader("📂 Tahmin Edilen Kategori")
        st.code(kategori, language="bash")

        st.subheader("🤖 Otomatik Yanıt")
        st.write(yanit)

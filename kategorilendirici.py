import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# 🔹 Veri Yükle
with open("data/sikayet_verileri.json", "r", encoding="utf-8") as f:
    veriler = json.load(f)

df = pd.DataFrame(veriler)

# 🔹 Eğitim
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["mesaj"])
y = df["kategori"]

model = MultinomialNB()
model.fit(X, y)

# 🔹 Tahmin Fonksiyonu
def kategori_tahmin_et(mesaj: str):
    X_new = vectorizer.transform([mesaj])
    tahmin = model.predict(X_new)[0]
    return tahmin

# 🔹 Örnek test
if __name__ == "__main__":
    test_mesaj = "Paramı geri almak istiyorum, uygulama hata verdi."
    kategori = kategori_tahmin_et(test_mesaj)
    print(f"Tahmin edilen kategori: {kategori}")

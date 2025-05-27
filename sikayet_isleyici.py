from kategorilendirici import kategori_tahmin_et
from yanit_uretici import yanit_uret

def ana_sistem(mesaj: str):
    print("📩 Gelen Şikayet:")
    print(mesaj)

    kategori = kategori_tahmin_et(mesaj)
    print(f"\n🔍 Tahmin Edilen Kategori: {kategori}")

    yanit = yanit_uret(mesaj)
    print(f"\n🤖 Otomatik Yanıt:\n{yanit}")

# Örnek test
if __name__ == "__main__":
    ornek_sikayet = "Kredi kartımdan para çekildi ama bilet gelmedi."
    ana_sistem(ornek_sikayet)

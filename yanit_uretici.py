import openai
import os
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Yeni istemci tanımı
client = openai.OpenAI()

# Otomatik yanıt üretme fonksiyonu
def yanit_uret(sikayet: str) -> str:
    prompt = f"""
Aşağıdaki müşteri şikayetini profesyonel, empatik ve çözüm odaklı bir şekilde yanıtla.
Şikayet: "{sikayet}"
Yanıt:
"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=512,
        temperature=0.7
    )
    return response.choices[0].message.content.strip()

# Örnek test
if __name__ == "__main__":
    test_sikayet = "Otobüs rötar yaptı ama bilgilendirme almadım."
    yanit = yanit_uret(test_sikayet)
    print("Otomatik Yanıt:")
    print(yanit)

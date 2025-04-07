import json
from crypto_util import xor_decrypt_with_salt

def run_quiz(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)

    for idx, soal in enumerate(data, start=1):
        print(f"\n🧠 Soal #{idx}: {soal['question']}")
        for k, v in soal['choices'].items():
            print(f"   {k}) {v}")

        user_ans = input("Jawaban Anda [a-e]: ").strip().lower()
        correct_ans = xor_decrypt_with_salt(soal['answer'])

        if user_ans == correct_ans:
            print("✅ Benar!")
        else:
            print(f"❌ Salah. Jawaban benar: {correct_ans}")
            print(f"🧾 Penjelasan: {soal['explanation']}")

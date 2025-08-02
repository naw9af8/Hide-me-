# Made by naw9af8 (Nawaf Altalhi) v1.0
# صنع بواسطة نواف الطلحي
# This code is a simple encryption/decryption tool that supports both English and Arabic languages.
import os

CONFIG_FILE = "language_config.txt"

def load_language():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                lang = f.read().strip()
                if lang in ['ar', 'en']:
                    return lang
        except:
            pass
    return None

def save_language(lang):
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        f.write(lang)

def get_language():
    lang = load_language()
    if lang:
        return lang
        
    print("\nChoose language / اختر اللغة:")
    print("1. English")
    print("2. العربية")
    choice = input("Enter choice (1/2): ")
    
    if choice == '1':
        lang = 'en'
    elif choice == '2':
        lang = 'ar'
    else:
        print("Invalid choice, using English")
        lang = 'en'
    
    save_language(lang)
    return lang

def encrypt(text, shift, lang):
    result = ""
    arabic_letters = "ابتثجحخدذرزسشصضطظعغفقكلمنهوي"
    
    for char in text:
        if lang == 'en' and char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - base + shift) % 26 + base)
        elif lang == 'ar' and char in arabic_letters:
            idx = (arabic_letters.index(char) + shift) % len(arabic_letters)
            result += arabic_letters[idx]
        else:
            result += char
    return result

def decrypt(text, shift, lang):
    return encrypt(text, -shift, lang)

def main():
    lang = get_language()
    
    # UI Translations
    translations = {
        'menu': {
            'en': "\n1. Encrypt text\n2. Decrypt text",
            'ar': "\n1. تشفير النص\n2. فك تشفير النص"
        },
        'choice_prompt': {
            'en': "Choose action (1/2): ",
            'ar': "اختر الإجراء (1/2): "
        },
        'invalid_choice': {
            'en': "Invalid choice!",
            'ar': "اختيار غير صحيح!"
        },
        'text_prompt': {
            'en': "Enter text: ",
            'ar': "أدخل النص: "
        },
        'shift_prompt': {
            'en': "Enter encryption key (integer): ",
            'ar': "أدخل مفتاح التشفير (عدد صحيح): "
        },
        'encrypted_result': {
            'en': "\nEncrypted text: ",
            'ar': "\nالنص المشفر: "
        },
        'decrypted_result': {
            'en': "\nDecrypted text: ",
            'ar': "\nالنص الأصلي: "
        },
        'invalid_shift': {
            'en': "Key must be an integer!",
            'ar': "المفتاح يجب أن يكون عدداً صحيحاً!"
        },
        'continue_prompt': {
            'en': "\nDo you want to perform another operation? (y/n): ",
            'ar': "\nهل تريد إجراء عملية أخرى؟ (y/n): "
        },
        'another_operation': {
            'en': "\nStarting a new operation...",
            'ar': "\nبدء عملية جديدة..."
        },
        'goodbye': {
            'en': "\nGoodbye!",
            'ar': "\nمع السلامة!"
        }
    }

    while True:
        # Display menu
        print(translations['menu'][lang])
        choice = input(translations['choice_prompt'][lang])
        
        if choice not in ['1', '2']:
            print(translations['invalid_choice'][lang])
            continue
        
        text = input(translations['text_prompt'][lang])
        
        try:
            shift = int(input(translations['shift_prompt'][lang]))
        except ValueError:
            print(translations['invalid_shift'][lang])
            continue

        if choice == '1':
            result = encrypt(text, shift, lang)
            print(translations['encrypted_result'][lang] + result)
        else:
            result = decrypt(text, shift, lang)
            print(translations['decrypted_result'][lang] + result)
        
        # Ask if user wants to continue
        cont = input(translations['continue_prompt'][lang]).strip().lower()
        if lang == 'ar':
            cont = 'ن' if cont == 'n' else 'y' if cont == 'y' else cont
        if cont in ['n', 'لا', 'no']:
            print(translations['goodbye'][lang])
            break
        else:
            print(translations['another_operation'][lang])

if __name__ == "__main__":
    main()

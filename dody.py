import ctypes
import time

ctypes.windll.user32.MessageBoxW(
    0,
    "Поздравляю! 😂\n\nЯ знаю все твои пароли! 🤣",
    "Сюрприз! 🎉",
    0x40
)

time.sleep(1)

ctypes.windll.user32.MessageBoxW(
    0,
    "Шутка! 😄\n\nНе бойся, это просто прикол! 🎭",
    "Шутка! 😜",
    0x30
)

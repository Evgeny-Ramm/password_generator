#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Модуль для работы со случайными числами и выбором случайного элемента
import secrets
# Модуль, содержащий наборы символов: буквы, цифры, знаки препинания
import string
# Модуль для разбора аргументов командной строки
import argparse

def generate_password(length=12, use_special=True):
    """
    Генерирует случайный пароль заданной длины.
    
    Аргументы:
        length (int): длина пароля (по умолчанию 12)
        use_special (bool): использовать ли специальные символы (по умолчанию True)
    
    Возвращает:
        str: сгенерированный пароль
    """
    # Если разрешены специальные символы, берём все буквы, цифры и знаки препинания
    if use_special:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        # Иначе только буквы и цифры (без знаков препинания)
        characters = string.ascii_letters + string.digits
    
    # Генерация пароля:
    # Для каждого из length раз выбираем случайный символ из строки characters
    # и склеиваем все символы в одну строку с помощью join
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def main():
    # Создаём парсер аргументов командной строки с описанием программы
    parser = argparse.ArgumentParser(description="Генератор случайных паролей")
    
    # Добавляем опцию для указания длины пароля:
    # -l или --length, ожидается целое число, по умолчанию 12
    parser.add_argument("-l", "--length", type=int, default=12,
                        help="Длина пароля (по умолчанию 12)")
    
    # Добавляем флаг для отключения специальных символов:
    # --no-special, если указан, то use_special становится False
    parser.add_argument("--no-special", action="store_true",
                        help="Не использовать специальные символы")
    
    # Разбираем аргументы командной строки
    args = parser.parse_args()
    
    # Генерируем пароль:
    # - длина берётся из args.length
    # - use_special = True, если флаг --no-special НЕ указан
    pwd = generate_password(args.length, use_special=not args.no_special)
    
    # Выводим результат на экран
    print(f"Сгенерированный пароль (длина {args.length}): {pwd}")

# Точка входа в программу: если файл запущен напрямую, а не импортирован как модуль,
# то вызываем функцию main()
if __name__ == "__main__":
    main()

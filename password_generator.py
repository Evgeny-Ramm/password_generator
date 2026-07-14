#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# password_generator.py
# Генератор паролей с цветным выводом, исключением похожих символов и оценкой стойкости.

import random
import string
import argparse
from colorama import init, Fore, Style

init(autoreset=True)

AMBIGUOUS = "1lI0O"

def generate_password(length=12, use_special=True, no_ambiguous=False):
    chars = string.ascii_letters + string.digits
    if use_special:
        chars += string.punctuation
    if no_ambiguous:
        chars = ''.join(c for c in chars if c not in AMBIGUOUS)
    return ''.join(random.choice(chars) for _ in range(length))

def check_strength(password):
    score = 0
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1

    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score >= 6:
        return f"{Fore.GREEN}strong{Style.RESET_ALL}"
    elif score >= 4:
        return f"{Fore.YELLOW}medium{Style.RESET_ALL}"
    else:
        return f"{Fore.RED}weak{Style.RESET_ALL}"

def main():
    parser = argparse.ArgumentParser(description="генератор паролей")
    parser.add_argument("-l", "--length", type=int, default=12, help="длина пароля")
    parser.add_argument("--no-special", action="store_true", help="без спецсимволов")
    parser.add_argument("--no-ambiguous", action="store_true", help="исключить похожие символы")
    args = parser.parse_args()

    password = generate_password(args.length, not args.no_special, args.no_ambiguous)
    strength = check_strength(password)

    print(f"{Fore.CYAN}Пароль:{Style.RESET_ALL} {password}")
    print(f"{Fore.CYAN}Стойкость:{Style.RESET_ALL} {strength}")

if __name__ == "__main__":
    main()

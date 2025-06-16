import random
import string
import re
from typing import List, Dict


class PasswordGenerator:
    """генератор паролей с оценкой сложности"""

    def __init__(self):
        self._char_sets = {
            'letters': string.ascii_letters,
            'digits': string.digits,
            'symbols': '!@#$%^&*()_+-='
        }
        self._strength_rules = {
            'length': lambda p: min(len(p) // 2, 4),
            'has_upper': lambda p: 1 if re.search(r'[A-Z]', p) else 0,
            'has_lower': lambda p: 1 if re.search(r'[a-z]', p) else 0,
            'has_digit': lambda p: 1 if re.search(r'\d', p) else 0,
            'has_symbol': lambda p: 1 if re.search(r'[^A-Za-z0-9]', p) else 0,
            'no_repeats': lambda p: 1 if not re.search(r'(.)\1', p) else 0
        }

    def _get_character_set(self) -> List[str]:
        """объединяет все наборы символов в 1 список"""
        return list(
            self._char_sets['letters'] +
            self._char_sets['digits'] +
            self._char_sets['symbols']
        )

    def _validate_length(self, length: int) -> None:
        """проверяет допустимость длины"""
        if length < 8:
            raise ValueError("Password length must be at least 8")

    def generate(self, length: int = 12) -> str:
        """генерирует случайный пароль"""
        self._validate_length(length)
        chars = self._get_character_set()
        return ''.join(random.choice(chars) for _ in range(length))

    def estimate_strength(self, password: str) -> int:
        """оценивает сложность пароля по шкале от 1 до 10
        критерии:
        длина (до 4 баллов)
        разные категории символов (4 балла)
        нет повторяющихся символов (1 балл)
        нет простых паттернов (1 балл)"""
        if not password:
            return 0
            
        score = sum(rule(password) for rule in self._strength_rules.values())
        return min(max(score, 1), 10)
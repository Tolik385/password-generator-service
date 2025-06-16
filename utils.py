import random
import string
from typing import List


class PasswordGenerator:
    """Генератор безопасных паролей"""

    def __init__(self):
        self._char_sets = {
            'letters': string.ascii_letters,
            'digits': string.digits,
            'symbols': '!@#$%^&*()_+-='
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
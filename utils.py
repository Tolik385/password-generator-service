import random
import string
from typing import List, Dict


class PasswordGenerator:
    """генератор с настройками и оценкой сложности"""

    def __init__(
        self,
        length: int = 12,
        use_symbols: bool = True,
        use_digits: bool = True
    ):
        """иинициализация генератора
        длина пароля (8-64 символа)
        использовать спецсимволы
        использовать цифры"""
        self.length = length
        self.use_symbols = use_symbols
        self.use_digits = use_digits
        self._validate_settings()

        """инициализация наборов символов"""
        self._char_sets = {
            'lower': string.ascii_lowercase,
            'upper': string.ascii_uppercase,
            'digits': string.digits,
            'symbols': string.punctuation
        }

    def _validate_settings(self) -> None:
        """проверка корректности настроек"""
        if not 8 <= self.length <= 64:
            raise ValueError("Длина пароля должна быть от 8 до 64 символов")

    def _get_available_chars(self) -> List[str]:
        """генерирует список доступных символов"""
        chars = self._char_sets['lower'] + self._char_sets['upper']
        if self.use_digits:
            chars += self._char_sets['digits']
        if self.use_symbols:
            chars += self._char_sets['symbols']
        return list(chars)

    def generate(self) -> str:
        """генерация пароля на основе настроек"""
        chars = self._get_available_chars()
        return ''.join(random.choice(chars) for _ in range(self.length))

    def estimate_strength(self, password: str) -> int:
        """оценка сложности пароля (1-10 баллов)
        критерии:
        длина пароля (макс. 4 балла)
        наличие символов разного типа (макс. 4 балла)
        отсутствие повторяющихся символов (1 балл)
        отсутствие простых последовательностей (1 балл)"""
        if not password:
            return 0

        score = 0
        
        """оценка длины"""
        score += min(len(password) // 2, 4)
        
        """оценка разнообразия"""
        checks = {
            'lower': any(c in self._char_sets['lower'] for c in password),
            'upper': any(c in self._char_sets['upper'] for c in password),
            'digit': self.use_digits and any(c in self._char_sets['digits'] for c in password),
            'symbol': self.use_symbols and any(c in self._char_sets['symbols'] for c in password)
        }
        score += sum(checks.values())
        
        """доп проверки"""
        if len(set(password)) == len(password):
            score += 1
            """нет повторяющихся символов"""
            
        if not any(
            password[i:i+3].isdigit() or 
            password[i:i+3].islower() or 
            password[i:i+3].isupper()
            for i in range(len(password)-2)
        ):
            score += 1  
            """нет простых последовательностей"""
            
        return min(max(score, 1), 10)

import math
import numpy as np
import re
import typing as ty

from core import config
from core.lib.handlers.crypt.crypt_handler_interface import CryptHandler


class CipherBlock(CryptHandler):
    _cipher_type: str
    _custom_offset: int
    _alphs: ty.Dict

    _cur_alph: str

    def __init__(self) -> None:
        """Init Handler"""
        self.handler_name = "Cipher Block"
        self._cipher_types_avail = { "custom" : self._custom_block }

        self._alphs = { 'eng': { 'forward' : "abcdefghijklmnopqrstuvwxyz",
                                 'backward': "zyxwvutsrqponmlkjihgfedcba" },
                        'ru' : { 'forward' : "абвгдеёжзийклмнопрстуфхцчшщъыьэюя", 
                                 'backward': "яюэьыъщшчцхфутсрпонмлкйизжёедгвба" } }

        self.cipher_type = 'custom'
        self.cols_count = 5

    @property
    def cipher_type(self) -> str:
        return self._cipher_type

    @cipher_type.setter
    def cipher_type(self, cipher_type_name: str) -> None:
        if cipher_type_name in self._cipher_types_avail:
            self._cipher_type = cipher_type_name
            return
        
        self._raise_error(f"No such simple substitution '{cipher_type_name}'")

    @property
    def custom_offset(self) -> int:
        return self._custom_offset

    @custom_offset.setter
    def custom_offset(self, custom_offset: int) -> None:
        try:
            custom_offset = int(custom_offset)
        except:
            self._raise_error(f"Error in custom offset creating (got {custom_offset})")

        self._custom_offset = custom_offset
        return
        
    def shift_char(self, char, block_number):
        char = char.lower()
        self.cur_alph = self._alphs['eng']['forward']

        if self._alphs['ru']['forward'].find(char) + 1:
            self.cur_alph = self._alphs['ru']['forward']

        shifted_alphabet = self.cur_alph[block_number:] + self.cur_alph[:block_number]
        return char.translate(str.maketrans(self.cur_alph, shifted_alphabet))

    def _custom_block(self, data: str, crypt=True) -> str:
        """
        Apply custom transposition encryption/decryption to text

        Parameters
        ----------
        data : str
                Text to encrypt or decrypt
        crypt : bool
                Information encrypt the text or decrypt it on the contrary
        """

        cur_block_num = -1
        self.custom_offset = -10
        incr = -1

        if crypt:
            cur_block_num += 2
            self.custom_offset += 20
            incr += 2

        result = []

        for i in range(0, len(data), 4):
            cur_block = data[i:i + 4]
            shifted_block = re.sub(r'[A-Za-zА-ЯЁа-яё]', lambda match: self.shift_char(match.group(), cur_block_num), cur_block)
            result.append(shifted_block)

            cur_block_num = int(math.copysign(int(cur_block_num % self.custom_offset + incr), cur_block_num))

        return ''.join(result)

    def _run(self, data: str, crypt=True) -> str:
        """
        Return encrypted/decrypted data

        Parameters
        ----------
        data : str
                Text to encrypt or decrypt
        crypt : bool
                Information encrypt the text or decrypt it on the contrary
        """

        data = self._cipher_types_avail[self.cipher_type](data, crypt=crypt)

        return data

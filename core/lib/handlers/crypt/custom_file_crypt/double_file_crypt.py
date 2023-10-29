from math import ceil
import numpy as np
import random
import typing as ty

from core import config
from core.lib.handlers.crypt.crypt_handler_interface import CryptHandler


class DoubleFileCrypt(CryptHandler):
    orig_file: str
    additional_file: str
    processed_file: str

    def __init__(self) -> None:
        """Init Handler"""
        self.handler_name = "Custom Single-file Encryptor"
        self.orig_file = 'orig.txt'
        self.additional_file = 'addit.txt'
        self.processed_file = 'processed.txt'

    def _custom_function(self, crypt: bool) -> None:
        orig_file = open(self.orig_file, "r")
        processed_file = open(self.processed_file, "w")

        addit_lines_array = []
        processed_lines_array = []

        if crypt:
            additional_file = open(self.additional_file, "w")
            for line in orig_file.readlines():
                line = line.replace('\n', '')
                addit_new_line = ''
                processed_new_line = ''

                for char in line:
                    addit_new_char_int = random.randint(ord(char) + 32, 2000)
                    addit_new_line += chr(addit_new_char_int)

                    processed_new_line += chr(abs(addit_new_char_int - ord(char)))

                addit_lines_array.append(addit_new_line)
                processed_lines_array.append(processed_new_line)

            additional_file.writelines('\n'.join(addit_lines_array))
            processed_file.writelines('\n'.join(processed_lines_array))

            return
        
        additional_file = open(self.additional_file, "r")
        for orig_line, addit_line in zip(orig_file.readlines(), additional_file.readlines()):
            orig_line = orig_line.replace('\n', '')
            addit_line = addit_line.replace('\n', '')
            processed_new_line = ''

            for idx, orig_char in enumerate(orig_line):
                processed_new_line += chr(ord(addit_line[idx]) - ord(orig_char))

            processed_lines_array.append(processed_new_line)

        processed_file.writelines('\n'.join(processed_lines_array))

        return

    def _run(self, data: str = '', crypt: bool = True) -> None:
        """
        Return encrypted/decrypted data

        Parameters
        ----------
        data : str
                Text to encrypt or decrypt
        crypt : bool
                Information encrypt the text or decrypt it on the contrary
        """

        self._custom_function(crypt=crypt)

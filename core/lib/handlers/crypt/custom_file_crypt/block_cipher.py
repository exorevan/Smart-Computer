import math
import re

from core.lib.handlers.crypt import consts_cipher
from core.lib.handlers.crypt.crypt_handler_interface import CryptHandler


class CipherBlock(CryptHandler):
    _cipher_type: str = "custom"
    _custom_offset: int  # pyright: ignore[reportUninitializedInstanceVariable]
    _alphs: dict[str, dict[str, str]] = consts_cipher.ALPHABETS

    cur_alph: str | None = None

    def __init__(self) -> None:
        """Init Handler"""
        self.handler_name = "Cipher Block"
        self._cipher_types_avail = {"custom": self._custom_block}

        self.custom_offset = -10
        self.cols_count = 5

    @property
    def custom_offset(self) -> int:
        return self._custom_offset

    @custom_offset.setter
    def custom_offset(self, custom_offset: int) -> None:
        try:
            custom_offset = int(custom_offset)
        except:
            self._raise_error(
                txt=f"Error in custom offset creating (got {custom_offset})"
            )

        self._custom_offset = custom_offset
        return

    def shift_char(self, char: str, block_number: int) -> str:
        char = char.lower()
        self.cur_alph = self._alphs["eng"]["forward"]

        if self._alphs["ru"]["forward"].find(char) + 1:
            self.cur_alph = self._alphs["ru"]["forward"]

        shifted_alphabet: str = (
            self.cur_alph[block_number:] + self.cur_alph[:block_number]
        )
        return char.translate(str.maketrans(self.cur_alph, shifted_alphabet))

    def _custom_block(self, data: str, crypt: bool = True) -> str:
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

        result: list[str] = []

        cur_block: str
        shifted_block: str
        for i in range(0, len(data), 4):
            cur_block = data[i : i + 4]
            shifted_block = re.sub(
                r"[A-Za-zА-ЯЁа-яё]",
                lambda match: self.shift_char(
                    char=match.group(), block_number=cur_block_num
                ),
                cur_block,
            )
            result.append(shifted_block)

            cur_block_num = int(
                math.copysign(
                    int(cur_block_num % self.custom_offset + incr), cur_block_num
                )
            )

        return "".join(result)

    def _run(self, data: str, crypt: bool = True) -> str:
        """
        Return encrypted/decrypted data

        Parameters
        ----------
        data : str
                Text to encrypt or decrypt
        crypt : bool
                Information encrypt the text or decrypt it on the contrary
        """

        data = self._cipher_types_avail[self._cipher_type](data, crypt=crypt)

        return data

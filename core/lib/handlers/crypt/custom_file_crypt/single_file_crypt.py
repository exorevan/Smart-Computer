from core.lib.handlers.crypt.crypt_handler_interface import CryptHandler


class SingleFileCrypt(CryptHandler):
    base_alph: str
    crypt_alph: str

    orig_file: str
    processed_file: str

    def __init__(self) -> None:
        """Init Handler"""
        self.handler_name = "Custom Single-file Encryptor"

        self.base_alph = "АЕЁИОУЫЭЮЯ"
        self.crypt_alph = "ЫЯОАЮЁЭЕИУ"

        self.orig_file = "orig.txt"
        self.processed_file = "processed.txt"

    def _custom_function(self, crypt: bool = True) -> None:
        """
        Apply custom function encryption/decryption to text

        Parameters
        ----------
        crypt : bool
                Information encrypt the text or decrypt it on the contrary
        """
        if not crypt:
            temp_alph: str = self.base_alph
            self.base_alph = self.crypt_alph
            self.crypt_alph = temp_alph

        processed_file = open(file=self.processed_file, mode="w")
        orig_file = open(file=self.orig_file, mode="r")

        line: str
        letter_idx: int
        for line in orig_file.readlines():
            new_line = ""

            for char in line:
                letter_idx = self.base_alph.find(char.upper())

                if letter_idx + 1:
                    new_line += self.crypt_alph[letter_idx]
                    continue

                new_line += char

            _ = processed_file.write(new_line)

    def _run(
        self,
        data: str = "",  # pyright: ignore[reportUnusedParameter]
        crypt: bool = True,
    ) -> None:
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

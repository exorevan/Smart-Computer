import typing as ty

from core import config
from core.lib.handlers.handler_interface import Handler


class SimpleSubstitute(Handler):
    _sub_type: str
    _cesar_offset: int

    _alphs: ty.Dict
    _special_symbols: str
    _sub_types_avail: ty.Dict

    _new_alph: str
    _current_alph: str

    def __init__(self) -> None:
        """Init Handler"""
        self.handler_name = "Simple Substitute Encryptor"

        self._alphs = { 'eng': { 'forward' : "abcdefghijklmnopqrstuvwxyz",
                                 'backward': "zyxwvutsrqponmlkjihgfedcba" },
                        'ru' : { 'forward' : "абвгдеёжзийклмнопрстуфхцчшщъыьэюя", 
                                 'backward': "яюэьыъщшчцхфутсрпонмлкйизжёедгвба" } }
        
        self._special_symbols = "1234567890 ,.!?:;'{}%$#№@^*()<>&|/\\\n\r\t\""
        
        self._sub_types_avail = { "cesar" : self._cesar_substitute,
                                  "atbash": self._atbash_substitute }
        
        self.sub_type = "cesar"
        self.cesar_offset = 5

    @property
    def sub_type(self) -> str:
        return self._sub_type

    @sub_type.setter
    def sub_type(self, sub_type_name: str) -> None:
        if sub_type_name in self._sub_types_avail:
            self._sub_type = sub_type_name
            return
        
        self._raise_error(f"No such simple substitution '{sub_type_name}'")

    @property
    def cesar_offset(self) -> str:
        return self._cesar_offset

    @cesar_offset.setter
    def cesar_offset(self, cesar_offset: ty.Union[str, int]) -> None:
        try:
            self._cesar_offset = int(cesar_offset)
        except:
            self._raise_error(f"Cannot cast '{cesar_offset}' to cesar_offset (int)")

    def encrypt(self, data: str) -> str:
        data = self._run(data, crypt=True)

        return data

    def decrypt(self, data: str) -> str:
        data = self._run(data, crypt=False)

        return data
    
    def _substitute_w_alph(self, data: str, alph_code: str) -> str:
        new_data = ''

        for _, letter in enumerate(data):
            if letter in self._special_symbols:
                new_data += letter
                continue

            letter_idx = self._current_alph.find(letter.lower())

            if not letter_idx + 1:
                self._raise_error(f"There's no such letter '{letter}' in {alph_code} alphabet")

            new_letter = self._new_alph[letter_idx]

            if letter.islower():
                new_data += new_letter
                continue

            new_data += new_letter.upper()

        return new_data

    def _select_alph(self, data: str) -> ty.Union[str, None]:
        """
        Find the alphabet corresponding to the text

        Parameters
        ----------
        data : str
                Text to encrypt or decrypt
        """
        
        for letter in data:
            for alph_key in self._alphs:
                alph = self._alphs[alph_key]['forward']

                if letter.lower() in alph:
                    return alph_key, alph
            
        self._raise_error(f"No alphabet with these letters '{data[:config.MAX_TEXT_LENGTH_TO_PRINT]}'")

    def _generate_alph_for_cesar(self, alph: str, crypt: int = 1) -> str:
        """
        Generate new alphabet for cesar's cipher

        Parameters
        ----------
        alph : str
                Alphabet to create a new one based on
        crypt : int
                Information encrypt the text or decrypt it on the contrary
        """
        
        return alph[crypt * self.cesar_offset : ] + alph[ : crypt * self.cesar_offset]

    def _atbash_substitute(self, data: str, crypt: int = 1) -> str:
        """
        Apply Abash encryption/decryption to text

        Parameters
        ----------
        data : str
                Text to encrypt or decrypt
        crypt : int
                Information encrypt the text or decrypt it on the contrary
        """

        alph_code, alph = self._select_alph(data)

        self._current_alph = alph
        self._new_alph = self._alphs[alph_code]['backward']

        new_data = self._substitute_w_alph(data, alph_code)

        return new_data


    def _cesar_substitute(self, data: str, crypt: int = 1) -> str:
        """
        Apply Cesar encryption/decryption to text

        Parameters
        ----------
        data : str
                Text to encrypt or decrypt
        crypt : int
                Information encrypt the text or decrypt it on the contrary
        """
        
        alph_code, alph = self._select_alph(data)

        self._current_alph = alph
        self._new_alph = self._generate_alph_for_cesar(alph, crypt)

        new_data = self._substitute_w_alph(data, alph_code)

        return new_data

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

        offset_multiplier = int(crypt) * 2 - 1

        data = self._sub_types_avail[self.sub_type](data, crypt=offset_multiplier)

        return data

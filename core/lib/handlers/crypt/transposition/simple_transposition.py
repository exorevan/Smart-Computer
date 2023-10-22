from math import ceil
import numpy as np
import typing as ty

from core import config
from core.lib.handlers.handler_interface import Handler


class SimpleTransposition(Handler):
    _trans_type: str
    _cols_count: int

    def __init__(self) -> None:
        """Init Handler"""
        self.handler_name = "Simple Transposition Encryptor"
        self._trans_types_avail = { "route" : self._route_transposition }

        self.trans_type = 'route'
        self.cols_count = 5

    @property
    def trans_type(self) -> str:
        return self._trans_type

    @trans_type.setter
    def trans_type(self, trans_type_name: str) -> None:
        if trans_type_name in self._trans_types_avail:
            self._trans_type = trans_type_name
            return
        
        self._raise_error(f"No such simple substitution '{trans_type_name}'")

    @property
    def cols_count(self) -> int:
        return self._cols_count

    @cols_count.setter
    def cols_count(self, cols_count: int) -> None:
        try:
            cols_count = int(cols_count)
        except:
            self._raise_error(f"Error in columns count creating (got {cols_count})")

        if cols_count > 0:
            self._cols_count = cols_count
            return
        
        self._raise_error(f"Negative number for columns count")

    def encrypt(self, data: str) -> str:
        data = self._run(data, crypt=True)

        return data

    def decrypt(self, data: str) -> str:
        data = self._run(data, crypt=False)

        return data

    def _route_transposition(self, data: str, crypt=True) -> str:
        """
        Apply route transposition encryption/decryption to text

        Parameters
        ----------
        data : str
                Text to encrypt or decrypt
        crypt : bool
                Information encrypt the text or decrypt it on the contrary
        """

        self.rows_count = ceil(len(data) / self.cols_count)
        data += ''.join(' ' for _ in range(self.rows_count * self.cols_count - len(data)))

        if crypt:
            data_matrix = np.array(list(data)).reshape(self.rows_count, self.cols_count)
            right_data_matrix = np.flip(data_matrix, 0).T
        else:
            data_matrix = np.array(list(data)).reshape(self.cols_count, self.rows_count)
            right_data_matrix = np.flip(data_matrix, 1).T

        data = ''.join(map(str, right_data_matrix.flatten())).lower().rstrip()

        return data

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

        data = self._trans_types_avail[self.trans_type](data, crypt=crypt)

        return data

from core.lib.handlers.handler_interface import Handler


class CryptHandler(Handler):
    def encrypt(self, data: str = '') -> str:
        data = self._run(data, crypt=True)

        return data

    def decrypt(self, data: str = '') -> str:
        data = self._run(data, crypt=False)

        return data
    
    def _custom_into_to_str_fill(self, code: str, str_len: int) -> str:
        return (f"%{str_len}.f" % code).replace(' ', '0')

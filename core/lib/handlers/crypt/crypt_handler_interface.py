from core.lib.handlers.handler_interface import Handler


class CryptHandler(Handler):
    def _run(
        self, data: str, crypt: bool  # pyright: ignore[reportUnusedParameter]
    ) -> str | None:
        raise NotImplementedError()

    def encrypt(self, data: str = "") -> str:
        processed_data: str = self._run(data=data, crypt=True)

        return processed_data

    def decrypt(self, data: str = "") -> str:
        processed_data: str = self._run(data=data, crypt=False)

        return processed_data

    def _custom_into_to_str_fill(self, code: str, str_len: int) -> str:
        return (f"%{str_len}.f" % code).replace(" ", "0")

"""Ответы сервера."""

from datetime import datetime
from constants import (
    RESPONSE_HEADERS,
    OK,
)

CRLF = b'\r\n'


class Response:
    """Ответы сервера."""

    def __init__(self, code=None, content=None, mime_type=None, length=None, method=None):
        self.code = code
        self.content = content
        self.mime_type = mime_type
        self.length = length
        self.method = method

    def get_answer(self):
        """Получить ответ."""
        report = [
            RESPONSE_HEADERS.get(self.code),
            f'Date: {datetime.today().strftime("%a, %d %b %Y %H:%M:%S %Z")}'.encode(),
            b'Server: MyTestServer',
            b'Connection: close',
        ]
        if self.code == OK:
            report.extend(
                [f'Content-Length: {self.length}'.encode(), f'Content-Type: {self.mime_type}'.encode()]
            )
            if self.method == 'GET':
                report.append(CRLF + self.content)

        report.append(CRLF)
        return CRLF.join(report)


FORBIDDEN_RESPONSE = Response(code=403)
NOT_FOUND_RESPONSE = Response(code=404)
NOT_ALLOWED_RESPONSE = Response(code=405)

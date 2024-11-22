"""Основной файл."""

import socket
import threading
import logging
import os

from constants import OK

from responses import (
    NOT_FOUND_RESPONSE,
    NOT_ALLOWED_RESPONSE,
    Response,
)

HOST = "localhost"
PORT = 8080
DOCUMENT_ROOT = './www'
PATH = '/index.html'


logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname).1s [%(threadName)s] %(message)s',
    datefmt='%Y.%m.%d %H:%M:%S',
)


def handle_request(client_socket: socket.socket):
    """Обработчик запроса."""
    try:
        request = client_socket.recv(1024).decode()

        lines = request.splitlines()
        if lines:
            method = lines[0].split()[0]
            file_path = get_file_path()

            if method in ['GET', 'HEAD']:
                response = get_get_or_head_response(file_path, method)
            else:
                response = get_not_allowed_response(method)

            client_socket.sendall(response)
    except Exception as e:
        raise e
    finally:
        try:
            client_socket.close()
        except Exception as e:
            logging.error(f'Error closing connection: {e}')


def get_file_path() -> str:
    """Получение пути шаблона."""
    file_path = os.path.join(DOCUMENT_ROOT, PATH.lstrip('/'))
    logging.info(f'Requested file "{file_path}" FOUND')
    return file_path


def get_get_or_head_response(file_path, method) -> bytes:
    """Получение ответа методов HEAD или GET."""
    if os.path.isfile(file_path):
        with open(file_path, 'rb') as file:
            content = file.read()

        response = get_response(content, method)
        logging.info(f'Server started on http://{HOST}:{PORT}')

    else:
        logging.info('Requested file is not not exist')
        response = NOT_FOUND_RESPONSE.get_answer()
    return response


def get_response(content: bytes, method: str) -> bytes:
    """Получение ответа 200 для GET и HEAD."""
    return Response(
        code=OK,
        content=content if method == 'GET' else None,
        length=len(content),
        mime_type='text/html',
        method=method,
    ).get_answer()


def get_not_allowed_response(method: str) -> bytes:
    """Получение ответа неразрешенного метода."""
    logging.info(f'Method "{method}" is not allowed')
    return NOT_ALLOWED_RESPONSE.get_answer()


def start_server():
    """Старт сервера."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    logging.info(f'Server started on http://{HOST}:{PORT}')

    while True:
        client_socket, url = server_socket.accept()
        logging.info(f'Connected from {url}')
        thread = threading.Thread(target=handle_request, args=(client_socket,))
        thread.start()


if __name__ == "__main__":
    """Движок."""
    start_server()

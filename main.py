# ЗАДАЧА 2

import os
import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upLoad_Link(self, disk_file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        print(disk_file_path)
        params = {'path': disk_file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        print(response)
        return response.json()

    def upload(self, file_path: str, filename):
        """Метод загруджает файл file_path на яндекс диск"""

        href = self._get_upLoad_Link(disk_file_path=file_path).get('href')

        if href:
            with open(os.path.abspath(filename), 'rb') as f:
                response = requests.put(href, f)
                response.raise_for_status()
                if response.status_code == 201:
                    print('Файл успешно загружен на Яндекс.Диск')


if __name__ == '__main__':
    uploader = YaUploader('')
    result = uploader.upload('Netology/test_upload.txt', 'test_upload.txt')

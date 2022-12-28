import requests
from setting import TOKEN


class YaUploader:
    host = 'https://cloud-api.yandex.net/'

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}

    def upload(self, path_to_file: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать
        uri = 'v1/disk/resources/upload'
        url = self.host + uri
        file_name = path_to_file.split
        params = {'path': file_name}
        response = requests.get(url, headers=self.get_headers(), params=params)
        upload_link = response.json()['href']
        print(upload_link)
        resp = requests.put(upload_link, headers=self.get_headers(), data=open(path_to_file, 'rb'))


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'testt.json'
    token = TOKEN
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)

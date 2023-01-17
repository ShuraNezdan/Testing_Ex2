import requests
from pprint import pprint


class YaUploader:
    HOST = 'https://cloud-api.yandex.net:443'
    token = 'введите свой токен'

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
    
    # Просто проверка подключения
    # def get_ya(self):
    #     url = f'{self.HOST}/v1/disk'
    #     headers = self.get_headers()
    #     response = requests.get(url, headers=headers)
    #     pprint(response.json()['user'])

    def create_folder(self, name_new_folder: str):
        url = f'{self.HOST}/v1/disk/resources/'
        headers = self.get_headers()
        params = {'path': name_new_folder}
        response = requests.put(url, params=params, headers=headers)
        print(response)


if __name__ == '__main__':

    Yandex = YaUploader()
    # Yandex.get_ya()
    Yandex.create_folder('ДляПроверки')
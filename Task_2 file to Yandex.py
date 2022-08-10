TOKEN = 'y0_AQAAAAA_A4UUAADLWwAAAADLF6At6ut-A5tiQZ62UcSdetciEoASM_s'
from email import header
from urllib import response
import requests
from pprint import pprint

class YandexDisk:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        # print(self.__dict__)
        return {
                'Content-Type': 'application/json',
                'Authorization': 'OAuth {}'.format(self.token)
            }
    
    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
    
        response = requests.get(files_url, headers=headers)
        return response.json()

if __name__ =="__main__":

    ya = YandexDisk(token = TOKEN)
    # print(ya.__dict__)
    pprint(ya.get_files_list())

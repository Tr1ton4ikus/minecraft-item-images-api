import json
import requests


class MinecraftItemImage:
    def __init__(self, json_path='minecraft-api.json'):
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.translations = data.get('translations', {})

    def get_eng_name(self, russian_name: str) -> str:
        eng_name = self.translations.get(russian_name)
        if not eng_name:
            raise ValueError(f"Предмет с русским названием '{russian_name}' не найден.")
        return eng_name

    def get_image_url(self, russian_name: str) -> str:
        eng_name = self.get_eng_name(russian_name)
        return f"https://idpredmetov.ru/sprites/32/{eng_name}.png"

    def get_image(self, russian_name: str) -> bytes:
        url = self.get_image_url(russian_name)
        response = requests.get(url)
        if response.status_code != 200:
            raise ValueError(f"Не удалось скачать изображение. Код: {response.status_code}")
        if 'image/png' not in response.headers.get('Content-Type', ''):
            raise ValueError(f"Полученный файл не является PNG изображением.")
        return response.content

    def get_image_or_url(self, russian_name: str, mode: str = 'img') -> str | bytes:
        if mode == 'url':
            return self.get_image_url(russian_name)
        elif mode == 'img':
            return self.get_image(russian_name)
        else:
            raise ValueError("Неверный формат, верный: 'img' или 'url'")


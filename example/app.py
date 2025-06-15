from module.MinecraftItemApi import MinecraftItemImage

if __name__ == '__main__':
    minecraft = MinecraftItemImage('../minecraft-api.json')

    # Получить и сохранить картинку
    item_name = 'Алмаз'
    image_bytes = minecraft.get_image_or_url(item_name, mode='img')
    with open(f"{minecraft.get_eng_name(item_name)}.png", 'wb') as f:
        f.write(image_bytes)

    # Получить ссылку
    url = minecraft.get_image_or_url(item_name, mode='url')
    print("Ссылка на изображение:", url)

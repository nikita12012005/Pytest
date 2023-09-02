import docker

# Создаем клиент Docker
client = docker.from_env()

# Загружаем образ (если необходимо)
client.images.pull('имя_образа:тег')

# Создаем и запускаем контейнер
container = client.containers.run('имя_образа:тег', detach=True)

# Печатаем ID контейнера
print(f"Запущен контейнер с ID: {container.id}")

# Остановка и удаление контейнера (по желанию)
container.stop()
container.remove()

.PHONY: install dev build clean lint update

# Установка зависимостей
install:
	npm install

# Запуск сервера разработки
dev:
	npm run dev

# Сборка проекта для продакшена
#build:
#	npm run build

# Очистка временных файлов и зависимостей
clean:
	rm -rf node_modules
	rm -rf dist

# Проверка и исправление ошибок линтинга
#lint:
#	npm run lint

# Обновление всех зависимостей до последних версий
update:
	npx npm-check-updates -u
	npm install
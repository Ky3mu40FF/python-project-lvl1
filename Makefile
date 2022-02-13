# Установка зависимостей
install:
	poetry install

# Запуск скрипта brain-games (brain_games.scripts.brain_games:main)
brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 brain_games

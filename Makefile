install:
	poetry install

build:
	poetry build

package-install:
	python3 -m pip install dist/*.whl

 publish:
	poetry publish --dry-run

make lint:
	poetry run flake8 gendiff

make check:
	poetry run pytest

make test-coverage:
	poetry run pytest --cov



.PHONY: install test lint selfcheck check build
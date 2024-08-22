.PHONY: test
test:
	poetry run coverage run -m pytest

.PHONY: coverage
coverage: test
	poetry run coverage report

.PHONY: build
build:
	poetry build

.PHONY: publish
publish:
	poetry publish --build

.PHONY: format
format:
	poetry run black

.PHONY: bump-version
bump-version:
	poetry version --next-phase ${phase}
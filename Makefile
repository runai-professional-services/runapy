include $(shell [ -f .env ] && echo .env)

PHONY: build
build:
	poetry build

PHONY: publish
publish:
	poetry publish -r testpypi --username __token__ --password $(PYPI_TOKEN)

PHONY: publish-test
publish-test:
	poetry publish -r testpypi --username __token__ --password $(TEST_PYPI_TOKEN)
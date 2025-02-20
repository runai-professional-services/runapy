generator:=python
package_name:=runai
client_dir:=../
templates_config_dir:=./templates/config.yaml
swagger_file:=swagger.json
current_package_version := $(shell grep 'packageVersion:' $(templates_config_dir) | awk '{print $$2}')

OS := $(shell uname)
SED_INPLACE :=
ifeq ($(OS),Darwin)  # macOS
	SED_INPLACE = sed -i ''
	OPENAPI_GENERATOR_BIN = openapi-generator
else                 # Linux
	SED_INPLACE = sed -i
	OPENAPI_GENERATOR_BIN = openapi-generator-cli
endif


.PHONY: generate
generate:
	$(OPENAPI_GENERATOR_BIN) \
	generate -g $(generator) \
	-i $(swagger_file) \
	--package-name $(package_name) \
	--output $(client_dir) \
	-c $(templates_config_dir) \
	--global-property apiDocs=false \
	--global-property modelDocs=false


.PHONY: pre-process
pre-process:
	python3 scripts/pre_processing.py

.PHONY: post-process
post-process:
	python3 scripts/post_processing.py

.PHONY: format
format:
	black $(client_dir) --quiet

.PHONY: generate-and-format
generate-and-format: pre-process generate post-process format

.PHONY: set-package-version
set-package-version:
	@echo "Setting package version to $(version)"
	$(SED_INPLACE) 's/packageVersion: $(current_package_version)/packageVersion: $(version)/' $(templates_config_dir)
	$(SED_INPLACE) 's/version = "$(current_package_version)"/version = "$(version)"/' $(client_dir)pyproject.toml

# Makefile

# Define the version of your project
VERSION = 1.0.0
ENV ?= development

.PHONY: help version clean setup install deploy destroy apply plan test release

help:
	@echo Available commands:
	@echo ================================================================
	@echo make help     : Show this help message
	@echo make version  : Show project version
	@echo make clean    : Clean temporary files
	@echo make setup    : Run setup tasks
	@echo make install  : Install dependencies
	@echo make deploy   : Deploy application
	@echo make destroy  : Destroy infrastructure
	@echo make apply    : Apply infrastructure changes
	@echo make plan     : Show planned changes
	@echo make test     : Run tests
	@echo make release  : Run clean, install, test, and deploy in sequence

version:
	@echo Project version: $(VERSION)

clean:
	@echo Cleaning up...

setup:
	@echo Running setup tasks...

install:
	@echo Installing dependencies...

deploy:
	@echo Deploying to environment: $(ENV)

destroy:
	@read -p "Are you sure you want to destroy infrastructure? (yes/no): " ans; \
	if [ "$$ans" = "yes" ]; then \
	    echo "Destroying infrastructure..."; \
	else \
	    echo "Destroy cancelled"; \
	fi

apply:
	@echo Applying infrastructure changes...

plan:
	@echo Planning infrastructure changes...

test:
	@echo Running tests...

release: clean install test deploy
	@echo Release complete!

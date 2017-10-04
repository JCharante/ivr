SHELL = /bin/bash

all:
	@echo "No default command"
freeze:
	pip freeze | grep -v "pkg-resources" > requirements.txt
install:
	sudo apt install -y python3.6 python3-pip python3-dev virtualenv
	if [ ! -d ".venv" ]; then virtualenv -p python3.6 .venv; fi
	. .venv/bin/activate; pip install -r requirements.txt

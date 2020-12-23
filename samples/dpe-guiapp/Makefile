APPNAME=test-dpe-guiapp
PYTHONVERSION="3.6.9"
EXTRAS="none"

help:
	@echo "usage: make [command]"

download_bash_environment_manager:
	@if test ! -d ".tmp/bash-environment-manager-master";then \
		sudo su -m $(SUDO_USER) -c "mkdir -p .tmp"; \
		sudo su -m $(SUDO_USER) -c "cd .tmp; wget -O bash-environment-manager.zip https://github.com/terminal-labs/bash-environment-manager/archive/master.zip"; \
		sudo su -m $(SUDO_USER) -c "cd .tmp; unzip bash-environment-manager.zip"; \
	fi

ondesktop: download_bash_environment_manager
	@sudo bash .tmp/bash-environment-manager-master/types/python/assemble.sh $(APPNAME) $(SUDO_USER) conda
	@sudo bash .tmp/bash-environment-manager-master/types/python/emit_activate.sh $(APPNAME) $(SUDO_USER) conda

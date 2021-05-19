ROOT_DIR:=./
VENV:= parallels-venv
VENV_BIN_DIR:="$(VENV)/bin"

REQUIREMENTS_LOCAL:="./requirements.txt"

PIP:="$(VENV_BIN_DIR)/pip"

CMD_FROM_VIEW:=". $(VENV_BIN_DIR)/activate"

SYM:= "$(ROOT_DIR)/symgiza-pp"

URL:= "https://github.com/emjotde/symgiza-pp.git"
all: venv activate

venv:
	$(CMD_FROM_VIEW:): requirements.txt
	python3 -m venv $(VENV)
	@$(PIP) install -r $(REQUIREMENTS_LOCAL)
	source $(VENV_BIN_DIR)/activate

activate: venv
	if [ ! -d $(SYM) ]; then git clone https://github.com/emjotde/symgiza-pp.git; fi
	chmod a+rwx $(SYM)/configure
	cd $(SYM) && ./configure
	chmod a+rwx $(SYM)/install-sh
	cd $(SYM) && make
	chmod a+rwx $(ROOT_DIR)/train.sh
	chmod a+rwx $(ROOT_DIR)/extract.sh
	chmod a+rwx $(ROOT_DIR)/scripts/symgiza.sh

clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete

.PHONY: all venv run clean
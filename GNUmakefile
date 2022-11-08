SHELL		= /bin/bash
PY3		?= $(shell python3 --version >/dev/null 2>&1 && echo python3 || echo python )
VERSION		= $(shell $(PY3) -c 'from hdwallet import __version__; print( __version__.strip("v"))')
WHEEL		= dist/hdwallet-$(VERSION)-py3-none-any.whl

.PHONY:			all test build build-check wheel install-dev install clean FORCE

all:			build

test:
	$(PY3) -m pytest

build:			clean wheel

build-check:
	@$(PY3) -m build --version \
	    || ( \
		echo -e "\n\n!!! Missing Python modules; run:"; \
		echo -e "\n\n        $(PY3) -m pip install --upgrade pip setuptools wheel build\n"; \
	        false; \
	    )

wheel:			$(WHEEL)

$(WHEEL):		build-check FORCE
	$(PY3) -m build
	@ls -last dist

# Install from wheel, including all optional extra dependencies (except dev)
install-dev:		$(WHEEL) FORCE
	$(PY3) -m pip install --upgrade $<[tests]

install:		$(WHEEL) FORCE
	$(PY3) -m pip install --force-reinstall $<[cli,docs]

clean:
	@rm -rf build dist *.egg-info $(shell find . -name '__pycache__' )

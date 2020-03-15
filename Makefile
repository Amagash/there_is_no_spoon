clean:
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info

build: clean
	python setup.py sdist

install: build
	python setup.py install

deploy-pip: install
	pip install twine
	twine upload -u Amagash -p "${PASSWORD_PYPI}" dist/*
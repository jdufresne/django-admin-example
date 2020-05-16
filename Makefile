.PHONY: run
run: venv data
	venv/bin/python manage.py runserver

venv:
	python -m venv venv
	venv/bin/pip install -e ../django
	venv/bin/pip install docutils

.PHONY: data
data: venv
	rm -f db.sqlite3
	venv/bin/python manage.py migrate --run-syncdb
	venv/bin/python manage.py mkdata

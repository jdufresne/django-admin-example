.PHONY: data
data:
	rm -f db.sqlite3
	python manage.py migrate --run-syncdb
	python manage.py mkdata

.PHONY: run
run: data
	python manage.py runserver

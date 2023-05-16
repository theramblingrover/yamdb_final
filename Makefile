start:
	docker-compose -f ./infra/docker-compose.yaml up --build -d

configure:
	docker-compose -f ./infra/docker-compose.yaml exec web python manage.py makemigrations
	docker-compose -f ./infra/docker-compose.yaml exec web python manage.py migrate
	docker-compose -f ./infra/docker-compose.yaml exec web python manage.py collectstatic
	docker-compose -f ./infra/docker-compose.yaml exec web python manage.py createsuperuser

loadfixtures:
	docker-compose -f ./infra/docker-compose.yaml exec web python manage.py loaddata fixtures.json

stop:
	docker-compose -f ./infra/docker-compose.yaml down
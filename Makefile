SERVICE = backend
DEV_ENF_FILE = .env.dev
PROD_ENF_FILE = .env.prod

dev:
	@echo "Starting CodeSandbox Developement Server..."
	@docker compose --env-file $(DEV_ENF_FILE) up --build -d

prod:
	@echo "Starting CodeSandbox Production Server..."
	@docker compose --env-file $(PROD_ENF_FILE) up --build -d

down:
	@echo "Shutting down CodeSandbox Server."
	@docker compose down

run:
	@echo "Running Django WSGI Server..."
	@python src/manage.py runserver 0.0.0.0:8000

logs:
	docker compose logs -f $(SERVICE)

migrate:
	docker compose exec $(SERVICE) python manage.py migrate

makemigrations:
	docker compose exec $(SERVICE) python manage.py makemigrations

shell:
	docker compose exec $(SERVICE) python manage.py shell

superuser:
	docker compose exec $(SERVICE) python manage.py createsuperuser

collectstatic:
	docker compose exec $(SERVICE) python manage.py collectstatic --noinput


clean:
	@echo "Cleaning Docker..."
	@docker container prune -f

clean-all:
	@docker rmi codesandbox-backend:latest postgres:16 redis:7 || true

remove-backend-image:
	@docker rmi codesandbox-backend:latest || true
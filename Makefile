SERVICE = backend
DEV_ENF_FILE = Assets/EnvFiles/.env.dev
PROD_ENF_FILE = Assets/EnvFiles/.env.prod
LOCAL_ENF_FILE = Assets/EnvFiles/.env.local


dev: ## Start development server (Docker)
prod: ## Start production server (Docker)
down: ## Stop all services
run: ## Run Django dev server locally
logs: ## View logs
makemigrations: ## Create migrations (Docker)
migrate: ## Apply migrations (Docker)
shell: ## Open Django shell (Docker)
superuser: ## Create superuser (Docker)
collectstatic: ## Collect static files (Docker)
clean: ## Remove stopped containers
clean-all: ## Remove images
remove-backend: ## Remove backend image
run-frontend: ## Run frontend

help:
	@echo "Usage: make <target>"
	@echo ""
	@awk 'BEGIN {FS = ":.*##"; printf "\nAvailable commands:\n\n"} \
	/^[a-zA-Z_-]+:.*?##/ { printf "  %-15s %s\n", $$1, $$2 }' $(MAKEFILE_LIST)


dev:
	@echo "Starting CodeSandbox Development Server..."
	@cp $(DEV_ENF_FILE) .env
	@docker compose up --build -d

prod:
	@echo "Starting CodeSandbox Production Server..."
	@cp $(PROD_ENF_FILE) .env
	@docker compose --env-file $(PROD_ENF_FILE) up --build -d

down:
	@echo "Shutting down CodeSandbox Server."
	@docker compose down

run:
	@echo "Running Django WSGI Server..."
	@cp $(LOCAL_ENF_FILE) .env
	@python src/manage.py runserver 0.0.0.0:8000

run-frontend:
	@cd frontend && npm run dev

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

remove-backend:
	@docker rmi codesandbox-backend:latest || true


.DEFAULT_GOAL := help

%:
	@echo "Unknown command: '$@'"
	@echo "Run 'make help' to see available commands"
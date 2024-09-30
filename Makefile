dev:
	docker-compose -f compose.dev.yml up --build --remove-orphans

prod:
	docker-compose -f compose.prod.yml up --build --remove-orphans

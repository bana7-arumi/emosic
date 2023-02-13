DEV_YML="docker-compose.dev.yml"
PROD_YML="docker-compose.prod.yml"

up:
	@docker compose -f $(DEV_YML) up -d
down:
	@docker compose -f $(DEV_YML) down
build:
	@docker compose -f $(DEV_YML) build
up-prod:
	@docker compose -f $(PROD_YML) up -d
down-prod:
	@docker compose -f $(PROD_YML) down
build-prod:
	@docker compose -f $(PROD_YML) build
it-rust-app:
	@docker exec -it rust-app bash
it-bff:
	@docker exec -it bff bash

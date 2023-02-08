DEV_YML="docker-compose.dev.yml"

up:
	@docker compose -f $(DEV_YML) up -d
down:
	@docker compose -f $(DEV_YML) down
build:
	@docker compose -f $(DEV_YML) build
it-rust-app:
	@docker exec -it rust-app bash
it-bff:
	@docker exec -it bff bash
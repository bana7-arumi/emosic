CPU_YML = "docker-compose.cpu.yml"
GPU_YML = "docker-compose.gpu.yml"

# cpu
up:
	@docker compose -f $(CPU_YML) up -d
down:
	@docker compose -f $(CPU_YML) down
build:
	@docker compose -f $(CPU_YML) build
restart:
	@docker compose -f $(CPU_YML) restart

# gpu
up-gpu:
	@docker compose -f $(GPU_YML) up -d
down-gpu:
	@docker compose -f $(GPU_YML) down
build-gpu:
	@docker compose -f $(GPU_YML) build
restart-gpu:
	@docker compose -f $(GPU_YML) restart

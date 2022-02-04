########################################################################################################################
# One-off commands
########################################################################################################################

define run_one_off_command
	docker-compose -f docker-compose.yml run backend bash -c $(1) ; \
	docker-compose -f docker-compose.yml down --volumes --remove-orphans
endef

.PHONY: db_migration
db_migration:
	@echo "Enter a name for the migration script: "; \
    read script_name; \
    $(call run_one_off_command,"alembic upgrade head && alembic revision -m \"$$script_name\" --autogenerate")

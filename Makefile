########################################################################################################################
# One-off commands
########################################################################################################################

.PHONY: db_migration
db_migration:
	@echo "Enter a name for the migration script: "; \
    read script_name; \
    $(call "alembic upgrade head && alembic revision -m \"$$script_name\" --autogenerate")

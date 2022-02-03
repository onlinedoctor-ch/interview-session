#!/usr/bin/env sh

alembic upgrade head

uvicorn --host 0.0.0.0 --port 5000 --interface asgi3 --factory service.main:create_app --reload
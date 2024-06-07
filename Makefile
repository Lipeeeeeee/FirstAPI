run:
	@uvicorn firstAPI.main:app --reload

make-migrations:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic revision --autogenerate -m $(d)

migrate:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic upgrade head









build:
	docker-compose up -d


worker:
	#celery -A myapp worker -Q sunshine,moon
	celery -A myapp worker -Q sunshine,moon --loglevel=info

flower:
	celery flower --port=5555 --address=0.0.0.0 --broker=pyamqp://guest@localhost

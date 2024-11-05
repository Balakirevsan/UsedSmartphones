.PHONY: venv install run clean

venv:
	python3 -m venv venv
	./venv/bin/pip install --upgrade pip

install:
	/bin/bash -c "source venv/bin/activate && pip install -r requirements.txt"

run:
	venv/bin/uvicorn main:app --reload

clean:
	rm -rf venv
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
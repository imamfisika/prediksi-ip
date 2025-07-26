FROM python:3.10-slim-bullseye

WORKDIR /app

COPY requirements.txt .
RUN apt-get update && apt-get upgrade -y && apt-get clean && rm -rf /var/lib/apt/lists/* \
	&& pip install --no-cache-dir -r requirements.txt

COPY . .
COPY models/ ./models/

RUN python train_model.py

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
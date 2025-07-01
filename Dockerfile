# Gunakan image Python resmi
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Salin file ke dalam container
COPY . .

# Install dependency
RUN pip install --no-cache-dir -r requirements.txt

# Jalankan shell interaktif (biar bisa pakai container interaktif)
CMD [ "bash" ]

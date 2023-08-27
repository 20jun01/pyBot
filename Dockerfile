FROM python:3.11-slim

WORKDIR /

COPY requirements.txt .

# Install dependencies for PIL
RUN apt-get update && apt-get install -y \
    libjpeg-turbo-progs \
    gcc \
    g++ \
    python3-dev \
    zlib1g-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*
    
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]

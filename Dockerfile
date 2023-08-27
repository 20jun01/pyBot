FROM python:3.11-slim

WORKDIR /

COPY requirements.txt .

# Install dependencies for PIL
RUN apk --no-cache add \
    libjpeg-turbo \
    && apk --no-cache --virtual pydeps add gcc \
    g++ \
    python3-dev \
    musl-dev \
    cython \
    jpeg-dev \
    zlib-dev \
    && apk del --purge pydeps
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]

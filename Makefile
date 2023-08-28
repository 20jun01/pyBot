IMAGE_NAME = pybot

.PHONY: run build
run: build
	docker run -p 10000:10000 $(IMAGE_NAME)

build:
	docker build -t $(IMAGE_NAME) .
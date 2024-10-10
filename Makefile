IMAGE_NAME = tutors-linux-course
PORT = 8000

#Whether to use podman or docker
CONTAINER_ENGINE := $(shell command -v podman 2>/dev/null || echo docker)

build:
	$(CONTAINER_ENGINE) build -t $(IMAGE_NAME) -f ContainerFile .

run: build
	$(CONTAINER_ENGINE) run --rm -p $(PORT):$(PORT) $(IMAGE_NAME)

.PHONY: all
all: build run

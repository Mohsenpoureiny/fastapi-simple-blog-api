#!/usr/bin/env just --justfile

build:
  sudo docker-compose -f "docker-compose.yaml" up -d --build

run:
  sudo docker-compose -f "docker-compose.yaml" up
#!/usr/bin/env just --justfile

run:
  sudo docker-compose -f "docker-compose.yaml" up
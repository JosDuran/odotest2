#!/bin/bash
docker-compose down
docker volume prune -f
docker container prune -f
docker image prune -f
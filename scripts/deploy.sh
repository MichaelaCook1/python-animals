#! /bin/bash


docker-compose pull
docker stack deploy --compose-file docker-compose.yaml animalapp

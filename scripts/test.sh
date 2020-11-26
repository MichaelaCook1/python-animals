#! /bin/bash



docker build -t testing-img -f testing/Dockerfile .
docker run -it -d --name testing-cont testing-img

docker exec testing-cont pytest ./frontend --cov ./frontend

docker exec testing-cont pytest ./backend --cov ./backend

docker stop testing-cont 
docker rm testing-cont

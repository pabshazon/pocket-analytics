#!/usr/bin/env bash

docker-compose -f infra/local_env/docker-compose.yml down

colima stop

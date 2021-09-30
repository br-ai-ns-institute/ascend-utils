# -*- Makefile -*-
#
# A thin-ish wrapper around mostly "docker" commands for the specific
# kinds of tasks that are needed to interact with Ascend devices.
#
# Advantages:
# * simpiler and shorter commands than those needed to run docker or similar commands
# * this serves to focus attention on the collection of often-used commands are useful
#   in working with the Huawei and in particular Ascend devices
# * the invocations shown here can be used as a starting point for more elaborate command invocations

MAKE   = make
PYTHON = python3
LOGS = "/root/ascend/log/plog/"

# Use the `CONTAINER` variable to set the container you want to use
CONTAINER = tensorflow_container

DOCKER_EXEC = sudo docker exec -w $(PWD) -it $(CONTAINER)
LOG_CMD = "ls -1tr $(LOGS) | tail -n 1 | xargs -I {} cat $(LOGS){}"

help:
	@echo ''
	@echo 'Usage: make [TARGET] [file=*value*]
	@echo ''
	@echo 'TARGETS:'
	@echo ''
	@echo '  npu            List ascend devices on docker container tansorflow_container'
	@echo '  log            List latest ascend log file'
	@echo '  run            Run target bash script'
	@echo '  bs             Start bash console in docker container'
	@echo '  py-run         Run python file in docker container'
	@echo '  python         Start python interpreter in docker container'
	@echo ''
	@echo 'EXTRA ARGUMENTS:'
	@echo '  file=      Complete path of the bash script to be run (inside container)
	@echo '             values:   /home/username/process1.sh     - for training_hanson example'

npu:
	@$(DOCKER_EXEC) npu-smi info

log:
	@$(DOCKER_EXEC) bash -c $(LOG_CMD)

run:
	@$(DOCKER_EXEC) bash $(file)

python:
	@$(DOCKER_EXEC) python3 $(file)

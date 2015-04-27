MODULE_VM = $(APP_ROOT)/module_vm

#
# VM module
# 
# NOTE: All these commands are run within the `boot2docker` environment.
#

copy-vm-deps:
	# Docker does not follow symlinks (!?)
	rm -rf $(MODULE_VM)/appython $(MODULE_VM)/shared
	cp -R $(APPYTHON_ROOT)/appython $(MODULE_VM)/
	cp -R $(APP_ROOT)/shared $(MODULE_VM)/

tail-vm:
	@echo "Getting logs from vm (VM) module..."
	docker exec -it `docker ps --quiet` tail -f /var/log/app_engine/app.log.json

run-vm: prepare-dev copy-vm-deps
	@echo "Running vm (VM) module..."
	cd $(MODULE_VM); gcloud preview app run vm.yaml \
		--project $(PROJECT_ID) \
		--log-http

run-vm-debug: prepare-dev copy-vm-deps
	@echo "Running vm (VM) module..."
	cd $(MODULE_VM); gcloud preview app run vm.yaml \
		--project $(PROJECT_ID) \
		--log-http \
		--verbosity debug 

deploy-vm: prepare-prod copy-vm-deps
	@echo "Deploying vm (VM) module..."
	cd $(MODULE_VM); gcloud preview app deploy vm.yaml \
		--project $(PROJECT_ID) \
		--verbosity info \
		--version v1 --set-default

MODULE_VM = $(APP_ROOT)/module_vm

#
# VM module
# 
# NOTE: All these commands are run within the `boot2docker` environment.
#

add-geo-deps:
	# Docker does not follow symlinks (!?)
	rm -rf $(MODULE_VM)/appython $(MODULE_VM)/shared
	cp -R $(APPYTHON_ROOT)/appython $(MODULE_VM)/
	cp -R $(APP_ROOT)/shared $(MODULE_VM)/

tail-vm:
	@echo "Getting logs from vm (VM) module..."
	docker exec -it `docker ps --quiet` tail -f /var/log/app_engine/app.log.json

run-vm: add-geo-deps
	@echo "Running vm (VM) module..."
	cd $(MODULE_VM); gcloud --log-http --project $(PROJECT_ID) \
		preview app run vm.yaml

run-vm-debug: add-geo-deps
	@echo "Running vm (VM) module..."
	cd $(MODULE_VM); gcloud --log-http --verbosity debug --project $(PROJECT_ID) \
		preview app run vm.yaml

deploy-vm: add-geo-deps
	@echo "Deploying vm (VM) module..."
	cd $(MODULE_VM); gcloud --project $(PROJECT_ID) \
		preview app deploy vm.yaml

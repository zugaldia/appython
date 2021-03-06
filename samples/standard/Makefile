# Get one from http://console.developers.google.com
PROJECT_ID = com-zugaldia-appython

# Appython path
APPYTHON_ROOT = ../../../appython

# Runscope URL -- remove comments in deploy-api when this is ready
RUNSCOPE_TRIGGER = https://api.runscope.com/radar/bucket/xxxxx/trigger

#
# No need to change anything after this
#

# Software reqs
APPENGINE = /usr/local/google_appengine
BOWER = /usr/local/bin/bower
CLOSURE = /usr/local/bin/closure-compiler
PYTHON = /usr/local/bin/python
SASS = /usr/bin/sass

# https://github.com/zugaldia/scripts
LN_PLUS = /usr/local/bin/ln_plus.py
PREPARE_BUILD = /usr/local/bin/prepare_build.py

# App paths
APP_ROOT = app
MODULE_DEFAULT = $(APP_ROOT)/module_default
MODULE_API = $(APP_ROOT)/module_api

all:
	@echo See Makefile for options

#
# Preparations
#

clean-symlinks:
	cd $(MODULE_DEFAULT); rm -rf appython shared
	cd $(MODULE_API); rm -rf appython shared

add-symlinks:
	# Default module
	$(LN_PLUS) --from $(MODULE_DEFAULT) --to $(APPYTHON_ROOT)/appython
	$(LN_PLUS) --from $(MODULE_DEFAULT) --to $(APP_ROOT)/shared
	# API module
	$(LN_PLUS) --from $(MODULE_API) --to $(APPYTHON_ROOT)/appython
	$(LN_PLUS) --from $(MODULE_API) --to $(APP_ROOT)/shared

clean-bower:
	rm -rf $(MODULE_DEFAULT)/static/vendor/bower_components

add-bower: clean-bower
	cd $(MODULE_DEFAULT)/static/vendor; $(BOWER) install

#
# Executed with every run/deploy
#

prepare-dev:
	$(PREPARE_BUILD) --filename=$(APP_ROOT)/shared/config.py \
		--stage=development

prepare-prod: 
	$(PREPARE_BUILD) --filename=$(APP_ROOT)/shared/config.py \
		--stage=production --increase-build=True

#
# Default module
#

run-default: prepare-dev minify-js minify-css
	@echo "Running default module..."
	cp $(MODULE_DEFAULT)/templates/landing_dev.html \
		$(MODULE_DEFAULT)/templates/landing.html
	cd $(MODULE_DEFAULT); dev_appserver.py . \
		--require_indexes

run-default-clean: prepare-dev minify-js minify-css
	@echo "Running default module (clean)..."
	cp $(MODULE_DEFAULT)/templates/landing_dev.html \
		$(MODULE_DEFAULT)/templates/landing.html
	cd $(MODULE_DEFAULT); dev_appserver.py . \
		--clear_datastore --require_indexes

deploy-default: prepare-prod minify-js minify-css
	@echo "Deploying default module..."
	cp $(MODULE_DEFAULT)/templates/landing_prod.html \
		$(MODULE_DEFAULT)/templates/landing.html
	cd $(MODULE_DEFAULT); $(PYTHON) $(APPENGINE)/appcfg.py \
		--noauth_local_webserver --oauth2 \
		--application=$(PROJECT_ID) \
		update .

#
# Other useful commands
#

download-app:
	@echo "Downloading the app..."
	rm -rf download; mkdir -p download/module_default download/module_api
	$(PYTHON) $(APPENGINE)/appcfg.py download_app \
		--oauth2 --application=$(PROJECT_ID) --module=default --version=v1 \
		download/module_default
	$(PYTHON) $(APPENGINE)/appcfg.py download_app \
		--oauth2 --application=$(PROJECT_ID) --module=api --version=v1 \
		download/module_api

#
# API module
#

run-api: prepare-dev
	@echo "Running API module..."
	cd $(MODULE_API); dev_appserver.py api.yaml \
		--require_indexes

run-api-clean: prepare-dev
	@echo "Running API module (clean)..."
	cd $(MODULE_API); dev_appserver.py api.yaml \
		--clear_datastore --require_indexes

deploy-api: prepare-prod
	@echo "Deploying API module..."
	cd $(MODULE_API); $(PYTHON) $(APPENGINE)/appcfg.py \
		--noauth_local_webserver --oauth2 \
		--application=$(PROJECT_ID) \
		update api.yaml
	# @echo "Triggering Runscope tests..."
	# curl $(RUNSCOPE_TRIGGER) > /dev/null

#
# Minify
#

minify-js:
	$(CLOSURE) --language_in ECMASCRIPT5_STRICT \
		--compilation_level SIMPLE_OPTIMIZATIONS \
		--js=$(MODULE_DEFAULT)/static/scripts/app.js \
		--js=$(MODULE_DEFAULT)/static/scripts/controllers/main.js \
		--js_output_file=$(MODULE_DEFAULT)/static/build/app.min.js

minify-css:
	# Production
	$(SASS) --style=compressed --sourcemap=none \
		$(MODULE_DEFAULT)/static/styles/app.scss \
		$(MODULE_DEFAULT)/static/build/app.min.css
	# Development
	$(SASS) --style=expanded --sourcemap=none \
		$(MODULE_DEFAULT)/static/styles/app.scss \
		$(MODULE_DEFAULT)/static/build/app.css

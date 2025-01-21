default: help

##@ Utility
help:  ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)


loadschema: ## Load Schema onto Spanner
	@echo "Loading Schema"
	@gcloud spanner databases create typeaheaddb --instance  typeahead --ddl-file=Schema.sql

instancecreate: ## Spin up a single node Spanner instance
	@gcloud spanner instances create typeahead --description="typeahead Database" --config=regional-us-west1 --edition=ENTERPRISE --processing-units=100 --default-backup-schedule-type=NONE

instancedelete: ## Shutdown the Spanner instance
	@gcloud spanner instances delete typeahead


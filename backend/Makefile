run: ## サーバーを起動します
	rye run python3 -m backend --reload

help: ## このヘルプを表示します
	@grep -E '^[a-zA-Z0-9_-]+:.*?## ' \$(MAKEFILE_LIST) \
	| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2}'

.PHONY: run help

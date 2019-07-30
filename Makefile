
.PHONY: static
static:
	@npx tailwindcss build \
		assets/index.css \
		--config assets/tailwind.config.js \
		--output assets/css/2019.css

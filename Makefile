
.PHONY: static
static:
	@NODE_ENV=production npm run build

# 	@npx tailwindcss build \
# 		assets/index.css \
# 		--config assets/tailwind.config.js \
# 		--output assets/css/2019.css

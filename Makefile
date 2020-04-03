FAVICON := ./assets/images/dcus-2017-bw.jpg

.PHONY: favicon
favicon:
	@for size in 32 128 152 167 180 192 196 ; do \
		convert "${FAVICON}" -resize "$${size}x$${size}" "./assets/images/favicon-$${size}.png" ; \
	done
	@convert "${FAVICON}" -resize 196x196 ./favicon.ico

.PHONY: static
static:
	@NODE_ENV=production npm run build

# 	@npx tailwindcss build \
# 		assets/index.css \
# 		--config assets/tailwind.config.js \
# 		--output assets/css/2019.css

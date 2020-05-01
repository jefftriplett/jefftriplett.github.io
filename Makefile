FAVICON := ./assets/images/dcus-2017-bw.jpg


.PHONY: embedme
embedme:
	@embedme _drafts/**/*.md


.PHONY: favicon
favicon:
	@for size in 32 128 152 167 180 192 196 ; do \
		convert "${FAVICON}" -resize "$${size}x$${size}" "./assets/images/favicon-$${size}.png" ; \
	done
	@convert "${FAVICON}" -resize 196x196 ./favicon.ico


.PHONY: static
static:
 	# @NODE_ENV=production npm run build
	@npx tailwindcss build \
		src/index.css \
		--config src/tailwind.config.js \
		--output assets/css/2020.css

	@NODE_ENV=production npx postcss src/index.css -o assets/css/2020.min.css

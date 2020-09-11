FAVICON := ./assets/images/dcus-2017-bw.jpg


.PHONY: build
build:
	@jekyll build


.PHONY: embedme
embedme:
	@embedme _drafts/**/*.md


.PHONY: favicon
favicon:
	@for size in 32 128 152 167 180 192 196 ; do \
		convert "${FAVICON}" -resize "$${size}x$${size}" "./assets/images/favicon-$${size}.png" ; \
	done
	@convert "${FAVICON}" -resize 196x196 ./favicon.ico


.PHONY: lint
lint:
	@curlylint _includes/ _layouts/ _pages/ *.html


.PHONY: static
static:
	@jekyll build
	@npx tailwindcss@1.8.7 build \
		src/index.css \
		--config src/tailwind.config.js \
		--output assets/css/2020.css

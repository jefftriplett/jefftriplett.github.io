FAVICON := "./assets/images/dcus-2017-bw.jpg"
TAILWIND_CSS_VERSION := "2.0.1"


@default:
    just --list


@build:
    jekyll build


@embedme:
    npx embedme _drafts/**/*.md


@favicon:
    for size in 32 128 152 167 180 192 196 ; do \
        convert "{{FAVICON}}" -resize "${size}x${size}" "./assets/images/favicon-${size}.png" ; \
    done
    convert "{{FAVICON}}" -resize 196x196 ./favicon.ico


@lint:
    curlylint _includes/ _layouts/ _pages/ *.html


@run:
    modd


@static: build static_development static_production


@static_development:
    npx tailwindcss@{{TAILWIND_CSS_VERSION}} build \
        src/index.css \
        --config src/tailwind.config.js \
        --output assets/css/2020.development.css


@static_production:
    JEKYLL_ENV=production npx tailwindcss@{{TAILWIND_CSS_VERSION}} build \
        src/index.css \
        --config src/tailwind.config.js \
        --output assets/css/2020.css

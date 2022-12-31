FAVICON := "./assets/images/dcus-2017-bw.jpg"
TAILWIND_CSS_VERSION := "latest"

@_default:
    just --list

# installs/updates all dependencies
@bootstrap:
    docker-compose pull
    docker-compose build

# invoked by continuous integration servers to run tests
@cibuild:
    docker-compose build

# opens a console
@console:
    echo "TODO: console"

# starts app
@server *ARGS:
    just up {{ ARGS }}

# sets up a project to be used for the first time
@setup:
    echo "TODO: setup"

# runs tests
@test *ARGS:
    pytest {{ ARGS }}

# updates a project to run at its current version
@update:
    -pip install -U pip
    just pip-compile
    docker-compose pull
    -docker-compose build

# ----

@build:
    docker-compose pull
    docker-compose build
    # just build-jekyll
    # just build-static

@build-jekyll:
    jekyll build

@build-static:
    just build-taildwind development 2020.development.css
    just build-taildwind production 2020.css

@build-taildwind target='' filename='2020.css':
    echo "{{ target }} == {{ filename }}"
    JEKYLL_ENV={{ target }} npx tailwindcss@{{ TAILWIND_CSS_VERSION }} build \
        src/index.css \
        --config src/tailwind.config.js \
        --output assets/css/{{ filename }}

@bump:
    bumpver update

@clean:
    rm -rf _site

@cog:
    cog -Pr ./README.md

@down:
    docker-compose down

@embedme:
    npx embedme _drafts/**/*.md
    # TODO: https://github.com/DavidWells/markdown-magic
    # md-magic --path '**/*.md' --config ./config.file.js

@favicon:
    for size in 32 128 152 167 180 192 196 ; do \
        convert "{{ FAVICON }}" -resize "${size}x${size}" "./assets/images/favicon-${size}.png" ; \
    done
    convert "{{ FAVICON }}" -resize 196x196 ./favicon.ico

@fmt:
    just --fmt --unstable

@lint:
    black --check .
    curlylint _includes/ _layouts/ _pages/ *.html
    rustywind --dry-run .

@opengraph:
    tcardgen \
        --config=./templates/template3.config.yaml \
        -f ./font/ \
        -o ./output \
        _posts/*.md

@pip-compile:
    pip install -U -r requirements.in
    rm -rf requirements.txt
    pip-compile requirements.in

@serve *ARGS:
    just server {{ ARGS }}
    # modd

@social:
    fmcardgen --config=./src/config.yml --recursive ./_posts/

@static:
    just build

@up *ARGS:
    docker-compose up {{ ARGS }}

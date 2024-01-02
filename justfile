FAVICON := "./assets/images/dcus-2017-bw.jpg"
TAILWIND_CSS_VERSION := "latest"

@_default:
    just --list

# installs/updates all dependencies
@bootstrap:
    docker-compose pull
    docker-compose build
    python -m pip install --upgrade pre-commit

# ----

@build:
    docker-compose pull
    docker-compose build
    # just build-jekyll
    # just build-static

@build-jekyll:
    JEKYLL_ENV=production jekyll build

@build-static:
    just build-tailwind development 2024.development.css
    just build-tailwind production 2024.css

@build-tailwind target='' filename='2024.css':
    echo "{{ target }} == {{ filename }}"

    # {{ TAILWIND_CSS_VERSION }}

    JEKYLL_ENV={{ target }} bun run tailwindcss build \
        --config src/tailwind.config.js \
        --input src/index.css \
        --output assets/css/{{ filename }}

@bump:
    bumpver update

# invoked by continuous integration servers to run tests
@cibuild:
    docker-compose build

@clean:
    rm -rf _site

@cog:
    cog -Pr ./README.md

# opens a console
@console:
    echo "TODO: console"

@deploy:
    docker-compose run --rm jekyll jekyll build
    rsync -av _site/ node3.cog.gs:/srv/sites/jefftriplett.com/

@down:
    docker-compose down

@embedme:
    bunx embedme _drafts/**/*.md
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
    pre-commit run --all-files


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

@pre-commit *ARGS:
    pre-commit run {{ ARGS }} --all-files

@pull:
    docker-compose pull

@restart:
    docker-compose restart

@serve *ARGS:
    just server {{ ARGS }}
    # modd

# starts app
@server *ARGS:
    just up {{ ARGS }}

# sets up a project to be used for the first time
@setup:
    just bootstrap

@screenshots ARGS="--no-clobber":
    shot-scraper multi {{ ARGS }} ./shots.yml

@snex:
    snex run

@social:
    fmcardgen --config=./src/config.yml --recursive ./_posts/

@start +ARGS="--detach":
    just server {{ ARGS }}

@static:
    just build

@stop:
    docker-compose down

@tail:
    docker-compose logs --follow --tail 100

# runs tests
@test *ARGS:
    pytest {{ ARGS }}

@toc:
    bunx doctoc ./_drafts/semi-automate-don-t-fully-automate.md \
        --github \
        --title "## Contents"

@up *ARGS:
    docker-compose up {{ ARGS }}

# updates a project to run at its current version
@update:
    -pip install -U pip
    -just pip-compile
    -docker-compose pull
    -docker-compose build

@diff:
    -diff .editorconfig ~/.virtualenvs/webology.dev/src/webology.dev-git/.editorconfig
    -diff .gitignore ~/.virtualenvs/webology.dev/src/webology.dev-git/.gitignore
    -diff docker-compose.yml ~/.virtualenvs/webology.dev/src/webology.dev-git/docker-compose.yml
    -diff Gemfile ~/.virtualenvs/webology.dev/src/webology.dev-git/Gemfile
    -diff justfile ~/.virtualenvs/webology.dev/src/webology.dev-git/justfile

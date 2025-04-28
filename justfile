FAVICON := "./assets/images/2025-brickman.jpg"
TAILWIND_CSS_VERSION := "latest"

# displays list of available commands
@_default:
    just --list

# fetch and add game entries from backlogged.co
@add-games *ARGS:
    uv --quiet run scripts/fetch-backlogged.py {{ ARGS }}

# fetch and add tract entries (movies/TV series)
@add-tract *ARGS:
    uv --quiet run scripts/fetch-tract.py {{ ARGS }}

alias add-movies := add-tract
alias add-series := add-tract

# installs/updates all dependencies
@bootstrap:
    python -m pip install --upgrade pip uv
    # docker compose pull
    # docker compose build

# build docker containers
@build:
    docker compose pull
    docker compose build

# bump version numbers using bumpver
@bump *ARGS:
    uv --quiet run bumpver update {{ ARGS }}

# invoked by continuous integration servers to run tests
@cibuild:
    docker compose build

# remove generated files
@clean:
    rm -rf _site

# run code generation on README.md
@cog:
    cog -Pr ./README.md

# opens a console
@console:
    echo "TODO: console"

# deploy site to production server
@deploy:
    docker compose run --rm jekyll jekyll build
    rsync -av _site/ node3.cog.gs:/srv/sites/jefftriplett.com/

# stop docker containers
@down:
    docker compose down

# embed code snippets into markdown files
@embedme:
    bunx embedme _drafts/**/*.md
    # TODO: https://github.com/DavidWells/markdown-magic
    # md-magic --path '**/*.md' --config ./config.file.js

# generate favicons in various sizes
@favicon:
    for size in 32 128 152 167 180 192 196 ; do \
        convert "{{ FAVICON }}" -resize "${size}x${size}" "./assets/images/favicon-${size}.png" ; \
    done
    convert "{{ FAVICON }}" -resize 196x196 ./favicon.ico

# fetch game entries from backlogged.co
@fetch-backlogged *ARGS:
    uv --quiet run scripts/fetch-backlogged.py {{ ARGS }}

# fetch album/book covers
@fetch-covers ARGS:
    uv --quiet run scripts/fetch-covers.py {{ ARGS }}

# format justfile
@fmt:
    just --fmt --unstable

# build Jekyll site in production mode
@jekyll-build:
    JEKYLL_ENV=production jekyll build

# run pre-commit hooks/linters
@lint *ARGS:
    uv tool run --with pre-commit-uv pre-commit run {{ ARGS }} --all-files

# generate OpenGraph images for social media
@opengraph:
    tcardgen \
        --config=./templates/template3.config.yaml \
        -f ./font/ \
        -o ./output \
        _posts/*.md

# update requirements.txt from requirements.in
@lock:
    uv pip compile requirements.in --output-file requirements.txt

# pull latest docker images
@pull:
    docker compose pull

# restart docker containers
@restart:
    docker compose restart
    
# force a complete Jekyll rebuild
@rebuild:
    docker compose stop jekyll
    rm -rf _site
    docker compose up -d jekyll

# alias for server command
@serve *ARGS:
    just server {{ ARGS }}
    # modd

# starts app
@server *ARGS:
    just up {{ ARGS }}

# sets up a project to be used for the first time
@setup:
    just bootstrap

# take screenshots defined in shots.yml
@screenshots ARGS="--no-clobber":
    shot-scraper multi {{ ARGS }} ./shots.yml

# run snex server
@snex:
    snex run

# generate social media card images
@social:
    fmcardgen --config=./src/config.yml --recursive ./_posts/

# start server in detached mode
@start +ARGS="--detach":
    just server {{ ARGS }}

# alias for build
@static:
    just build

# build Tailwind CSS in both dev and production modes
@static-build:
    # npx update-browserslist-db@latest
    just tailwind-build development 2024.development.css
    just tailwind-build production 2024.css

# stop docker containers
@stop:
    docker compose down

# tail docker logs
@tail:
    docker compose logs --follow --tail 100

# build Tailwind CSS with specified target and filename
@tailwind-build target='' filename='2024.css':
    echo "{{ target }} == {{ filename }}"

    # {{ TAILWIND_CSS_VERSION }}

    JEKYLL_ENV={{ target }} bun run tailwindcss build \
        --config src/tailwind.config.js \
        --input src/index.css \
        --output assets/css/{{ filename }}

# runs tests
@test *ARGS:
    pytest {{ ARGS }}

# generate table of contents in markdown file
@toc:
    bunx doctoc ./_drafts/semi-automate-don-t-fully-automate.md \
        --github \
        --title "## Contents"

# start docker containers
@up *ARGS:
    docker compose up {{ ARGS }}

# updates a project to run at its current version
@update:
    -python -m pip install --upgrade pip uv
    -just lock
    # -docker compose pull
    # -docker compose build

# compare files with webology.dev repository
@diff:
    -diff .editorconfig ~/.virtualenvs/webology.dev/src/webology.dev-git/.editorconfig
    -diff .gitignore ~/.virtualenvs/webology.dev/src/webology.dev-git/.gitignore
    -diff docker compose.yml ~/.virtualenvs/webology.dev/src/webology.dev-git/docker compose.yml
    -diff Gemfile ~/.virtualenvs/webology.dev/src/webology.dev-git/Gemfile
    -diff justfile ~/.virtualenvs/webology.dev/src/webology.dev-git/justfile

FAVICON := "./assets/images/dcus-2017-bw.jpg"
TAILWIND_CSS_VERSION := "latest"

@_default:
    just --list

@opengraph:
    # tcardgen \
    #     -f ./font/ \
    #     -o ./output \
    #     -t ./templates/template.png \
    #     _posts/*.md

    tcardgen \
        --config=./templates/template3.config.yaml \
        -f ./font/ \
        -o ./output \
        _posts/*.md

#    tcardgen \
#        -f path/to/fontDir \
#        -o path/to/hugo/static/imgDir \
#        -t path/to/templateFile \
#        path/to/hugo/content/posts/*.md

@build:
    just build-jekyll
    just build-static

@build-jekyll:
    jekyll build

@build-static:
    just build-taildwind development 2020.development.css
    just build-taildwind production 2020.css

@build-taildwind target='' filename='2020.css':
    echo "{{target}} == {{filename}}"
    JEKYLL_ENV={{target}} npx tailwindcss@{{TAILWIND_CSS_VERSION}} build \
        src/index.css \
        --config src/tailwind.config.js \
        --output assets/css/{{filename}}

@bump:
    bumpver update

@clean:
    rm -rf _site

@embedme:
    npx embedme _drafts/**/*.md
    # TODO: https://github.com/DavidWells/markdown-magic
    # md-magic --path '**/*.md' --config ./config.file.js

@favicon:
    for size in 32 128 152 167 180 192 196 ; do \
        convert "{{FAVICON}}" -resize "${size}x${size}" "./assets/images/favicon-${size}.png" ; \
    done
    convert "{{FAVICON}}" -resize 196x196 ./favicon.ico

@lint:
    black --check .
    curlylint _includes/ _layouts/ _pages/ *.html
    rustywind --dry-run .

@pip-compile:
    pip install -U -r requirements.in
    rm -rf requirements.txt
    pip-compile requirements.in

@serve:
    modd

@social:
    fmcardgen --config=./src/config.yml --recursive ./_posts/

@static:
    just build

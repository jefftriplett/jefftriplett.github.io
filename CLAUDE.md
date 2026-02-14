# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview
Personal website built with Jekyll, featuring automated content management for games, movies, TV series, music, and products. Uses Tailwind CSS for styling and Docker for development environment.

## Build/Test/Lint Commands
- **Build**: `just build` or `just static-build` (builds Jekyll site and Tailwind CSS)
- **Serve**: `just serve` or `just server` (starts local development server)
- **Test**: `just test` (runs all tests)
- **Test (single)**: `pytest tests/test_file.py::test_function`
- **Lint**: `just lint` or `just lint --hook-stage manual` (runs pre-commit hooks)
- **Format**: `just lint` (includes ruff/ruff-format for Python)
- **Clean**: `just clean` (removes _site directory)
- **Rebuild**: `just rebuild` (force complete Jekyll rebuild)

## Content Management Commands
- **Games**: `just add-games` or `just add-backlogged` (fetches from backlogged.co)
- **Movies/TV**: `just add-tract` (aliases: `just add-movies`, `just add-series`)
- **Music**: `just add-music` (Spotify/YouTube entries)
- **Products**: `just add-products`
- **Covers**: `just add-covers` (album/book covers)
- **Note**: Always use `just add-tract` to add or update covers for movies and series (fetches from TMDB)

### Finding Missing Covers
To find and fix movies/series with missing covers:
```bash
# Find files with empty covers
grep -l "^cover:\s*$" _movies/*.md _series/*.md

# Update covers using TMDB
just add-tract _movies/2025-12-15-knives-out-2019.md
```

The `fetch-tract.py` script extracts title/year from frontmatter and searches TMDB for poster images.

## Development Environment
- **Setup**: `just bootstrap` then `just setup`
- **Python**: 3.11+ required, use `uv run` instead of `python` for scripts
- **Dependencies**: `uv pip compile requirements.in` to update requirements.txt
- **Docker**: `just up` to start, `just down` to stop containers
- **Virtual env**: Managed by direnv (see .envrc)

## Architecture & Structure
Jekyll site with content organized in collections prefixed with underscore:
- `_posts/` - Blog posts in YYYY-MM-DD-title.md format
- `_games/`, `_movies/`, `_series/` - Media content collections
- `_agents/` - Custom AI agent configurations
- `_appearances/`, `_drafts/`, `_events/` - Other content types
- `pages/` - Static pages (about, now, etc.)
- `scripts/` - Python automation scripts for content fetching
- `assets/` - Images, CSS, JavaScript files

## Code Style
- **Python**: ruff for linting/formatting (black style), reorder-python-imports
- **HTML/CSS**: djhtml/djcss with 2-space tabs
- **Tailwind**: rustywind for class ordering
- **JavaScript**: djjs formatter
- **Line endings**: Unix style with final newline
- **Git**: Avoid large file commits

## Important Restrictions
- **NEVER** attempt to load the tailwind.css file directly
- **DO NOT** open or browse content folders (_posts, _movies, _series, _games, etc.) unless specifically requested
- Use Tailwind classes directly in HTML/templates
- Content folders are prefixed with underscore (_) and should not be accessed without explicit user request

## Key Technologies
- **Jekyll**: Static site generator with Liquid templating
- **Tailwind CSS**: Utility-first CSS framework (v3.0.24)
- **Docker**: Containerized development environment
- **Just**: Command runner (see justfile for all commands)
- **Python**: Automation scripts using uv for dependency management
- **Pre-commit**: Automated code quality checks

## Deployment
- **Production**: GitHub Pages (jefftriplett.com)
- **Deploy**: `just deploy` (deploys to production)
- **CI/CD**: GitHub Actions for image optimization

## Additional Tools
- **Screenshots**: `just screenshots` (uses shots.yml configuration)
- **Favicons**: `just favicon` (generates from assets/images/2025-brickman.jpg)
- **Social cards**: `just social` or `just opengraph`
- **Table of contents**: `just toc` (generates TOC in markdown)
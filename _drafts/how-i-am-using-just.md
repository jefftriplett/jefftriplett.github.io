---
slug: "how-i-am-using-just"
title: "How I Am Using Just"
---

I have been using `casey/just` for a year or so and it fits my brain better than other tools I have used.

I have used Make going on 20+ years and I hear a lot "Just Use Make" and up until now, I mostly do.
That said, "Just Use Make" means something different to everyone that uses it and that's fine, but not what I'm looking for.
Make works best for me as a command runner, but I quickly run into quirks that are best avoided for me.
Trying to figure out how to use Make was a headache, so I switched to `just` which fits my brain better.

Recently, I was burned on a project because of the subtitles between macOS's BSD make vs. GNU make aka `gmake` if you didn't already know that.

## Getting Started

Every justfile I create starts with this snippet at the top:

```yaml
@_default:
    just --list
```

To break down what this is doing:

- the `default` command is special and gets ran when you run `just` without any command line arguments.

- the `@` is special and says to not actually print the command `just --list` to the console before showing it's output.
Pro-tip: remove the `@` when you are debugging your justfiles.

- the `--list` option will pretty print all of your command.

- the `_` is special and will hide `_default` from showing up as a command you can run.

## Reasons I use it

justfiles are enough yaml to be useful, but not enough to get in my way.
90% of what I want to do with Make is standardize how I interact with a project.

- justfiles are yaml files
- yaml are well documented for how to diff, update, and generate
- just can talk to other justfiles
- just can contain logic
- just can embed python or other languages which is nice for quick work flows
- `filefile`s are uniquely named which make searching for them on GitHub straightforward

## The Rest of the Just Story

Five or six years ago, I read [Scripts to Rule Them All][] and it's stuck out to me. A boilerplate example with just, would look like:

```yaml
@_default:
    just --list

# installs/updates all dependencies
@bootstrap:
    echo "TODO: bootstrap"

# invoked by continuous integration servers to run tests
@cibuild:
    echo "TODO: cibuild"

# opens a console
@console:
    echo "TODO: console"

# starts app
@server:
    echo "TODO: server"

# sets up a project to be used for the first time
@setup:
    echo "TODO: setup"

# runs tests
@test:
    echo "TODO: test"

# updates a project to run at its current version
@update:
    echo "TODO: update"
```

## TODO: Common things

- calling other just commands from within just

- chaining commands

    Having the ability to run `just build up test down` and switch to another project is something I use a lot to batch up a series of steps that I know may take 30 seconds or 15 minutes.

- ARGS for pytest

    ```yaml
    @test +ARGS="":
        pytest {{ARGS}}
    ```

    ```shell
    $ just test --last-failed
    ```

- alias commands

- embed Python

- some logic

- examining

    ```shell
    $ just --summary
    ```

- Running python 2 and python 3 test together

## TODO: How I'm writing my own playbooks

Recently, I added a justfile to my home folder with a goal of adding common commands that I run to it to develop more playbooks.

Playbooks are my way of documenting, remembering, and automating tasks that I find myself repeating or looking up how they work.

Even if `just` isn't your jam, build playbooks, write docs, or do what works best for you. Your future self will look back and appreciate your previous efforts.

## GitHub Actions

I have been playing around with the [setup-just][extractions/setup-just] which makes using just on GitHub Actions fairly painless.

## Alternatives

- [pyinvoke][pyinvoke/invoke] is another one my favorites because it's written in Python. pyinvoke is my goto for when I want to use subprocess or when I want a higher level of control over the commands that I'm running.
It's my goto for when application needs to control a machine and analyze the output more.

- [ninja][ninja-build/ninja] - I hear good things about ninja, but it didn't quite fit into my brain.
Check out their ["Generating Ninja files from code"](https://ninja-build.org/manual.html#_generating_ninja_files_from_code) section if that's your jam.

[Julia Evans - ninja: a simple way to do builds][julia-evans-on-ninja] is a good introduction for the curious.

- [Rush][rednafi/rush] Rush is another Python meets yaml config meets bash tool.
I used it on several projects to much success.
It's not quite as feature complete as `just`.


[casey/just]: https://github.com/casey/just
[extractions/setup-just]: https://github.com/extractions/setup-just
[julia-evans-on-ninja]: https://jvns.ca/blog/2020/10/26/ninja--a-simple-way-to-do-builds/
[ninja-build/ninja]: https://github.com/ninja-build/ninja
[pyinvoke/invoke]: https://github.com/pyinvoke/invoke
[rednafi/rush]: https://github.com/rednafi/rush
[Scripts to Rule Them All]: https://github.blog/2015-06-30-scripts-to-rule-them-all/

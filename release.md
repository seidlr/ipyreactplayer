# Fully automated

    $ ./release.sh patch

## Making an alpha release

    $ ./release.sh patch --new-version 1.0.0

# semi automated

To make a new release

```
# update ipyreactplayer/__init__.py
$ git add -u && git commit -m 'Release v1.0.0' && git tag v1.0.0 && git push upstream master v1.0.0
```

If a problem happens, and you want to keep the history clean

```
# do fix
$ git rebase -i HEAD~3
$ git tag v1.0.0 -f &&  git push upstream master v1.0.0 -f
```

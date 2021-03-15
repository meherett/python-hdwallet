# Contributing to HDWallet

First off, thanks for taking the time to contribute and
when contributing to this repository, please first discuss 
the change you wish to make via [issue](https://github.com/meherett/hdwallet/issues) 
with the owners of this repository before making a change.

## Development

To get started, just fork this repo, clone it locally, and run:

```
$ pip install -e .[tests,docs] -r requirements.txt
```

## Pull Request

Add notes for pushing your branch:

> When you are ready to generate a pull request, either for preliminary review, 
or for consideration of merging into the project you must first push your local 
topic branch back up to GitHub.

Include a note about submitting the PR:

> Once you've committed and pushed all of your changes to GitHub, go to the page 
for your fork on GitHub, select your development branch, and click the pull request 
button. If you need to make any adjustments to your pull request, just push the updates 
to your branch. Your pull request will automatically track the changes on your 
development branch and update.

```commandline
git push origin new-feature
```

- Fork the repository and make a branch for your translation.
- Ensure any install or build dependencies are removed before the end of the layer when doing a build.
- Include any relevant documentation updates

GitHub's documentation for working on pull requests is [available here](https://help.github.com/articles/about-pull-requests/).

## Testing

You can run the tests with:

```
$ pytest
```

Or use `tox` to run the complete suite against the full set of build targets, or pytest to run specific 
tests against a specific version of Python.

## License

Distributed under the [ISC](https://github.com/meherett/python-hdwallet/blob/master/LICENSE) license. See ``LICENSE`` for more information.

# prefect-mattermost

<a href="https://pypi.python.org/pypi/prefect-mattermost/" alt="PyPI Version">
    <img src="https://badge.fury.io/py/prefect-mattermost.svg" /></a>
<a href="https://github.com/rpeden/prefect-mattermost/" alt="Stars">
    <img src="https://img.shields.io/github/stars/rpeden/prefect-mattermost" /></a>
<a href="https://pepy.tech/badge/prefect-mattermost/" alt="Downloads">
    <img src="https://pepy.tech/badge/prefect-mattermost" /></a>
<a href="https://github.com/rpeden/prefect-mattermost/pulse" alt="Activity">
    <img src="https://img.shields.io/github/commit-activity/m/rpeden/prefect-mattermost" /></a>
<a href="https://github.com/rpeden/prefect-mattermost/graphs/contributors" alt="Contributors">
    <img src="https://img.shields.io/github/contributors/rpeden/prefect-mattermost" /></a>
<br>
<a href="https://prefect-community.slack.com" alt="Slack">
    <img src="https://img.shields.io/badge/slack-join_community-red.svg?logo=slack" /></a>
<a href="https://discourse.prefect.io/" alt="Discourse">
    <img src="https://img.shields.io/badge/discourse-browse_forum-red.svg?logo=discourse" /></a>

## Welcome!

Prefect Mattermost notifier.

## Getting Started

### Python setup

Requires an installation of Python 3.7+.

We recommend using a Python virtual environment manager such as pipenv, conda or virtualenv.

These tasks are designed to work with Prefect 2.0. For more information about how to use Prefect, please refer to the [Prefect documentation](https://orion-docs.prefect.io/).

### Installation

Install `prefect-mattermost` with `pip`:

```bash
pip install prefect-mattermost
```

### Write and run a flow

```python
from prefect import flow
from prefect_mattermost.tasks import (
    goodbye_prefect_mattermost,
    hello_prefect_mattermost,
)


@flow
def example_flow():
    hello_prefect_mattermost
    goodbye_prefect_mattermost

example_flow()
```

## Resources

If you encounter any bugs while using `prefect-mattermost`, feel free to open an issue in the [prefect-mattermost](https://github.com/rpeden/prefect-mattermost) repository.

If you have any questions or issues while using `prefect-mattermost`, you can find help in either the [Prefect Discourse forum](https://discourse.prefect.io/) or the [Prefect Slack community](https://prefect.io/slack).

## Development

If you'd like to install a version of `prefect-mattermost` for development, clone the repository and perform an editable install with `pip`:

```bash
git clone https://github.com/rpeden/prefect-mattermost.git

cd prefect-mattermost/

pip install -e ".[dev]"

# Install linting pre-commit hooks
pre-commit install
```

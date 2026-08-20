# P2obt
<!-- Project Shields -->
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)
![Lifecycle: production](https://img.shields.io/badge/lifecycle-production-orange.svg)
![PyPI - Version](https://img.shields.io/pypi/v/p2obt?pypiBaseUrl=https%3A%2F%2Fpypi.org)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white)](https://conventionalcommits.org)
[![Build with pixi](https://img.shields.io/badge/build-pixi-5A29E4.svg)](https://pixi.prefix.dev/latest/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/charliermarsh/ruff)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

The Phase 2 OB tool (p2obt) has been made to streamline/automate
the process of MATISSE observation (ob) preparation on ESO's p2 environment.

>[!NOTE]
> Although not currently supported, extensions to make the tool work with PIONIER,
> GRAVITY or other potential interferometric instruments at the VLTI should be possible.

More information can be found in the [**documentation**](https://mbsck.github.io/p2obt/)
and for quick access under the following links:

* [**Installation**](https://mbsck.github.io/p2obt/installation.html)
* [**Getting Started**](https://mbsck.github.io/p2obt/getting_started.html) (supplemented by scripts in the `example/` directory).

## 🚀 Installation

This package uses [`pixi`](https://pixi.prefix.dev/latest/) to manage environments
and dependencies. It’s fully compatible with `pip` but much faster,
simpler to use, and most of all highly reproducible.

### 1️⃣ Install uv

Detailled installation guides can be found [pixi-installation](https://pixi.prefix.dev/latest/installation/).

**On Linux / macOS:**

```bash
curl -fsSL https://pixi.sh/install.sh | sh
```

### 2️⃣ Install the package

```bash
pixi add --pypi p2obt
```

## Contributing

We welcome contributions of (but not limited to):

* Star or fork the repository to let us know you are using the code.
* Code or documentation should be added via [pull-request](https://github.com/mbsck/p2obt/pulls).
* To suggest/request a feature or file a bug reports, please make use of the [issue tracker](https://github.com/mbsck/p2obt/issues).

## [Credit](https://mbsck.github.io/p2obt/credit.html)

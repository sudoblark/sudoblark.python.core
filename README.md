<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/sudoblark/sudoblark.python.core">
    <img src="./docs/logo.jpg" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">sudoblark.python.core</h3>

  <p align="center">
    The core Python library for Sudoblark, mainly used to power CLI tooling to augment CI/CD operations.
    <br>
    &middot;
    <a href="https://github.com/sudoblark/sudoblark.python.core/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/sudoblark/sudoblark.python.core/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#technical-documentation">Technical Documentation</a></li>
    <li><a href="#testing">Testing</a></li>
    <li><a href="#cicd">CI/CD</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This is the core Python library for Sudoblark, mainly used to power CLI tooling
to augment CI/CD operations.

The live source of documentation may be said to reside [here](https://sudoblark.github.io/sudoblark.python.core/1.0.0). It
is recommended for developers to at least read the "Developers notes" section
before attempting to contribute to this repo.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* Library
  * [Python 3.10](https://docs.python.org/3.10/)
* Testing and quality control
  * [flake8-pyproject](https://pypi.org/project/Flake8-pyproject/)
  * [flake8](https://flake8.pycqa.org/en/latest/)
  * [behave!](https://behave.readthedocs.io/en/latest/)
* Packaging
  * [pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
* Documentation
  * [mkdocstrings-python](https://mkdocstrings.github.io/python/)
  * [mike](https://pypi.org/project/mike/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

The below are instructions for how to develop the core library,
for instructions on how to install see the <a href="#usage">Usage</a>
section instead.

### Prerequisites

These installation instructions are targeted for MacOS.

* Python3.10
    ```sh
    brew install python@3.10
    ```
* Poetry
  ```sh
  python3.10 -m venv venv
  source venv/bin/activate
  pip install -U pip setuptools
  pip install poetry
  ```

### Installation

Assume a local virtual environment, and poetry, are setup as per
the <a href="#prerequisites">Prerequisites</a> then installation
is simply:

```sh
poetry install
```

Which you may verify via:

```sh
python3
import sudoblark_python_core
help(sudoblark_python_core)
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

Install from PyPi:

```shell
pip install sudoblark-python-core
```

And off you go. More details are available via the live documentation.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- TECHNICAL DOCUMENTATION -->
## Technical Documentation

mkdocs is used in order to auto-generation documentation. It is configured via
the [docs/mkdocs.yml](./docs/mkdocs.yml) file and - for the most part - doesn't
need to be altered.

In order to generation a local web server of documentation:

```sh
mkdocs serve
```

However, it should be noted that live versioned documentation is produced via
the appropriate workflow as per the CI/CD section of this document.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Testing -->
## Testing

The Behave! library is utilised in order to conduct end-to-end testing, hopefully proving
we can actually interact in a reliable fashion with the GitHub RESTAPI.

For those uninitiated, the basic premise is:
- The [features](features) folder is the root of Behave!
- At this top-level, it contains `.feature` files, which are used to define our test cases
- In the nested `steps` folder, we will define what the test case components mean in programmatic terms

Checks may be run by simply executing `behave` locally once the `Installation` steps have been followed.

> **_NOTE:_**  All scenarios require a valid GITHUB_TOKEN environment variable to be present

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CI/CD -->
## CI/CD

GitHub Actions is used for all CI/CD activities. We give a brief outline of what
each pipeline does below.

| Pipeline                    | Triggers                    | Description                                |
|-----------------------------|-----------------------------|--------------------------------------------|
| commit-to-pull-request.yaml | Commit on a pull request    | Runs flake8 and behavioural tests          |
| release.yaml                | When a release is published | Builds and publishes docs and pypi package |


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the project_license. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
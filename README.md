<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/sudoblark/sudoblark.python.core">
    <img src="./docs/logo.jpg" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">sudoblark.python.core</h3>

  <p align="center">
    The core Python library for Sudoblark, mainly used to power <a href="todo">magpie</a>
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
    <li><a href="#cicd">CI/CD</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This is the core Python library for Sudoblark, mainly used to power [magpie]() - a CLI tooling
intended to augment CI/CD operations.

The live source of documentation may be said to reside [here](). It
is recommended for developers to at least read the "Developers notes" section
before attempting to contribute to this repo.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* Library
  * [Python 3.10](https://docs.python.org/3.10/)
* Testing and quality control
  * [PyTest 7.3](https://docs.pytest.org/en/7.3.x/)
  * [flake8-pyproject](https://pypi.org/project/Flake8-pyproject/)
  * [flake8](https://flake8.pycqa.org/en/latest/)
  * [Coverage](https://pypi.org/project/coverage/)
* Packaging
  * [pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
* Documentation
  * [mkdocstrings-python](https://mkdocstrings.github.io/python/)
* Pipelines
  * TODO

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

If you need to re-generate documentation locally, simply
run the following command:

```sh
doxygen
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

TODO

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

However, it should be noted that versioned documentation is automatically produced -
and made publicly available - via [CI/CD](#cicd). So there's no need for you to do this
unless you want to compile a local version of the docs for yourself.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CI/CD -->
## CI/CD

TODO

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the project_license. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
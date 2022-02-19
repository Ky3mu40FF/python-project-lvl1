### Hexlet tests and linter status:
[![Actions Status](https://github.com/Ky3mu40FF/python-project-lvl1/workflows/hexlet-check/badge.svg)](https://github.com/Ky3mu40FF/python-project-lvl1/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/43c2cbe52d1de56c7986/maintainability)](https://codeclimate.com/github/Ky3mu40FF/python-project-lvl1/maintainability)

![Linter Status](https://github.com/Ky3mu40FF/python-project-lvl1/workflows/code-check-linter/badge.svg)


# Description:
This project is a set of text mathematical games.

This project contains:
1. *brain-even* - Determine if a number is even
2. *brain-calc* - Calculate the proposed expression
3. *brain-gcd* - Find the Greatest Common Divisor (GCD)
4. *brain-progression* - Determine the missing element of an arithmetic progression
5. *brain-prime* - Determine if a number is prime


# Requirements:
- Python >= 3.8 (<3.8 not tested)


# Dev-requirements
- Poetry >= 1.0.0


# Install from index (TestPyPI)
Install this package using pip:
- Ubuntu:

    `python3 -m pip install --user --index-url https://test.pypi.org/simple/ ky3mu40ff-brain-games-prj==1.0.0`

asciinema record with **installation process and test gameplay**:

<a href="https://asciinema.org/a/YuLwQ8EVDF4DLHpJ37WV0oVDF" target="_blank">
    <img src="https://asciinema.org/a/YuLwQ8EVDF4DLHpJ37WV0oVDF.svg"/>
</a>


# Build and install from source:
1. Clone this repository and move to project directory
2. Install poetry: `curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -`
3. Install all dependencies: `make install`
4. Build package: `make build`
5. Install package to user environment: `make package-install`
6. Run one of the game. List of available games you can find in Description. Example: `brain-even`

asciinema record with process of **building project and installation**:

<a href="https://asciinema.org/a/O3V778z3pMHvH22StRNXtvgiq" target="_blank">
    <img src="https://asciinema.org/a/O3V778z3pMHvH22StRNXtvgiq.svg"/>
</a>


# Gameplay demos:
asciinema record with **brain-even** tests (Step 5):

<a href="https://asciinema.org/a/dAFg7iG6CBfDB7wcBLmLo4grO" target="_blank">
    <img src="https://asciinema.org/a/dAFg7iG6CBfDB7wcBLmLo4grO.svg" />
</a>

asciinema record with **brain-calc** tests (Step 6):

<a href="https://asciinema.org/a/QrwO2rXe0YyjSlRZHvtMxIWCF" target="_blank">
    <img src="https://asciinema.org/a/QrwO2rXe0YyjSlRZHvtMxIWCF.svg" />
</a>

asciinema record with **brain-gcd** tests (Step 7):

<a href="https://asciinema.org/a/DofArQ1AjNYRXubkFKKy6RVCT" target="_blank">
    <img src="https://asciinema.org/a/DofArQ1AjNYRXubkFKKy6RVCT.svg" />
</a>

asciinema record with **brain-progression** tests (Step 8):

<a href="https://asciinema.org/a/3wG4yliEVSGQJDaQEGvGwIpwy" target="_blank">
    <img src="https://asciinema.org/a/3wG4yliEVSGQJDaQEGvGwIpwy.svg" />
</a>

asciinema record with **brain-prime** tests (Step 9):

<a href="https://asciinema.org/a/EqqoectxISY7ecjz0kkdHdYpS" target="_blank">
    <img src="https://asciinema.org/a/EqqoectxISY7ecjz0kkdHdYpS.svg" />
</a>

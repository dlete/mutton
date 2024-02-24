# Ubuntu OS and packages

Have Ubuntu 16.04

Install the following packages:
```
apt-get install python3-dev
apt-get install build-essential
apt-get install libssl-dev
apt-get install libmysqlclient-dev
apt-get install libssl-dev libffi-dev     # (otherwise, the Python package cryptography fails)
apt-get install libxml2-dev libxslt1-dev  # (otherwise, the Python package lxml fails)
```


# Virtualenv

Create a virtual environment for this project.

- Install `apt-get install python3-venv`, this is necessary in Ubuntu 16.04.

- Create a virtual environment.
```python
python3 -m venv /path/to/new/virtual/environment
```

And then to use the virtual environment:
- To activate the virtual environment:
```Shell
source </path/to/new/virtual/environment>/bin/activate
```

- To deactivate the virtual environment:
```Shell
deactivate
```


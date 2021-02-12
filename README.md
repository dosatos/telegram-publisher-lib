Basic usage: https://python-poetry.org/docs/basic-usage/

```bash
virtualenv --python python3 .venv
```

```bash
$ poetry env info

Virtualenv
Python:         3.7.3
Implementation: CPython
Path:           {YOUR PATH}/telegram-publisher-lib/.venv
Valid:          True

System
Platform: darwin
OS:       posix
Python:   /Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7
```

```bash
source $(poetry env info --path)/bin/activate
```

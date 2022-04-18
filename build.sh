#!/bin/sh

if poetry run pyinstaller --onefile fedciv_lab_cli/__init__.py --name civlab ; then
    echo Build done.
elif pyinstaller --onefile fedciv_lab_cli/__init__.py --name civlab ; then
    echo Build done.
else
    echo Are you in your venv?
fi
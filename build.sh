#!/bin/sh

if pyinstaller --onefile fedciv_lab_cli/__init__.py --name civlab ; then
    echo Build done.
elif poetry run pyinstaller --onefile fedciv_lab_cli/__init__.py --name civlab ; then
    echo Build done.
else
    echo Build failed.
fi
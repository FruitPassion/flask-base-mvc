#!/bin/bash

set -e

BASEDIR="app"
HTMLDIR="$BASEDIR/view/"
CSSDIR="$BASEDIR/static/css/"
JSDIR="$BASEDIR/static/js/"


source $(poetry env info --path)/bin/activate

# Linting
echo "Applying flake8 ..." && flake8 $BASEDIR
echo "Applying DJlint linting..." && djlint $HTMLDIR/* --lint

# Beautify
echo "Applying isort ..." && isort $BASEDIR
echo "Applying black ..." && black $BASEDIR
echo "Applying css-beautify ..." && css-beautify -r $CSSDIR*
echo "Applying js-beautify ..." && js-beautify -r $JSDIR*
echo "Applying djlint reformat ..." && djlint $HTMLDIR/* --quiet --reformat
#!/bin/sh
if [ -z "$1" ]
  then
    echo "No argument supplied"
    exit
fi

echo 'making directory src/backtester/'$1
mkdir src/backtester/$1

echo 'making __init__.py'
touch src/backtester/$1/__init__.py

echo 'making controllers.py'
echo 'from flask import Blueprint, current_app, render_template' > src/backtester/$1/controllers.py
echo 'from flask_security.decorators import login_required' >> src/backtester/$1/controllers.py

echo $1" = Blueprint('"$1"', __name__, template_folder='templates')" >> src/backtester/$1/controllers.py

echo "@"$1".route('/')" >> src/backtester/$1/controllers.py
echo "@login_required" >> src/backtester/$1/controllers.py
echo "def display_index():" >> src/backtester/$1/controllers.py
echo '    return render_template("'$1'_index.html")' >> src/backtester/$1/controllers.py


echo 'making templates'
mkdir src/backtester/$1/templates

echo 'making '$1'_index.html'
touch src/backtester/$1/templates/$1_index.html

echo "app.register_blueprint("$1", url_prefix='/"$1"')" >> src/backtester/__init__.py

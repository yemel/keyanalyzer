source env/bin/activate

export DATABASE_URL="postgres://postgres:1@localhost/analyzer"

export ROOT=`pwd`
export MANAGE="python $ROOT/manage.py"

alias m=$MANAGE

RUN=$1
CURRENT=$(git rev-parse --abbrev-ref HEAD 2>&1)
CLEAN=$(git status | grep -o 'working tree clean' | head -1)
if [ "$CLEAN" != "working tree clean" ]; then
echo "🚨🚨🚨 Working directory is not clean. Please review and commit or stash dirty files. 🚨🚨🚨"
exit 1
fi
git diff --name-only --oneline --pretty="format:" $CURRENT origin/$CURRENT >/dev/null
if [ $? != 0 ] ; then
    RUNPY=$(git diff --name-only --oneline --pretty="format:" $CURRENT origin/staging | grep -o '.py' | head -1)
else
    RUNPY=$(git diff --name-only --oneline --pretty="format:" $CURRENT origin/$CURRENT | grep -o '.py' | head -1)
fi
if [ \( "$RUNPY" == ".py" \) -o \( "$RUN" == 'py' \) ]; then
    flake8 backend
    FLAKE8=$?
    if [ $FLAKE8 -ne 0 ]; then
        echo "flake8 failed"
        exit 1
    fi
    
    export MYPYPATH=./stubs; mypy backend --ignore-missing-imports --config-file backend/mypy.ini
    MYPY=$?
    if [ $MYPY -ne 0 ]; then
        echo "mypy failed"
        exit 1
    fi

    python ./backend/manage.py test
    TEST=$?
    if [ $TEST -ne 0 ]; then
        echo "Tests failed"
        exit 1
    fi
fi

echo "✨🚀✨🚀✨🚀✨🚀✨🚀✨"
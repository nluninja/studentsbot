#!/bin/bash

# StudentsBot Environment Deactivation Script

echo "🤖 Deactivating StudentsBot environment..."

# Remove alias
unalias studentsbot 2>/dev/null

# Unset project-specific environment variables
unset STUDENTSBOT_PROJECT_DIR

# Remove project from Python path
if [[ ":$PYTHONPATH:" == *":$(pwd):"* ]]; then
    export PYTHONPATH=$(echo $PYTHONPATH | sed "s|$(pwd):||g" | sed "s|:$(pwd)||g")
fi

# Deactivate virtual environment
if [[ "$VIRTUAL_ENV" != "" ]]; then
    echo "🔄 Deactivating virtual environment..."
    deactivate
fi

echo "✅ StudentsBot environment deactivated!"
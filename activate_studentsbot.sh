#!/bin/bash

# StudentsBot Environment Activation Script

echo "🤖 Activating StudentsBot environment..."

# Set project directory
export STUDENTSBOT_PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
echo "📁 Project directory: $STUDENTSBOT_PROJECT_DIR"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Install requirements
echo "📥 Installing requirements..."
pip install -r requirements.txt

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "⚠️  .env file not found. Creating from template..."
    cp .env.example .env
    echo "✏️  Please edit .env file and add your API keys"
fi

# Set environment variables
if [ -f ".env" ]; then
    echo "🔑 Loading environment variables..."
    export $(cat .env | grep -v '^#' | xargs)
fi

# Add project to Python path
export PYTHONPATH="$STUDENTSBOT_PROJECT_DIR:$PYTHONPATH"

echo "✅ StudentsBot environment activated!"
echo "💡 Run 'python bot_refactored.py' to start the bot"
echo "💡 Run 'deactivate' to exit the environment"

# Create alias for easy bot startup
alias studentsbot="python $STUDENTSBOT_PROJECT_DIR/bot_refactored.py"
echo "🚀 You can now use 'studentsbot' command to run the bot"
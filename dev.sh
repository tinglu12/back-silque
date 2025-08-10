#!/bin/bash

# FastAPI Development Server Script
# Sets PYTHONPATH to include current directory and starts the dev server

echo "🚀 Starting FastAPI development server..."
echo "📁 Working directory: $(pwd)"
echo "🔧 Setting PYTHONPATH to include current directory"

export PYTHONPATH=.
fastapi dev main.py

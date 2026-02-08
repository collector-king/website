#!/usr/bin/env python3
# Red Tiger - Backend Terminal Server

from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import sys
import os
import json

app = Flask(__name__)
CORS(app)

# Change to RedTiger-Tools directory
os.chdir(os.path.join(os.path.dirname(__file__), 'RedTiger-Tools'))

@app.route('/api/execute', methods=['POST'])
def execute_command():
    """Execute a Python command"""
    try:
        data = request.json
        command = data.get('command', '')
        
        if not command:
            return jsonify({'output': '', 'error': ''})
        
        # Execute Python command
        result = subprocess.run(
            [sys.executable, '-c', command],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        return jsonify({
            'output': result.stdout,
            'error': result.stderr,
            'returncode': result.returncode
        })
    except subprocess.TimeoutExpired:
        return jsonify({
            'output': '',
            'error': 'Command timed out (max 10 seconds)',
            'returncode': 1
        })
    except Exception as e:
        return jsonify({
            'output': '',
            'error': str(e),
            'returncode': 1
        })

@app.route('/api/startup', methods=['GET'])
def startup():
    """Load and run RedTiger.py on startup"""
    try:
        # Try to run RedTiger.py
        result = subprocess.run(
            [sys.executable, 'RedTiger.py'],
            capture_output=True,
            text=True,
            timeout=5,
            input='help\n'  # Send 'help' command
        )
        
        return jsonify({
            'output': result.stdout,
            'error': result.stderr,
            'status': 'ready'
        })
    except Exception as e:
        # If RedTiger.py fails, return menu
        return jsonify({
            'output': 'RedTiger Terminal - Type commands below\n\nAvailable commands:\n  help - Show help\n  menu - Show menu\n  exit - Exit\n',
            'error': '',
            'status': 'ready'
        })

@app.route('/api/health', methods=['GET'])
def health():
    """Health check"""
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    print("Red Tiger Backend Server starting...")
    print("Running on http://localhost:5000")
    print("Terminal available at http://localhost:5000/terminal.html")
    app.run(debug=False, host='localhost', port=5000)

import logging
import subprocess
import shlex
import os
import sys

from flask import Flask, request, jsonify

# Python 2/3 compatibility
try:
    unicode
except NameError:
    unicode = str

app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World'

@app.route('/unsafe')
def unsafe():
    """Demonstrate a command injection vulnerability."""
    cmd = request.args.get('cmd', 'echo hello')
    # Fixed B602: Use shell=False and shlex.split to prevent shell injection
    # shlex.split expects bytes in Python 2
    if sys.version_info[0] < 3 and isinstance(cmd, unicode):
        cmd = cmd.encode('utf-8')
    
    subprocess.call(shlex.split(cmd), shell=False)
    return 'Command executed'

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

if __name__ == '__main__':
    # Fixed B104: Avoid hardcoded bind to all interfaces
    # Use environment variable for host, default to localhost for safety
    host = os.environ.get('HOST', '127.0.0.1')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port)

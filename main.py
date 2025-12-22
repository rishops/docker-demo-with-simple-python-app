import logging
import subprocess

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World'

@app.route('/unsafe')
def unsafe():
    """Demonstrate a command injection vulnerability (Fixed)."""
    cmd = request.args.get('cmd', 'echo hello')
    # Fix: Validate and sanitize input, and do not use shell=True
    # strict sanitization to allow only alphanumeric and spaces
    safe_arg = "".join(c for c in cmd if c.isalnum() or c.isspace())
    subprocess.call(['echo', safe_arg], shell=False)
    return 'Command executed'

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)

import logging
import subprocess
import shlex

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World'

@app.route('/unsafe')
def unsafe():
    """Demonstrate a command injection vulnerability."""
    cmd = request.args.get('cmd', 'echo hello')
    # B602: subprocess call with shell=True identified, security issue.
    args = shlex.split(cmd)
    subprocess.call(args, shell=False)
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
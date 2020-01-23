from flask import Flask, jsonify
from ranking_resource import get_rankings

app = Flask(__name__)


@app.route('/api')
def main():
    return jsonify(get_rankings())

if __name__ == '__main__':
    app.run()
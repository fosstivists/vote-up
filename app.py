from flask import Flask, jsonify, request

app = Flask(__name__)
app.config["DEBUG"] = True


elections = [
    {
        "id": "2000",
        "name": "VIP Test Election",
        "electionDay": "2021-06-06",
        "ocdDivisionId": "ocd-division/country:us"
    },
]


@app.route('/')
def index():
    return "Hello world!"


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/api/v1/elections/all', methods=['GET'])
def api_all():
    # req = request.
    return jsonify(elections)


app.run()

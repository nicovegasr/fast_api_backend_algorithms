from flask import *

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(_):
    return make_response("Not Implemented", 501)

# app.add_url_rule("/process_files", "process_files", process_files, methods=["POST"])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)

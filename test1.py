from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def vulnerable_page():
    name = request.args.get('name', '')
    response = make_response(f"<h1>Welcome, {name}!</h1>")
    return response

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, render_template_string

app = Flask(__name__)

# Load the HTML form
@app.route("/", methods=["GET"])
def index():
    with open("index.html", "r") as file:
        html_content = file.read()
    return render_template_string(html_content)

# Handle form submission
@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    confirmation = request.form.get("confirmation")
    with open("wedding_responses.txt", "a") as file:
        file.write(f"Name: {name}, Confirmation: {confirmation}\n")
    return "<h1>Thank you! Your response has been recorded.</h1>"

if __name__ == "__main__":
    app.run(debug=True)

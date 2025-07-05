from flask import Flask, request, render_template
from controller import self_tuning_loop

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    eval_info = None
    attempts = []

    if request.method == "POST":
        user_input = request.form["user_input"]
        output, feedback, attempts = self_tuning_loop(
            user_input=user_input,
            base_prompt="You are a helpful assistant. Respond:\n\n{input}"
        )
        result = output
        eval_info = feedback

    return render_template("index.html", result=result, eval_info=eval_info, attempts=attempts)

if __name__ == "__main__":
    app.run(debug=True)
 
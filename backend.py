from flask import Flask, request, render_template , redirect , url_for


app = Flask(__name__ , template_folder=r"C:\Users\Sparsh Mahajan\OneDrive\Documents\c progams\.vscode\.vscode\backend\chat-bot\templates")

chat = []

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/submit'  , methods=[  "GET" ,  "POST"  ])
def abc():
    user=None
    ai=None
    if request.method=='POST':  
        user = request.form["text"]
        ai="hi"+user
        chat.append([user , ai])
        return redirect(url_for('abc'))
    return render_template("index.html" , ans=ai , chat= chat )

    user=None
    ai=None
    return render_template("index.html" , ans=ai , chat= request.form.get("text") )

if __name__ == "__main__":
    app.run(debug=True)

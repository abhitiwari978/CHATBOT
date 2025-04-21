from flask import Flask, render_template,request,jsonify
import backend

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/message', methods=['POST'])
def message():
    data = request.get_json()
    user_message = data.get('message')
    response=backend.reply(user_message)
    return jsonify({'reply': response})

if __name__=="__main__":
    app.run(debug=True)
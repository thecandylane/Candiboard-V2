from flask import Flask, jsonify

#app instance
app = Flask(__name__)

@app.route('/api/home', methods=['GET'])
def return_home():
    return jsonify({
        'message':'hello world'
    })

if __name__ == "__main__":
    #remove for production(debug=true)
    app.run(debug=True)
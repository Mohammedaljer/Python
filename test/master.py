from flask import Flask, jsonify, request
import random
import requests
app = Flask(__name__)
player_url = "http://localhost:8080"

numbertoguess = None
@app.route('/health')
def health():
    return 'healthy', 200

@app.route("/guess", methods=["POST","GET"])
def evaluate_guess():
   
    global numbertoguess
    
    data = request.get_json()
    guess = data["guess"]
    
    if numbertoguess is None:
        numbertoguess = random.randint(1, 1000)
    
    if numbertoguess == guess:
        numbertoguess = random.randint(1, 1000)
        response = { 
        "message": 'WIN'
        }   
    elif numbertoguess > guess:
         response = { 
            "message": 'higher' 
        }
    else: 
         response = { 
            "message": 'lower'
        }
    
    return jsonify(response), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)




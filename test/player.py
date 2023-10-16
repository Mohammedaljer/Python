from flask import Flask, jsonify, request
import requests
import random

app = Flask(__name__)
gamemaster_url = "http://localhost:4000"

@app.route('/health')
def health():
    return 'healthy', 200

@app.route('/hostname')
def hostname():
    return request.host_url , 200

@app.route("/play", methods=["POST","GET"])
def guess_number():
    try:
        
        
        history = []
        guessarray=[1,1000]
        
        
        while True:
             
             guess = random.randint(guessarray[0], guessarray[1])
             
        
             headers = {"Content-Type": "application/json"}
             response = requests.post(f"{gamemaster_url}/guess", json={"guess": guess}, headers=headers)
            
             message = response.json()["message"]

             history.append(f"Guess: {guess}, Result: {message}")
             
             if  message == "higher":
                
                guessarray = (guess + 1, guessarray[1])
             elif message == "lower":
                
                guessarray = (guessarray[0], guess - 1)
             if message == "WIN":
                break
             
        result = {
            "history": history
        }

        return jsonify(result), 200
    except (TypeError, ValueError) as e:
        error_message = {"error": str(e)}
        
        return jsonify(error_message), 400
        
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)


from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
model = genai.GenerativeModel("gemini-1.5-flash")
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv('API_KEY')
genai.configure(api_key="AIzaSyBwMZ1rSnDQyQZJuXcFVDL8rT_v85WioRg")
genai.configure(api_key=api_key) 

app = Flask(__name__)
CORS(app)  # Permite solicitudes desde cualquier origen

@app.route('/texto', methods=['POST'])
def handle_text():
    data = request.get_json()
    text = data.get('text', '')
    print(f"texto: {text}")
    response = model.generate_content(f"del siguiente texto califica la escritura, la gramatica y el sentido del mismo texto {text}")
    # Procesa el texto según sea necesario
    return jsonify({'Respuesata': response.text}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

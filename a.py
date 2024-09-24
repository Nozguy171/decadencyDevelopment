from flask import Flask, request, jsonify 
from flask_cors import CORS
import os
import google.generativeai as genai
model = genai.GenerativeModel("gemini-1.5-flash")
from dotenv import load_dotenv
from supabase import create_client, Client
import boto3

load_dotenv()
api_key = os.getenv('API_KEY')
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
AWS_AK = os.getenv('AWS_AK')
AWS_SAK = os.getenv('AWS_SAK')

supabase: Client = create_client(url, key)
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
    handel_uadio(response.text)
    return jsonify({'Respuesata': response.text}), 200

def handel_uadio(texto):
    polly = boto3.client('polly', region_name='us-east-1',aws_access_key_id=AWS_AK,aws_secret_access_key=AWS_SAK)  # Cambia a tu región preferida
    response = polly.synthesize_speech(
        Text=texto,
        OutputFormat='mp3',
        VoiceId='Lucia'
    )
    if 'AudioStream' in response:
    # Guardar el audio en un archivo temporal
        with open('output.mp3', 'wb') as file:
            file.write(response['AudioStream'].read())
        
        with open('output.mp3', 'rb') as f:
            upload_response = supabase.storage.from_("audios").upload("output.mp3", f, file_options={"content-type": "audio/mpeg"})
            print(upload_response)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

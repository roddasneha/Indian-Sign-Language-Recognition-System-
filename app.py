from flask import Flask, render_template, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/run_isl_to_audio')
def run_isl_to_audio():
    # Runs ISL to Audio/Text script in the background
    process = subprocess.Popen(['python', 'final_pred.py'])
    return jsonify({"status": "Processing ISL to Audio/Text. The result will be displayed soon."})

@app.route('/run_audio_to_isl')
def run_audio_to_isl():
    # Runs Audio to ISL script in the background
    process = subprocess.Popen(['python', 'Speech_Recognition_Hindi.py'])
    return jsonify({"status": "Processing Audio to ISL. The result will be displayed soon."})

if __name__ == '__main__':
    app.run(debug=True)

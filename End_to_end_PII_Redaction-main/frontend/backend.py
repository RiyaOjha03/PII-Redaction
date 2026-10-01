from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename
import time

# Initialize Flask app
app = Flask(__name__, static_folder='uploads')  # Static folder for file uploads
CORS(app)  # Allow cross-origin requests

# File upload configurations
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # Max file size 100MB

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Function to check if the file is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route to handle file upload and redaction
@app.route('/upload/', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"message": "No file part"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400

    if file and allowed_file(file.filename):
        # Secure and save the file
        filename = secure_filename(file.filename)
        timestamp = int(time.time())
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{timestamp}_{filename}")
        file.save(file_path)

        # Redaction Logic (can be customized)
        # Here we are just saving the same file for demo purposes
        redacted_pdf_path = file_path  # Replace this with actual redaction process

        # Generate preview and download URLs
        preview_url = f'http://127.0.0.1:5000/static/{timestamp}_{filename}'
        download_url = f'http://127.0.0.1:5000/static/{timestamp}_{filename}'

        # Return the URLs as JSON response
        return jsonify({
            "preview_url": preview_url,
            "download_url": download_url
        })

    return jsonify({"message": "Invalid file type. Only PDF files are allowed."}), 400

# Route for favicon.ico (to avoid 404)
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.getcwd(), 'favicon.ico')

# Serve static files (for PDF preview and download)
@app.route('/static/<filename>')
def serve_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Root route for homepage (index page)
@app.route('/')
def home():
    return render_template('rough3.html')  # Flask will look in the templates folder

# Start the Flask app
if __name__ == '_main_':
    app.run(debug=True)
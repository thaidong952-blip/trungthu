from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='templates')  # Giữ nguyên, nhưng thêm debug

@app.route('/')
def home():
    try:
        return render_template('index.html')
    except Exception as e:
        return f"Error: {str(e)}", 500  # Debug để log rõ lỗi

# Export cho Vercel WSGI
module = app

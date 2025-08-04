from flask import Flask, render_template
import os

# Vercelでは、index.py が起点なので templates/static の場所を明示
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, 'templates'),
    static_folder=os.path.join(BASE_DIR, 'static')
)

@app.route('/')
def home():
    return render_template('index.html')

# Vercelは app 変数をそのまま使用。app.run()は不要。
app = app
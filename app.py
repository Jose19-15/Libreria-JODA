from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    return send_from_directory('templates', 'index.html')

@app.route('/<path:path>')
def serve_file(path):
    # Sirve cualquier archivo de templates, static, icons, etc.
    import os
    if os.path.exists(f'templates/{path}'):
        return send_from_directory('templates', path)
    elif os.path.exists(f'static/{path}'):
        return send_from_directory('static', path)
    elif os.path.exists(f'icons/{path}'):
        return send_from_directory('icons', path)
    elif os.path.exists(f'logo/{path}'):
        return send_from_directory('logo', path)
    else:
        return "Archivo no encontrado", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

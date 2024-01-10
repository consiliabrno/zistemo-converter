import os
import shutil

from flask import Flask, request, render_template, send_from_directory
from werkzeug.utils import secure_filename
from convert import convert

app = Flask(__name__)
app.config['DEBUG'] = False
app.config['ENV'] = 'production'
app.config.from_object('config')

app_version = "1.0"

ALLOWED_EXTENSIONS = set(["xlsx"])

def is_allowed_file(filename: str):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def delete_output():
    folder = "static/output"
    if os.path.exists(folder):
        for file_name in os.listdir(folder):
            if (file_name != ".gitkeep"):
                file_path = os.path.join(folder, file_name)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print('Failed to delete %s. Reason: %s' % (file_path, e))

@app.route("/", methods=["GET", "POST"])
def index():
    delete_output()

    if request.method == "POST":
        file = request.files["file"]
        if file and is_allowed_file(file.filename):
            filename = secure_filename(file.filename)
            save_location = os.path.join("static/input", filename)
            file.save(save_location)
            new_file = f"converted_{filename}"
            convert(filename, new_file)
            if os.path.exists(f"static/input/{filename}"):
                os.remove(f"static/input/{filename}") 
            return send_from_directory("static/output", new_file)
    return render_template("index.jinja", version=app_version)

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)
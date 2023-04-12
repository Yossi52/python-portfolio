from flask import Flask, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap
import os
from image_process import ImageProcess


UPLOAD_FOLDER = 'static/image/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
tol = 10

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456qwerty'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000
Bootstrap(app)

filename = "demo.jpg"


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def home():
    global filename, tol
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'image.jpg'))
            tol = int(request.form.get('tolerance'))
            filename = 'image.jpg'
            return redirect(url_for('home'))
    img_process = ImageProcess(filename)
    most_color = img_process.most_color(tol)
    img_size = [img_process.resized_img.width, img_process.resized_img.height]
    return render_template('index.html', img_path=UPLOAD_FOLDER+filename, size=img_size, colors=most_color)


if __name__ == '__main__':
    app.run(debug=True)

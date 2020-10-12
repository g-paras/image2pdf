from flask import Flask, render_template, redirect, url_for, request, send_file
# from werkzeug.utils import secure_filename
from PIL import Image
import os

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/file', methods=['GET', 'POST'])
def file():
	if request.method == 'POST':
		try:
			os.remove('thispdf.pdf')
		except:
			pass
		image = request.files.getlist['images']
		image.save(image.filename)
		var = Image.open(image.filename).convert("RGB")
		var.save('thispdf.pdf')
		os.remove(image.filename)
		return send_file('thispdf.pdf')
	return redirect(url_for('index'))

if __name__ == '__main__':
	app.run(debug=True)

	# for file in images:
	# 		if file and allowed_file(file.filename):
	# 		filename = secure_filename(file.filename)
	# 		file_names.append(filename)
	# 		file.save(filename)
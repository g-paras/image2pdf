from flask import Flask, render_template, redirect, url_for, request, send_file
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
		image = request.files['images']
		image.save(image.filename)
		var = Image.open(image).convert("RGB")
		var.save('thispdf.pdf')
		os.remove(image.filename)
		return send_file('thispdf.pdf')
	return redirect(url_for('index'))

if __name__ == '__main__':
	app.run(debug=True)
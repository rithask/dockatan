from flask import Flask, render_template, request, flash, redirect
from docker_commands import *
import requests

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'super secret key'

@app.route('/', methods = ['GET', 'POST'])
def hello_world():
	if request.method == "POST":
		btn = list(request.form.to_dict())
		if btn[0] == "startBtn":
			container_name = request.form['startBtn']
			start_container(container_name)
		if btn[0] == "stopBtn":
			container_name = request.form['stopBtn']
			stop_container(container_name)
	running = list_running_container()
	exited = list_terminated_container()
	return render_template('containers.html', running=running, exited=exited)

@app.route('/containers', methods = ['GET', 'POST'])
def containers():
	if request.method == "POST":
		btn = list(request.form.to_dict())
		if btn[0] == "startBtn":
			container_name = request.form['startBtn']
			start_container(container_name)
		if btn[0] == "stopBtn":
			container_name = request.form['stopBtn']
			stop_container(container_name)
	running = list_running_container()
	exited = list_terminated_container()
	return render_template('containers.html', running=running, exited=exited)

@app.route('/images', methods=['GET', 'POST'])
def images():
	if request.method == "POST":
		image_name = f"{request.form['repo']}:{request.form['tag']}"
		if check_running_containers(image_name) == True:
			flash(f"A running container is using the image \"{image_name}\"")
		else:
			delete_image(image_name)
	images = list_images()
	return render_template('images.html', images=images)

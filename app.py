from flask import Flask, render_template, request
from docker_commands import *
import requests

app = Flask(__name__)

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

@app.route('/images')
def images():
	return render_template('images.html')


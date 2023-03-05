# Dockatan
A simple Docker management tool
- - -

## Introduction
Dockatan is a simple and lightweight Docker management tool that can be used to manage Docker containers and images. This eliminates the need to use the command line to manage Docker containers and images.

## Features
1. View the list of containers
2. View the list of images
3. Start, stop, restart, pause, unpause, kill, remove containers
4. Remove images

## Installation
1. Make sure python and pip is installed
2. Install the python packages required using `pip install -r requirements.txt`
3. Run 'flask run' to start the server

## Usage
1. Open the web browser and go to the address `http://localhost:5000/`
2. Click on the `Containers` tab to view the list of containers
3. Click on the `Images` tab to view the list of images

## Timeline
1. What was the initial stage of the project?
	- We're getting tired of using the command line to manage Docker containers and images. We want to have a simple and lightweight tool to manage Docker containers and images.
2. What stage is it now?
	- We have a simple and lightweight tool to manage Docker containers and images. We can start, stop, restart, pause, unpause, kill, remove containers and remove images.
3. How did you get there?
	- We started out by digging out and skimming through the documentations of Docker, flask and everything else that we need to use. We then started to write the code and test it out. We then started to add more features to the tool.
4. What is working/not working?
	- Everything shown in the features section is working. We have not encountered any bugs yet. But the 'Network' part of the Docker is not yet implemented.

## License
Dockatan is licensed under the MIT License. See the LICENSE file for more details.

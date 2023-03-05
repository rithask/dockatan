from datetime import datetime
import docker
import json

client = docker.from_env()


# Container commands

def list_running_container():
	container_list = []
	i = 0
	for container in client.containers.list(filters={"status": "running"}):
		container_list.append({})
		container_list[i]["name"] = container.name
		container_list[i]["image"] = container.image.tags[0]
		ports = container.ports
		container_list[i]["ports"] = list(ports.keys())
		container_list[i]["created"] = clean_time(container.attrs["Created"])

		i += 1
	return container_list

def list_terminated_container():
	container_list = []
	i = 0
	for container in client.containers.list(filters = {"status": "exited"}):
		container_list.append({})
		container_list[i]["name"] = container.name
		try:
			container_list[i]["image"] = container.image.tags[0]
		except:
			container_list[i]["image"] = "None"
		ports = container.ports
		container_list[i]["ports"] = list(ports.keys())
		container_list[i]["created"] = clean_time(container.attrs["Created"])
		
		i += 1

	return container_list

def stop_container(container_name):
	container = client.containers.get(container_name)
	container.stop()

def start_container(container_name):
	container = client.containers.get(container_name)
	container.start()

def check_container_image(image_name):
	for container in client.containers.list(all):
		if container.image.tags[0] == image_name:
			return True
	return False

def delete_container(container_name):
	container = client.containers.get(container_name)
	container.remove()


# Image commands

def list_images():
	image_list = []
	i = 0
	for image in client.images.list():
		image_list.append({})
		try:
			image_list[i]["repository"] = image.tags[0].split(":")[0]
			image_list[i]["tag"] = image.tags[0].split(":")[1]
		except:
			image_list[i]["repository"] = "None"
			image_list[i]["tag"] = "None"
		image_list[i]["id"] = image.id[7:19]
		image_list[i]["created"] = clean_time(image.attrs["Created"])
		size = int(image.attrs["Size"])/(10**6)
		image_list[i]["size"] = str(round(size,2)) + " MB"

		i += 1
	return image_list

def delete_image(image_name):
	if check_container_image(image_name) == False:
		image = client.images.get(image_name)
		image.remove()
		return True
	else:
		return False


# Extra functions

def clean_time(s):
    date,time = s.split("T")
    date_string = date +" "+time[:5]
    date_obj = datetime.strptime(date_string, "%Y-%m-%d %H:%M")
    formated_date = date_obj.strftime("%b %d %Y, %I:%M %p")
    return formated_date
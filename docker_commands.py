import datetime
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
	image_list = {}
	for image in client.images.list():
		image_list["name"] = image.tags[0]
		image_list["id"] = image.id
		
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
    k=s[:10]
    y=int(k[:4])
    m = int(k[5:7])
    d=int(k[9:10])
    x = datetime.datetime(y,m,d)
    date = x.strftime("%Y %b %d") +" "+ str(s[11:16])
    return date

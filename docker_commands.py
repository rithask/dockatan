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

# save json
def save_json(data, filename):
	with open(filename, 'w') as f:
		json.dump(data, f, indent=4)

		
# Extra functions

def clean_time(s):
    k=s[:10]
    y=int(k[:4])
    m = int(k[5:7])
    d=int(k[9:10])
    x = datetime.datetime(y,m,d)
    date = x.strftime("%Y %b %d") +" "+ str(s[11:16])
    return date

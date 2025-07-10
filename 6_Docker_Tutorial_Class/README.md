# Docker Tutorial Class

This tutorial covers basic Docker concepts, essential commands, and a practical example of running MongoDB inside a
Docker container with persistent data storage.

---

## What is Docker?

Docker is an open-source platform that automates the deployment, scaling, and management of applications inside
lightweight, portable containers. It enables developers to package applications with all their dependencies into a
standardized unit for easy development, testing, and deployment.

---

## What is a Container?

A **container** is a lightweight, standalone, and executable software package that includes everything needed to run an
application — code, runtime, system tools, libraries, and settings. Containers share the host system’s kernel but run in
isolated user spaces, ensuring applications behave consistently across different environments.

---

## Why Use Docker and Containers?

* **Portability:** Containers run consistently across different machines and environments.
* **Efficiency:** Containers are lightweight and start quickly because they share the host OS kernel.
* **Isolation:** Containers run isolated from each other, preventing conflicts.
* **Scalability:** Easily scale services by running multiple container instances.
* **Simplified DevOps:** Streamlines development, testing, and deployment workflows.
* **Resource Optimization:** More efficient than traditional virtual machines.

---

## Virtual Machines (VMs) vs Docker Containers

| Feature          | Virtual Machines                  | Docker Containers                         |
|------------------|-----------------------------------|-------------------------------------------|
| **Architecture** | Runs full OS on virtual hardware  | Runs isolated processes on host OS kernel |
| **Startup Time** | Minutes                           | Seconds                                   |
| **Resource Use** | High (separate OS instance)       | Low (shares host OS kernel)               |
| **Portability**  | Less portable, OS dependent       | Highly portable across environments       |
| **Size**         | Large (GBs)                       | Small (MBs)                               |
| **Isolation**    | Strong hardware-level isolation   | User-space isolation                      |
| **Use Cases**    | Run multiple OSes on one hardware | Package and run applications efficiently  |

---

## Docker Architecture Overview

Docker follows a **client-server architecture**:

* **Docker Client:** The CLI tool (`docker`) you use to issue commands.
* **Docker Daemon:** Background service (`dockerd`) that manages Docker objects (containers, images, volumes, networks).
* The client communicates with the daemon via REST API to build, run, and manage containers.

### Docker Images vs Containers

* **Docker Image:** A read-only template with instructions for creating a container. It bundles application code,
  libraries, dependencies, and configuration.
* **Docker Container:** A running instance of an image. Containers are isolated, executable environments.

### Docker Hub

* Public registry for sharing Docker images.
* You can **pull** images to run locally or **push** your own images for sharing.

---

## Prerequisites

* Docker installed on your machine.
* Basic knowledge of Linux shell/bash commands.

---

## Docker Service Management

Control Docker daemon using `systemctl`:

```bash
sudo systemctl enable docker       # Start Docker on boot
sudo systemctl start docker        # Start Docker daemon
sudo systemctl stop docker         # Stop Docker daemon
sudo systemctl restart docker      # Restart Docker daemon
sudo systemctl status docker       # Check Docker daemon status
```

---

## Basic Docker Commands

### Containers

* Run a container:

  ```bash
  sudo docker run -d --name <container_name> <image_name>
  ```

* List running containers:

  ```bash
  sudo docker ps
  ```

* List all containers (running + stopped):

  ```bash
  sudo docker ps -a
  ```

* Start a container:

  ```bash
  sudo docker start <container_id_or_name>
  ```

* Stop a container:

  ```bash
  sudo docker stop <container_id_or_name>
  ```

* Remove a container:

  ```bash
  sudo docker rm <container_id_or_name>
  ```

* Force stop and remove a container:

  ```bash
  sudo docker rm -f <container_id_or_name>
  ```

* Inspect container details:

  ```bash
  sudo docker inspect <container_id_or_name>
  ```

* View container logs:

  ```bash
  sudo docker logs <container_id_or_name>
  ```

### Images

* Pull image from Docker Hub:

  ```bash
  sudo docker pull <image_name>
  ```

* List local images:

  ```bash
  sudo docker images
  ```

* Remove an image (if unused):

  ```bash
  sudo docker rmi <image_id_or_name>
  ```

* Remove unused images:

  ```bash
  sudo docker image prune
  ```

---

## Running MongoDB in Docker with Data Persistence

Run a MongoDB container with persistent volume to keep data across container restarts:

```bash
sudo docker run -d \
  --name mongodb \
  -p 27017:27017 \
  -v /home/jeetendra/Container/MongoDB:/data/db \
  -e MONGO_INITDB_ROOT_USERNAME=Admin \
  -e MONGO_INITDB_ROOT_PASSWORD=Admin@1814 \
  mongo:4.4
```

* `-d`: Run container in background (detached mode)
* `--name`: Container name
* `-p`: Map container port 27017 to host port 27017
* `-v`: Mount host directory for MongoDB data persistence
* `-e`: Environment variables for root username and password

---

## Testing MongoDB Data Persistence

Access MongoDB shell inside the container:

```bash
sudo docker exec -it mongodb mongo -u Admin -p Admin@1814 --authenticationDatabase admin
```

In the MongoDB shell:

```mongodb
use testdb
db.info.insertOne({ name: "Jeetendra", status: "confirmed" })
exit
```

Alternatively, enter the container’s bash shell and then Mongo shell:

```bash
sudo docker exec -it mongodb bash
mongo --username Admin --password Admin@1814 --authenticationDatabase admin
use testdb
db.info.insertOne({ name: "Jeetendra", status: "confirmed" })
exit
exit
```

---

## Summary

* Manage Docker service lifecycle.
* Create, list, start, stop, remove containers and images.
* Understand Docker architecture and key concepts.
* Run a MongoDB container with persistent storage.
* Perform basic MongoDB operations inside Docker.

---
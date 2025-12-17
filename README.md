# Python App Docker Demo

This demo illustrates how to:
1.  Install `docker-ce` on CentOS 7.
2.  Build and run a simple Docker image with a Python, Flask, and Gunicorn web application.

## 1. Install Docker CE on CentOS 7

Refer to the official documentation: [Get Docker Engine - Community for CentOS](https://docs.docker.com/engine/installation/linux/docker-ce/centos/).
You can also find [other OS installation docs here](https://docs.docker.com/engine/installation).

### Uninstall Old Versions

```bash
sudo yum remove docker \
                docker-common \
                docker-selinux \
                docker-engine
```

### Install Using Repository

```bash
sudo yum install -y yum-utils device-mapper-persistent-data lvm2
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo yum install docker-ce
sudo systemctl start docker
sudo docker run hello-world
```

### Useful Docker Commands

*   **Check Docker status:**
    ```bash
    sudo systemctl status docker.service
    ```

*   **Stop Docker:**
    ```bash
    sudo systemctl stop docker
    ```

*   **Uninstall Docker CE:**
    ```bash
    sudo yum remove docker-ce
    ```

*   **Remove all images, containers, and volumes:**
    ```bash
    sudo rm -rf /var/lib/docker
    ```

## 2. Build and Run a Simple Python + Flask Docker Web App

### Create the Dockerfile

The `Dockerfile` defines the environment:

```dockerfile
FROM python:2.7

# Create Application Source Code Directory
RUN mkdir -p /usr/src/app

# Set Home Directory for containers
WORKDIR /usr/src/app

# Install python dependencies
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy src code to Container
COPY . /usr/src/app

# Application Environment variables
ENV PORT 8080

# Expose Ports
EXPOSE $PORT

# Set Persistent data
VOLUME ["/app-data"]

# Run Python Application
CMD gunicorn -b :$PORT -c gunicorn.conf.py main:app
```

### Build Your Image

Image naming convention is typically `{company/application-name}:{version-number}`. For this demo, we use `{application-name}:{version-number}`.

```bash
sudo docker build -t my-python-app:1.0.1 .
```

### Manage Docker Images

*   **List all Docker images:**
    ```bash
    $ sudo docker images
    REPOSITORY              TAG                 IMAGE ID            CREATED             SIZE
    my-python-app           1.0.1               2b628d11ba3a        22 minutes ago      701.6 MB
    docker.io/python        2.7                 b1d5c2d7dda8        13 days ago         679.3 MB
    docker.io/hello-world   latest              05a3bd381fc2        5 weeks ago         1.84 kB
    ```

*   **Tag an image:**
    ```bash
    # Usage: docker tag <IMAGE ID> <REPOSITORY>:<TAG>
    sudo docker tag 2b628d11ba3a my-python-app:1.0.1
    sudo docker tag 2b628d11ba3a my-python-app:latest
    ```

*   **Remove an image:**
    ```bash
    sudo docker rmi --force 2b628d11ba3a
    ```

### Run Your Image

Run the container in detached mode, mapping host port 8080 to container port 8080:

```bash
sudo docker run -d -p 8080:8080 my-python-app:1.0.1
```

### Manage Running Containers

*   **List running containers:**
    ```bash
    $ sudo docker ps
    CONTAINER ID        IMAGE                 COMMAND                  CREATED             STATUS              PORTS                    NAMES
    4de6041072b7        my-python-app:1.0.1   "/bin/sh -c 'gunicorn"   20 minutes ago      Up 20 minutes       0.0.0.0:8080->8080/tcp   elegant_kowalevski
    ```

*   **View container logs:**
    ```bash
    sudo docker logs 4de6041072b7
    ```
    *Output example:*
    ```text
    [2017-10-23 20:29:49 +0000] [7] [INFO] Starting gunicorn 19.6.0
    [2017-10-23 20:29:49 +0000] [7] [INFO] Listening at: http://0.0.0.0:8080 (7)
    ...
    ```

*   **Stop a container:**
    ```bash
    sudo docker stop 4de6041072b7
    ```

*   **Access the container shell:**
    ```bash
    sudo docker exec -it 4de6041072b7 /bin/sh
    # ls /usr/src/app
    # exit
    ```

### Test Your Application

Once the container is running:

```bash
$ curl http://localhost:8080
Hello World
```


# Dummy API Key (GitLeaks Test)
aws_secret_access_key = "AKIAIOSFODNN7EXAMPLE"

# Dummy Password in Env Format
DB_PASSWORD=SuperSecret123!

# Dummy Private Key
----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEA7X3+zYgxA0fA19yK8RT4Z7wGdpO1A4EJ1vVvZqRlDlB9NsEx
...
----END RSA PRIVATE KEY-----

# Dummy Slack Token
xoxb-123456789012-1234567890123-ABCDEFGHIJKLMNO

# Dummy JWT Token
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
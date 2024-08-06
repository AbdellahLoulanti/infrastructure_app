from flask import Flask, render_template, jsonify
import subprocess
from script import run_containers,run_docker_compose
import os

app = Flask(__name__)

START_PORT = 8080
END_PORT = 8090
PORT_FILE = 'last_port.txt'

def get_next_port():
    if not os.path.exists(PORT_FILE):
        with open(PORT_FILE, 'w') as f:
            f.write(str(START_PORT - 1))
    
    with open(PORT_FILE, 'r') as f:
        last_port = int(f.read())
    
    next_port = last_port + 1
    if next_port > END_PORT:
        next_port = START_PORT
    
    with open(PORT_FILE, 'w') as f:
        f.write(str(next_port))
    
    return next_port

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-containers', methods=['POST'])
def run_containers():
    image_name = "my-nginx-image"
    next_port = get_next_port()
    container_name = f"nginx_container_{next_port}"
    subprocess.run([
        "docker", "run", "-d", "--name", container_name, "-p", f"{next_port}:80", image_name
    ])
    return jsonify(message=f"Started container on port {next_port}.")

@app.route('/run-docker-compose', methods=['POST'])
def run_docker_compose_endpoint():
    try:
        run_docker_compose()
        return jsonify(message="Docker Compose services are running.")
    except subprocess.CalledProcessError as e:
        return jsonify(message=f"Docker Compose failed: {e}"), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

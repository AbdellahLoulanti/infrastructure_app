import subprocess

def run_containers(image_name, start_port, end_port):
    for port in range(start_port, end_port + 1):
        container_name = f"nginx_container_{port}"
        subprocess.run([
            "docker", "run", "-d", "--name", container_name, "-p", f"{port}:80", image_name
        ])
    print(f"Started containers from port {start_port} to {end_port}.")

def run_docker_compose():
    try:
        result = subprocess.run(['docker-compose', 'up', '-d'], check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(e.stdout)
        print(e.stderr)
        raise

if __name__ == "__main__":
    image_name = "my-nginx-image"
    start_port = 8080
    end_port = 8090
    run_containers(image_name, start_port, end_port)

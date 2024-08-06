# Docker Images Project

## Description

This project is a Docker-based web application that allows users to run and monitor containers using Flask and Docker Compose. The web interface provides options to start individual Nginx containers or launch a set of monitoring tools including Prometheus, Grafana, Node Exporter, and cAdvisor.

## Project Structure

- `app.py`: The main Flask application file.
- `docker_playbook.yml`: An Ansible playbook to build and run the Docker container.
- `docker-compose.yml`: Docker Compose file to set up Prometheus, Grafana, Node Exporter, cAdvisor, and Nginx services.
- `Dockerfile`: Dockerfile for building the Nginx image.
- `hosts`: Ansible hosts file.
- `last_port.txt`: File to keep track of the last used port for container deployment.
- `nginx.conf`: Nginx configuration file.
- `prometheus.yml`: Prometheus configuration file.
- `script.py`: Python script for running containers and Docker Compose.
- `templates/index.html`: HTML template for the web interface.

## Requirements

- Docker
- Docker Compose
- Python 3.x
- Flask
- Ansible (if using the playbook)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/docker-images-project.git
    cd docker-images-project
    ```

2. **Build the Docker image:**

    ```bash
    docker build -t my-nginx-image .
    ```

3. **Set up the Python environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

## Usage

### Running with Flask

1. **Start the Flask application:**

    ```bash
    python app.py
    ```

2. **Access the web interface:**
    Open your browser and go to `http://localhost:5000`.

3. **Use the interface:**
    - Click "Order" to start an Nginx container on the next available port.
    - Click "Start Monitoring" to run the monitoring stack using Docker Compose.

### Running with Docker Compose

1. **Start the services:**

    ```bash
    docker-compose up -d
    ```

2. **Access the services:**
    - Prometheus: `http://localhost:9090`
    - Grafana: `http://localhost:3001` (default login: `admin` / `admin`)
    - Nginx: `http://localhost:8080`

### Running with Ansible

1. **Run the Ansible playbook:**

    ```bash
    ansible-playbook -i hosts docker_playbook.yml
    ```

## Configuration

- **Nginx configuration:** Modify `nginx.conf` as needed.
- **Prometheus configuration:** Modify `prometheus.yml` as needed.
- **Docker Compose services:** Modify `docker-compose.yml` to add or change services.

## License

This project is licensed under the MIT License.

# 🐱 These are the instructions for building and running a Flask application that displays a random cat every time it loads.

## 📋 About the project

A simple application that:
- Runs a Flask web server
- Displays a random cat GIF from a pre-prepared list
- Updates the GIF every time the page is refreshed

## 🛠 Technologies

- Python 3.8
- Flask
- Docker
- HTML/CSS

## 🚀 Running with Docker

### Prerequisites

- Docker installed on your computer

### Steps to get started

1. Open a terminal in the project folder
2. Build the Docker image:

```bash
docker build -t flask_cat_app .
 ```
3. Run the container:

```bash
docker run -p 8866:5000 flask_cat_app
 ```
4. Open in browser:

text

http://localhost:8866

## Stopping a container
- If the container is running normally, press Ctrl+C
- If it's running in the background:
```bash
docker stop flask_cat_app
 ```

📁 Project structure
text

flask-app/
├── app.py                
├── requirements.txt     
├── Dockerfile           
├── templates/           
│   └── index.html       
└── README.md           

Enjoy using it! 🐾

# Slap - A Full-Stack Web Application

**Slap** is a custom-built website made using Flask (Python), HTML, CSS, and JavaScript. It features a MariaDB database hosted on a Virtual Machine (VM), and is deployed with Nginx on a Raspberry Pi.

## 🚀 Features

- Flask-powered backend
- Responsive frontend using HTML, CSS, and JavaScript
- Data management with MariaDB
- Hosting with Nginx on a Raspberry Pi
- Secure and lightweight deployment

---

## 🛠️ Setup Guide

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/slap.git
cd slap
```

### 2. Set Up Python Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Configure the Database

Ensure MariaDB is installed and running on your VM.

```sql
CREATE DATABASE slap_db;
CREATE USER 'slap_user'@'%' IDENTIFIED BY 'yourpassword';
GRANT ALL PRIVILEGES ON slap_db.* TO 'slap_user'@'%';
FLUSH PRIVILEGES;
```

Update the database connection settings in your Flask app (e.g., `config.py`):

```python
DB_HOST = 'your-vm-ip'
DB_USER = 'slap_user'
DB_PASSWORD = 'yourpassword'
DB_NAME = 'slap_db'
```

### 4. Run the Flask App

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

---

## 🌐 Deployment with Nginx on Raspberry Pi

### 1. Install Nginx

```bash
sudo apt update
sudo apt install nginx
```

### 2. Configure Nginx

Create a configuration file:

```bash
sudo nano /etc/nginx/sites-available/slap
```

Add the following configuration (adjust paths and domain):

```
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Enable the site and restart Nginx:

```bash
sudo ln -s /etc/nginx/sites-available/slap /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```

### 3. Enable Flask App with systemd (Optional for persistent hosting)

Create a service file:

```bash
sudo nano /etc/systemd/system/slap.service
```

```ini
[Unit]
Description=Slap Flask App
After=network.target

[Service]
User=pi
WorkingDirectory=/home/pi/slap
ExecStart=/home/pi/slap/venv/bin/python3 app.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable and start the service:

```bash
sudo systemctl daemon-reexec
sudo systemctl enable slap
sudo systemctl start slap
```

---

## 📂 Project Structure

```
slap/
├── static/
├── templates/
├── app.py
├── config.py
├── requirements.txt
└── README.md
```

## 📬 Contact

For questions or issues, feel free to open an issue or contact the project maintainer.


---

## ❓ FAQ

### Q: What is Slap?
**A:** Slap is a custom-built website made using Flask, designed to be lightweight and easily deployable on small-scale devices like a Raspberry Pi.

### Q: What technologies does Slap use?
**A:** Flask (Python), HTML, CSS, JavaScript, MariaDB (on a VM), and Nginx for hosting on a Raspberry Pi.

### Q: How do I change the database credentials?
**A:** Edit the database settings in `config.py` or wherever your connection setup is located.

### Q: How do I run this on a different machine?
**A:** Update the database host and domain configuration, then follow the setup guide to install dependencies and run the app.

### Q: Can I use MySQL instead of MariaDB?
**A:** Yes, MariaDB is a drop-in replacement for MySQL. Just ensure your SQL syntax and driver support match.

### Q: How do I access the website from another device?
**A:** Use the Raspberry Pi’s local IP or domain name (if you’ve set up DNS) to access the Flask app through Nginx.

### Q: Is there HTTPS support?
**A:** You can set up HTTPS with a free SSL certificate provider like Let’s Encrypt using `certbot` with Nginx.

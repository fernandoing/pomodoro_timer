# Pomodoro Timer Web App

A simple Pomodoro timer web application with:
- Space bar start/pause/resume
- Tracking of completed Pomodoros, skips, short breaks, and long breaks
- Persistent daily history stored in a JSON file
- Scrollable table of past days' stats

---

## 📦 1. Running Locally (No Docker)

**Requirements:**
- Python 3.9+
- `pip` (Python package manager)

**Steps:**
```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/pomodoro-app.git
cd pomodoro-app

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

The app will be available at:
**[http://localhost:5000](http://localhost:5000)**

---

## 🐳 2. Building the Docker Image Locally

```bash
# Build the image
docker build -t pomodoro-app:latest .
```

---

## 💾 3. Running with Data Persistence

We store persistent stats in `/data/stats.json` inside the container.
Mount a host directory to `/data` to keep your history across runs.

### Linux / macOS:

```bash
mkdir -p $(pwd)/pomodoro_data
docker run -d -p 5000:5000 \
  -v $(pwd)/pomodoro_data:/data \
  --name pomodoro \
  pomodoro-app:latest
```

### Windows (PowerShell):

```powershell
mkdir pomodoro_data
docker run -d -p 5000:5000 `
  -v ${PWD}\pomodoro_data:/data `
  --name pomodoro `
  pomodoro-app:latest
```

### Windows (CMD):

```cmd
mkdir pomodoro_data
docker run -d -p 5000:5000 -v %cd%\pomodoro_data:/data --name pomodoro pomodoro-app:latest
```

App will be available at:
**[http://localhost:5000](http://localhost:5000)**

---

## ☁ 4. Pushing to Docker Hub

**First time login:**

```bash
docker login
```

Enter your **Docker Hub username** and password.

**Tag your image for Docker Hub:**

```bash
docker tag pomodoro-app:latest YOUR_DOCKERHUB_USERNAME/pomodoro-app:latest
```

**Push it:**

```bash
docker push YOUR_DOCKERHUB_USERNAME/pomodoro-app:latest
```

---

## 🌍 5. Running from Docker Hub (With Persistence)

### Linux / macOS:

```bash
mkdir -p $(pwd)/pomodoro_data
docker run -d -p 5000:5000 \
  -v $(pwd)/pomodoro_data:/data \
  --name pomodoro \
  YOUR_DOCKERHUB_USERNAME/pomodoro-app:latest
```

### Windows (PowerShell):

```powershell
mkdir pomodoro_data
docker run -d -p 5000:5000 `
  -v ${PWD}\pomodoro_data:/data `
  --name pomodoro `
  YOUR_DOCKERHUB_USERNAME/pomodoro-app:latest
```

### Windows (CMD):

```cmd
mkdir pomodoro_data
docker run -d -p 5000:5000 -v %cd%\pomodoro_data:/data --name pomodoro YOUR_DOCKERHUB_USERNAME/pomodoro-app:latest
```

---

## 📜 Notes

* Data is stored in `stats.json` inside the mounted `pomodoro_data` directory.
* Newer days are shown at the top of the table in the app.
* You can stop and start the container without losing data:

```bash
docker stop pomodoro
docker start pomodoro
```

Enjoy your productivity!

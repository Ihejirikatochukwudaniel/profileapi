# Complete Setup Guide

## 📋 Table of Contents
1. [Prerequisites](#prerequisites)
2. [Project Setup](#project-setup)
3. [Local Development](#local-development)
4. [Testing](#testing)
5. [Railway Deployment](#railway-deployment)
6. [Troubleshooting](#troubleshooting)
7. [Submission Checklist](#submission-checklist)

---

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.11+** - [Download here](https://www.python.org/downloads/)
- **pip** (comes with Python)
- **Git** - [Download here](https://git-scm.com/downloads)
- **A text editor** (VS Code, PyCharm, Sublime Text, etc.)
- **Railway account** - [Sign up here](https://railway.app/)

### Verify installations:

```bash
python --version  # or python3 --version
pip --version
git --version
```

---

## Project Setup

### Step 1: Create Project Directory

```bash
mkdir backend-wizards-stage0
cd backend-wizards-stage0
```

### Step 2: Create Folder Structure

Create the following directories:

```bash
mkdir profile_api
mkdir api
```

### Step 3: Create All Files

Create these files with the content from the provided artifacts:

**Root directory files:**
- `manage.py`
- `requirements.txt`
- `Procfile`
- `runtime.txt`
- `railway.json`
- `.env.example`
- `.gitignore`
- `README.md`

**profile_api/ directory:**
- `__init__.py`
- `settings.py`
- `urls.py`
- `wsgi.py`
- `asgi.py`

**api/ directory:**
- `__init__.py`
- `apps.py`
- `models.py`
- `admin.py`
- `views.py`
- `urls.py`
- `tests.py`

### Step 4: Initialize Git Repository

```bash
git init
git add .
git commit -m "Initial commit: Backend Wizards Stage 0"
```

---

## Local Development

### Step 1: Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt.

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Create Environment File

```bash
cp .env.example .env
```

Edit `.env` file:
```env
SECRET_KEY=django-insecure-your-secret-key-change-this-123456789
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

**Generate a secure SECRET_KEY:**

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Step 4: Update Your Personal Information

Edit `api/views.py` and find the `USER_INFO` dictionary:

```python
USER_INFO = {
    "email": "yourname@example.com",  # Your actual email
    "name": "John Doe",                # Your full name
    "stack": "Python/Django"           # Your backend stack
}
```

### Step 5: Run Migrations

```bash
python manage.py migrate
```

Expected output:
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  ...
```

### Step 6: Run Development Server

```bash
python manage.py runserver
```

You should see:
```
Starting development server at http://127.0.0.1:8000/
```

### Step 7: Test the Endpoint

Open a new terminal (keep the server running) and test:

```bash
curl http://127.0.0.1:8000/me
```

Or open your browser and navigate to: `http://127.0.0.1:8000/me`

**Expected Response:**
```json
{
  "status": "success",
  "user": {
    "email": "yourname@example.com",
    "name": "John Doe",
    "stack": "Python/Django"
  },
  "timestamp": "2025-10-15T14:23:45.678Z",
  "fact": "Cats sleep 70% of their lives."
}
```

---

## Testing

### Run Unit Tests

```bash
python manage.py test
```

Expected output:
```
Creating test database...
..........
----------------------------------------------------------------------
Ran 10 tests in 0.234s

OK
Destroying test database...
```

### Manual Testing Checklist

- [ ] Endpoint returns 200 status code
- [ ] Response has correct JSON structure
- [ ] All required fields are present
- [ ] Timestamp is in ISO 8601 format
- [ ] Timestamp updates on each request
- [ ] Cat fact changes on each request
- [ ] Content-Type is application/json
- [ ] POST/PUT/DELETE return 405

---

## Railway Deployment

### Method 1: Deploy via GitHub (Recommended)

#### Step 1: Create GitHub Repository

1. Go to [GitHub](https://github.com) and create a new repository
2. Name it: `backend-wizards-stage0`
3. **Do NOT** initialize with README (you already have one)

#### Step 2: Push to GitHub

```bash
git remote add origin https://github.com/YOUR_USERNAME/backend-wizards-stage0.git
git branch -M main
git push -u origin main
```

#### Step 3: Deploy on Railway

1. Go to [Railway Dashboard](https://railway.app/dashboard)
2. Click **"New Project"**
3. Select **"Deploy from GitHub repo"**
4. Authorize Railway to access your GitHub
5. Select your `backend-wizards-stage0` repository
6. Railway will automatically detect Django and start deploying

#### Step 4: Configure Environment Variables

1. In Railway dashboard, click on your project
2. Click **"Variables"** tab
3. Add these variables:

```
SECRET_KEY=<generate-new-secret-key>
DEBUG=False
ALLOWED_HOSTS=*
```

To generate SECRET_KEY, run locally:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

#### Step 5: Generate Domain

1. Go to **"Settings"** tab
2. Scroll to **"Networking"** section
3. Click **"Generate Domain"**
4. Copy your domain (e.g., `your-app.railway.app`)

#### Step 6: Test Deployed API

```bash
curl https://your-app.railway.app/me
```

### Method 2: Deploy via Railway CLI

#### Step 1: Install Railway CLI

```bash
npm install -g @railway/cli
```

#### Step 2: Login

```bash
railway login
```

#### Step 3: Initialize Project

```bash
railway init
```

Follow prompts to create a new project.

#### Step 4: Set Environment Variables

```bash
railway variables set SECRET_KEY="your-secret-key-here"
railway variables set DEBUG=False
railway variables set ALLOWED_HOSTS="*"
```

#### Step 5: Deploy

```bash
railway up
```

#### Step 6: Get Domain

```bash
railway domain
```

#### Step 7: Test

```bash
curl https://your-railway-domain.railway.app/me
```

---

## Troubleshooting

### Common Issues

#### Issue 1: ModuleNotFoundError

**Error:**
```
ModuleNotFoundError: No module named 'django'
```

**Solution:**
```bash
# Ensure virtual environment is activated
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate      # Windows

# Reinstall dependencies
pip install -r requirements.txt
```

#### Issue 2: Port Already in Use

**Error:**
```
Error: That port is already in use.
```

**Solution:**
```bash
# Use a different port
python manage.py runserver 8080
```

#### Issue 3: ALLOWED_HOSTS Error on Railway

**Error:**
```
Invalid HTTP_HOST header: 'your-app.railway.app'
```

**Solution:**
1. Go to Railway Variables
2. Set `ALLOWED_HOSTS=*`
3. Or add specific domain: `ALLOWED_HOSTS=your-app.railway.app`

#### Issue 4: Railway Build Fails

**Error:**
```
Build failed: No such file or directory
```

**Solution:**
1. Check all files are committed to Git
2. Verify `requirements.txt` exists in root
3. Check `Procfile` and `railway.json` are in root
4. Push changes: `git push origin main`

#### Issue 5: Cat Facts API Timeout

**Error in logs:**
```
Cat Facts API request timed out
```

**Solution:**
- This is normal! The app uses a fallback message
- The API will return: "Cats are amazing creatures!"
- Check if external API is down: `curl https://catfact.ninja/fact`

#### Issue 6: 502 Bad Gateway on Railway

**Solution:**
1. Check Railway logs: `railway logs`
2. Verify `Procfile` content:
   ```
   web: gunicorn profile_api.wsgi --log-file -
   ```
3. Check if migrations ran: Add to `railway.json` buildCommand
4. Redeploy the application

---

## Submission Checklist

Before submitting, ensure you have:

### Code Requirements
- [ ] All files created with correct structure
- [ ] Personal information updated in `api/views.py`
- [ ] `.env` file NOT committed (in `.gitignore`)
- [ ] Code is clean and well-commented
- [ ] No placeholder values in USER_INFO

### Functionality
- [ ] `/me` endpoint returns 200 OK
- [ ] Response matches exact JSON schema
- [ ] All required fields present
- [ ] Timestamp in ISO 8601 format
- [ ] Timestamp updates dynamically
- [ ] Cat fact fetches from external API
- [ ] Content-Type is application/json
- [ ] Error handling works properly

### Deployment
- [ ] Code pushed to GitHub
- [ ] Deployed on Railway (NOT Vercel or Render)
- [ ] Domain is accessible publicly
- [ ] Environment variables configured
- [ ] API tested and working on live URL

### Documentation
- [ ] README.md complete with:
  - [ ] Setup instructions
  - [ ] How to run locally
  - [ ] Dependencies list
  - [ ] Environment variables needed
- [ ] GitHub repo is public
- [ ] Clear commit history

### Social Media Post
- [ ] Created post on LinkedIn/Dev.to/Medium/Hashnode/X
- [ ] Post includes:
  - [ ] Work process description
  - [ ] What you learned
  - [ ] Screenshots/images of working API
  - [ ] Link to GitHub repo
  - [ ] Link to live API

### Submission Form
- [ ] Fill out: https://forms.gle/cqXmjZwzRr4rchYBA
- [ ] Include GitHub repo link
- [ ] Include live Railway URL
- [ ] Include social media post link

---

## Quick Reference Commands

### Local Development
```bash
# Activate virtual environment
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate      # Windows

# Run server
python manage.py runserver

# Run tests
python manage.py test

# Make migrations
python manage.py makemigrations
python manage.py migrate
```

### Git Commands
```bash
# Check status
git status

# Add all files
git add .

# Commit
git commit -m "Your message"

# Push
git push origin main
```

### Railway CLI
```bash
# Login
railway login

# View logs
railway logs

# View variables
railway variables

# Deploy
railway up

# Open in browser
railway open
```

### Testing Endpoint
```bash
# Local
curl http://127.0.0.1:8000/me

# Production
curl https://your-app.railway.app/me

# Pretty print JSON
curl https://your-app.railway.app/me | python -m json.tool
```

---

## Need Help?

1. **Check Railway logs:**
   ```bash
   railway logs
   ```

2. **Check Django logs:**
   - Look in terminal where server is running
   - Check Railway deployment logs

3. **Test Cat Facts API:**
   ```bash
   curl https://catfact.ninja/fact
   ```

4. **Verify environment variables:**
   ```bash
   railway variables
   ```

---

## Success Criteria

Your API is ready for submission when:

✅ It responds correctly at `/me` endpoint
✅ Returns proper JSON with all required fields
✅ Timestamp updates on each request
✅ Cat facts are fetched dynamically
✅ Deployed and accessible on Railway
✅ GitHub repo is well-documented
✅ Social media post is published


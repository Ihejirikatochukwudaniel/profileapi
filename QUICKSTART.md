# ⚡ Quick Start Guide

Get your API running in 5 minutes!

## 🚀 Super Fast Setup

### 1. Create Project & Install (2 minutes)

```bash
# Create directory and navigate
mkdir backend-wizards-stage0 && cd backend-wizards-stage0

# Create all the folders
mkdir profile_api api

# Copy all the files from the artifacts provided
# Then create virtual environment
python -m venv venv

# Activate it
source venv/bin/activate  # macOS/Linux
# OR
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure (1 minute)

```bash
# Create .env file
cp .env.example .env

# Edit .env - use any text editor
# Change SECRET_KEY to something random

# Edit api/views.py - Update USER_INFO with your details:
# - email
# - name  
# - stack
```

### 3. Run (1 minute)

```bash
# Run migrations
python manage.py migrate

# Start server
python manage.py runserver
```

### 4. Test (30 seconds)

Open browser: http://127.0.0.1:8000/me

Or use curl:
```bash
curl http://127.0.0.1:8000/me
```

You should see your profile JSON! 🎉

---

## 🚂 Railway Deployment (5 minutes)

### Quick Deploy

```bash
# 1. Initialize git
git init
git add .
git commit -m "Initial commit"

# 2. Create GitHub repo and push
git remote add origin https://github.com/YOUR_USERNAME/backend-wizards-stage0.git
git branch -M main
git push -u origin main

# 3. Go to railway.app
# - Click "New Project"
# - Select "Deploy from GitHub repo"
# - Choose your repository
# - Add environment variables:
#   SECRET_KEY=<generate-new-one>
#   DEBUG=False
#   ALLOWED_HOSTS=*
# - Generate domain
# - Test: https://your-app.railway.app/me
```

Done! Your API is live! 🎊

---

## 📝 Files You Need

Create these files in your project with the code from the artifacts:

**Root files:**
- manage.py
- requirements.txt
- Procfile
- runtime.txt
- railway.json
- .env.example
- .gitignore
- README.md

**profile_api/ folder:**
- \_\_init\_\_.py
- settings.py
- urls.py
- wsgi.py
- asgi.py

**api/ folder:**
- \_\_init\_\_.py
- apps.py
- models.py
- admin.py
- views.py
- urls.py
- tests.py

---

## ⚠️ Don't Forget!

1. **Update YOUR info in** `api/views.py`:
   ```python
   USER_INFO = {
       "email": "YOUR_EMAIL@example.com",
       "name": "YOUR FULL NAME",
       "stack": "Python/Django"
   }
   ```

2. **Generate a SECRET_KEY** for .env:
   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

3. **Don't commit .env** (it's in .gitignore already)

4. **Test before submitting:**
   - Local: http://127.0.0.1:8000/me
   - Railway: https://your-app.railway.app/me

5. **Create social media post** about your work

6. **Submit:**
   - Form: https://forms.gle/cqXmjZwzRr4rchYBA
   - Include: GitHub link, Railway URL, social post link

---

## 🆘 Quick Fixes

**Server won't start?**
```bash
pip install -r requirements.txt
python manage.py migrate
```

**Railway not deploying?**
- Check all files are in git
- Verify Procfile and railway.json exist
- Check Railway logs

**405 Method Not Allowed?**
- Make sure you're using GET request
- /me endpoint only accepts GET

**Timestamp not updating?**
- Refresh the page or make a new request
- It should change every time

---

## ✅ Final Checklist

Before submitting:
- [ ] API works locally
- [ ] API deployed on Railway
- [ ] Your personal info updated
- [ ] GitHub repo is public
- [ ] README.md is complete
- [ ] Social media post created
- [ ] Tested live URL



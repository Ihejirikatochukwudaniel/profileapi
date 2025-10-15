# Profile API

A RESTful API endpoint that returns profile information along with a dynamic cat fact fetched from an external API.

## 🚀 Features

- **GET /me** endpoint returning profile data
- Dynamic cat fact integration from Cat Facts API
- ISO 8601 timestamp generation
- Error handling and fallback mechanisms
- CORS enabled
- Production-ready with Gunicorn and WhiteNoise

## 📋 Requirements

- Python 3.11+
- pip
- Virtual environment (recommended)

## 🛠️ Local Setup

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd backend-wizards-stage0
```

### 2. Create and activate virtual environment

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

```bash
cp .env.example .env
```

Edit `.env` file and update:
- `SECRET_KEY`: Generate a new secret key (you can use Django's get_random_secret_key())
- `DEBUG`: Set to `True` for development
- `ALLOWED_HOSTS`: Keep as `localhost,127.0.0.1` for local development

### 5. Update your personal information

Edit `api/views.py` and update the `USER_INFO` dictionary with your details:

```python
USER_INFO = {
    "email": "your.email@example.com",  # Your email
    "name": "Your Full Name",            # Your name
    "stack": "Python/Django"              # Your stack
}
```

### 6. Run migrations

```bash
python manage.py migrate
```

### 7. Run the development server

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/me`

## 🧪 Testing the Endpoint

### Using cURL

```bash
curl http://127.0.0.1:8000/me
```

### Using a web browser

Navigate to: `http://127.0.0.1:8000/me`

### Expected Response

```json
{
  "status": "success",
  "user": {
    "email": "your.email@example.com",
    "name": "Your Full Name",
    "stack": "Python/Django"
  },
  "timestamp": "2025-10-15T12:34:56.789Z",
  "fact": "A cat's purr vibrates at a frequency of 25 to 150 hertz."
}
```

## 🚂 Deploying to Railway

### Prerequisites

1. Create a [Railway](https://railway.app/) account
2. Install Railway CLI (optional but recommended)

```bash
npm install -g @railway/cli
```

### Deployment Steps

#### Option 1: Deploy via GitHub (Recommended)

1. **Push your code to GitHub**

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <your-github-repo-url>
git push -u origin main
```

2. **Connect to Railway**
   - Go to [Railway Dashboard](https://railway.app/dashboard)
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository
   - Railway will auto-detect Django and deploy

3. **Configure Environment Variables**
   - In Railway dashboard, go to your project
   - Click on "Variables" tab
   - Add the following variables:
     - `SECRET_KEY`: Generate a new secret key
     - `DEBUG`: `False`
     - `ALLOWED_HOSTS`: `*` (or your Railway domain)
     - `RAILWAY_STATIC_URL`: (Railway will set this automatically)

4. **Generate Domain**
   - Go to "Settings" tab
   - Click "Generate Domain" under "Networking"
   - Your API will be available at the generated URL + `/me`

#### Option 2: Deploy via Railway CLI

1. **Login to Railway**

```bash
railway login
```

2. **Initialize project**

```bash
railway init
```

3. **Add environment variables**

```bash
railway variables set SECRET_KEY="your-secret-key"
railway variables set DEBUG=False
railway variables set ALLOWED_HOSTS="*"
```

4. **Deploy**

```bash
railway up
```

5. **Get your domain**

```bash
railway domain
```

### Post-Deployment

1. **Test your endpoint**

```bash
curl https://your-railway-domain.railway.app/me
```

2. **Monitor logs**

In Railway dashboard or via CLI:
```bash
railway logs
```

## 📦 Dependencies

- **Django 4.2.7**: Web framework
- **requests 2.31.0**: HTTP library for external API calls
- **gunicorn 21.2.0**: WSGI HTTP server for production
- **django-cors-headers 4.3.1**: CORS handling
- **python-decouple 3.8**: Environment variable management
- **whitenoise 6.6.0**: Static file serving

## 🏗️ Project Structure

```
backend-wizards-stage0/
├── profile_api/          # Project configuration
│   ├── settings.py       # Django settings
│   ├── urls.py          # Root URL configuration
│   └── wsgi.py          # WSGI configuration
├── api/                 # API application
│   ├── views.py         # Endpoint logic
│   └── urls.py          # API URL routes
├── requirements.txt     # Python dependencies
├── Procfile            # Process configuration for deployment
├── runtime.txt         # Python version specification
├── railway.json        # Railway deployment configuration
└── README.md           # This file
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `SECRET_KEY` | Django secret key | Required |
| `DEBUG` | Debug mode | `False` |
| `ALLOWED_HOSTS` | Allowed hosts (comma-separated) | `localhost,127.0.0.1` |
| `RAILWAY_STATIC_URL` | Railway static URL | Auto-set by Railway |

### API Configuration (in `api/views.py`)

- `CAT_FACTS_API_URL`: Cat Facts API endpoint
- `API_TIMEOUT`: Timeout for external API calls (5 seconds)
- `FALLBACK_FACT`: Fallback message if API fails
- `USER_INFO`: Your personal information (email, name, stack)

## 🐛 Troubleshooting

### Local Development

**Issue: ModuleNotFoundError**
```bash
pip install -r requirements.txt
```

**Issue: Port already in use**
```bash
python manage.py runserver 8080
```

### Railway Deployment

**Issue: Application not starting**
- Check Railway logs for errors
- Ensure all environment variables are set
- Verify `requirements.txt` is complete

**Issue: 502 Bad Gateway**
- Check if the application is listening on the correct port
- Verify `Procfile` is correctly configured
- Check Railway logs for startup errors

**Issue: ALLOWED_HOSTS error**
- Add your Railway domain to `ALLOWED_HOSTS` environment variable
- Or set `ALLOWED_HOSTS=*` (not recommended for production)

## 📝 API Documentation

### GET /me

Returns profile information with a dynamic cat fact.

**Response**
- Status Code: `200 OK`
- Content-Type: `application/json`

**Response Schema**
```json
{
  "status": "success",
  "user": {
    "email": "string",
    "name": "string",
    "stack": "string"
  },
  "timestamp": "string (ISO 8601)",
  "fact": "string"
}
```

**Error Handling**
- Cat Facts API timeout: Returns fallback fact
- Cat Facts API failure: Returns fallback fact
- Server error: Returns 500 status with error message

## 🎯 Acceptance Criteria

- ✅ Working GET /me endpoint (200 OK status)
- ✅ Response follows defined JSON schema
- ✅ All required fields present (status, user, timestamp, fact)
- ✅ User object contains email, name, and stack
- ✅ Timestamp in ISO 8601 format and updates dynamically
- ✅ Cat fact fetched from Cat Facts API on every request
- ✅ Content-Type: application/json
- ✅ Well-structured code following best practices
- ✅ Proper error handling and logging
- ✅ CORS enabled
- ✅ Production-ready deployment

## 📚 Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Railway Documentation](https://docs.railway.app/)
- [Cat Facts API](https://catfact.ninja/)
- [REST API Best Practices](https://restfulapi.net/)

## 👨‍💻 Author

**Your Name**
- Email: tochukwuihejirika3@gmail.com
- GitHub: [@yourusername](https://github.com/Ihejirikatochukwudaniel)
- LinkedIn: [Your Name](https://www.linkedin.com/in/tochukwu-ihejirika-daniel-902a51203/)

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- Backend Wizards Cohort
- Cat Facts API for providing cat facts
- Railway for hosting platform
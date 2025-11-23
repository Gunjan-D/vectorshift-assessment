# VectorShift Technical Assessment - Setup & Testing Guide

## ✅ What's Been Completed

**HubSpot Integration Implementation:**
- ✅ Backend OAuth2 flow (`backend/integrations/hubspot.py`)
- ✅ Frontend React component (`frontend/src/integrations/hubspot.js`)
- ✅ API endpoints (`backend/main.py`)
- ✅ Integration mappings updated

## 🛠️ Setup Instructions

### 1. Install Prerequisites

#### Install Node.js (if not installed)
```powershell
winget install OpenJS.NodeJS.LTS
```
Or download from: https://nodejs.org/ (LTS version)

#### Install Redis for Windows
**Option 1: Memurai (Recommended for Windows)**
```powershell
winget install Memurai.Memurai-Developer
```

**Option 2: Redis for Windows**
Download from: https://github.com/tporadowski/redis/releases
- Download `Redis-x64-5.0.14.1.msi`
- Install and ensure it starts as a service

**Option 3: Docker**
```powershell
docker run -d -p 6379:6379 redis:latest
```

**Option 4: WSL (Windows Subsystem for Linux)**
```bash
sudo apt-get install redis-server
sudo service redis-server start
```

### 2. Get HubSpot OAuth Credentials

1. Go to https://developers.hubspot.com/
2. Sign up or login to your HubSpot developer account
3. Click "Create App" → "Get started"
4. Fill in basic app information:
   - App Name: "VectorShift Integration Test"
   - Description: "Testing HubSpot integration"
5. Go to "Auth" tab
6. Add Redirect URL: `http://localhost:8000/integrations/hubspot/oauth2callback`
7. Select Scopes:
   - `crm.objects.contacts.read`
   - `crm.objects.companies.read`
   - `crm.objects.deals.read`
8. Copy your **Client ID** and **Client Secret**
9. Update `backend/integrations/hubspot.py` lines 14-15:
   ```python
   CLIENT_ID = 'your-client-id-here'
   CLIENT_SECRET = 'your-client-secret-here'
   ```

### 3. Backend Setup

```powershell
# Navigate to backend directory
cd integrations_technical_assessment\backend

# Create virtual environment (recommended)
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Start Redis (if not running as service)
# Check if Redis is running:
redis-cli ping
# Should return "PONG"

# Start the backend server
uvicorn main:app --reload
```

Backend will run at: http://localhost:8000

### 4. Frontend Setup

Open a NEW terminal:

```powershell
# Navigate to frontend directory
cd integrations_technical_assessment\frontend

# Install dependencies
npm install

# Start the React app
npm start
```

Frontend will run at: http://localhost:3000

## 🧪 Testing the Integration

### Test HubSpot Integration

1. Open browser: http://localhost:3000
2. Enter User ID (e.g., "TestUser") and Organization ID (e.g., "TestOrg")
3. Select "HubSpot" from the Integration Type dropdown
4. Click "Connect to HubSpot"
5. OAuth popup window opens
6. Login to HubSpot and authorize the app
7. Window closes automatically
8. Button changes to "HubSpot Connected" (green)
9. Click "Load Data" button
10. Data should appear in the "Loaded Data" field

### Test Existing Integrations (Optional)

**Airtable:**
- Already has credentials in code (CLIENT_ID and CLIENT_SECRET)
- Should work out of the box

**Notion:**
- Requires your own CLIENT_ID and CLIENT_SECRET
- Update `backend/integrations/notion.py` lines 15-16

## 📹 Screen Recording Checklist

Record a screen recording covering:

1. **Introduction** (30 seconds)
   - "Hi, I'm Gunjan. This is my submission for the VectorShift technical assessment."

2. **Demo Functionality** (2-3 minutes)
   - Show the React app running
   - Select HubSpot integration
   - Click "Connect to HubSpot"
   - Complete OAuth flow
   - Show successful connection
   - Click "Load Data"
   - Display the loaded contacts, companies, and deals

3. **Code Walkthrough** (2-3 minutes)
   - Open `backend/integrations/hubspot.py`
   - Explain OAuth2 flow implementation
   - Show `authorize_hubspot()` function
   - Show `oauth2callback_hubspot()` function
   - Show `get_items_hubspot()` function (fetches contacts, companies, deals)
   - Open `frontend/src/integrations/hubspot.js`
   - Explain React component structure
   - Show state management and OAuth popup handling

4. **Architecture Overview** (1 minute)
   - Explain how it follows the existing Airtable/Notion pattern
   - Mention Redis for state management
   - Mention IntegrationItem data model

**Recommended Recording Tools:**
- OBS Studio (Free): https://obsproject.com/
- Loom (Free): https://loom.com/
- Windows Game Bar (Built-in): Win + G

**Save as:** `Gunjan_Deshpande_screenrecording.mp4`

## 📦 Submission Preparation

### 1. Create Zip File

```powershell
# Navigate to parent directory
cd C:\Users\gdeshpande\Downloads\automations_technical_assessment

# Create zip file (exclude node_modules and __pycache__)
Compress-Archive -Path integrations_technical_assessment\* -DestinationPath Gunjan_Deshpande_technical_assessment.zip -Force
```

**Note:** Make sure to exclude:
- `node_modules/` folder
- `__pycache__/` folders
- `venv/` folder
- `.git/` folder (if any)

### 2. Create GitHub Repository & PR

```powershell
cd integrations_technical_assessment

# Initialize git repository
git init

# Add original files
git add .
git commit -m "Initial commit: Original VectorShift assignment"

# Create GitHub repo (via GitHub website or gh CLI)
# Then add remote
git remote add origin https://github.com/YOUR_USERNAME/vectorshift-assessment.git
git branch -M main
git push -u origin main

# Create feature branch for your work
git checkout -b hubspot-integration

# Add your changes (they're already there)
git add .
git commit -m "feat: Implement HubSpot integration with OAuth2 flow and CRM data fetching"
git push -u origin hubspot-integration

# Create PR on GitHub:
# Go to: https://github.com/YOUR_USERNAME/vectorshift-assessment
# Click "Compare & pull request"
# Add description explaining your implementation
```

### 3. Submit via Form

Fill out the submission form with:
1. **Zip file:** `Gunjan_Deshpande_technical_assessment.zip`
2. **Screen recording:** `Gunjan_Deshpande_screenrecording.mp4`
3. **GitHub PR link:** Link to your pull request

## ✅ Final Checklist

Before submitting:

- [ ] Redis is running
- [ ] Backend server starts without errors
- [ ] Frontend runs without errors
- [ ] HubSpot OAuth credentials are configured
- [ ] HubSpot integration connects successfully
- [ ] Data loads from HubSpot (contacts, companies, deals)
- [ ] Screen recording is complete and clear
- [ ] Zip file is created (without node_modules)
- [ ] GitHub repository is created
- [ ] Pull request is created with clear description
- [ ] All files are submitted via the form

## 🐛 Troubleshooting

**Redis Connection Error:**
```
redis.exceptions.ConnectionError: Error connecting to Redis
```
Solution: Make sure Redis is running. Check with `redis-cli ping`

**OAuth Callback Error:**
```
State does not match
```
Solution: Redis might not be storing state. Check Redis connection.

**CORS Error in Browser:**
```
Access to XMLHttpRequest blocked by CORS policy
```
Solution: Backend should already have CORS configured. Restart backend server.

**Module Not Found (Frontend):**
```
Module not found: Can't resolve './integrations/hubspot'
```
Solution: Make sure `hubspot.js` is created in `frontend/src/integrations/`

**Import Error (Backend):**
```
ModuleNotFoundError: No module named 'fastapi'
```
Solution: Install dependencies: `pip install -r requirements.txt`

## 📞 Need Help?

If you encounter issues:
1. Check error messages in browser console (F12)
2. Check backend terminal for Python errors
3. Check Redis is running: `redis-cli ping`
4. Verify HubSpot OAuth credentials are correct

Good luck with your submission! 🚀

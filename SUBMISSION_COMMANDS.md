# Quick Submission Commands

## 📋 Pre-Submission Checklist

```powershell
# Navigate to project root
cd C:\Users\gdeshpande\Downloads\automations_technical_assessment\integrations_technical_assessment

# Make sure everything works
cd backend
uvicorn main:app --reload
# Test in browser: http://localhost:8000

# In new terminal
cd ../frontend
npm start
# Test in browser: http://localhost:3000

# Test HubSpot integration end-to-end
# Stop servers before continuing
```

## 📦 Create Submission Zip File

```powershell
# Navigate to parent directory
cd C:\Users\gdeshpande\Downloads\automations_technical_assessment

# Method 1: PowerShell (Excludes node_modules, __pycache__, etc.)
$source = "integrations_technical_assessment"
$destination = "Gunjan_Deshpande_technical_assessment.zip"

$exclude = @('node_modules', '__pycache__', '*.pyc', '.DS_Store', 'venv', '.env', '.git', 'dump.rdb', '*.log')

Get-ChildItem -Path $source -Recurse | 
    Where-Object { 
        $item = $_
        -not ($exclude | Where-Object { $item.FullName -like "*$_*" })
    } | 
    Compress-Archive -DestinationPath $destination -Force

Write-Host "Zip file created: $destination"
```

**Or simpler (but includes everything):**
```powershell
Compress-Archive -Path integrations_technical_assessment -DestinationPath Gunjan_Deshpande_technical_assessment.zip -Force
```

**Verify zip contents:**
```powershell
Expand-Archive -Path Gunjan_Deshpande_technical_assessment.zip -DestinationPath temp_verify -Force
Get-ChildItem temp_verify -Recurse
Remove-Item temp_verify -Recurse -Force
```

## 🎥 Screen Recording

**Save your recording as:** `Gunjan_Deshpande_screenrecording.mp4`

**Check file size:**
```powershell
Get-Item Gunjan_Deshpande_screenrecording.mp4 | Select-Object Name, @{Name="SizeMB";Expression={[math]::Round($_.Length/1MB,2)}}
```

## 🐙 GitHub Repository & Pull Request

### Option 1: Using GitHub CLI (if installed)

```powershell
# Navigate to project
cd integrations_technical_assessment

# Initialize git
git init

# Add all files
git add .
git commit -m "Initial commit: Original VectorShift assignment"

# Create GitHub repo
gh repo create vectorshift-assessment --public --source=. --remote=origin --push

# Create feature branch
git checkout -b hubspot-integration

# Stage changes
git add .
git commit -m "feat: Implement HubSpot integration

- Implemented OAuth2 authorization flow in backend
- Created React component for HubSpot connection
- Added HubSpot endpoints to FastAPI
- Fetches contacts, companies, and deals from HubSpot CRM
- Follows existing Airtable/Notion integration patterns"

# Push branch
git push -u origin hubspot-integration

# Create PR
gh pr create --title "Add HubSpot Integration" --body "Implements complete HubSpot integration with OAuth2 and CRM data fetching"
```

### Option 2: Using Git + GitHub Website

```powershell
# Navigate to project
cd integrations_technical_assessment

# Initialize git
git init

# Add all files
git add .
git commit -m "Initial commit: Original VectorShift assignment"

# Create repo on GitHub website first, then:
git remote add origin https://github.com/YOUR_USERNAME/vectorshift-assessment.git
git branch -M main
git push -u origin main

# Create feature branch
git checkout -b hubspot-integration
git add .
git commit -m "feat: Implement HubSpot integration"
git push -u origin hubspot-integration

# Then go to GitHub and create PR manually
```

**PR Description Template:**
```markdown
# HubSpot Integration Implementation

## Summary
Complete implementation of HubSpot integration following the existing Airtable and Notion patterns.

## Changes
- ✅ Backend OAuth2 flow (`backend/integrations/hubspot.py`)
- ✅ Frontend React component (`frontend/src/integrations/hubspot.js`)
- ✅ API endpoints in `backend/main.py`
- ✅ Integration mappings updated

## Features
- OAuth2 authorization with state validation
- Fetches Contacts, Companies, and Deals from HubSpot CRM
- Consistent with existing integration patterns
- Redis-based state management

## Testing
Tested with HubSpot developer account. Successfully:
- Completes OAuth flow
- Loads CRM data
- Displays in frontend

## Files Changed
- `backend/integrations/hubspot.py` (new)
- `frontend/src/integrations/hubspot.js` (new)
- `backend/main.py` (updated)
- `frontend/src/integration-form.js` (updated)
- `frontend/src/data-form.js` (updated)
```

## 📤 Final Submission Steps

1. **Fill out the submission form with:**
   - Zip file: `Gunjan_Deshpande_technical_assessment.zip`
   - Screen recording: `Gunjan_Deshpande_screenrecording.mp4`
   - GitHub PR link: `https://github.com/YOUR_USERNAME/vectorshift-assessment/pull/1`

2. **Verify all files:**
```powershell
Get-ChildItem | Where-Object { $_.Name -like "Gunjan_Deshpande*" }
```

3. **Double-check:**
   - [ ] Zip file contains all code
   - [ ] Screen recording plays correctly
   - [ ] GitHub PR is public and accessible
   - [ ] All three submitted via form

## 🔍 Final Verification Commands

```powershell
# Check zip file size (should be reasonable, < 50MB without node_modules)
(Get-Item Gunjan_Deshpande_technical_assessment.zip).Length / 1MB

# Check video file size (ideally < 500MB)
(Get-Item Gunjan_Deshpande_screenrecording.mp4).Length / 1MB

# List submission files
Get-ChildItem | Where-Object { $_.Name -match "Gunjan_Deshpande" } | Format-Table Name, @{Name="SizeMB";Expression={[math]::Round($_.Length/1MB,2)}}
```

## 📧 Follow-up Email (Optional)

After submitting, you can send a brief email to Albert:

**Subject:** VectorShift Technical Assessment Submission - Gunjan Deshpande

**Body:**
```
Hi Albert,

I've completed and submitted the technical assessment. Here's a quick summary:

✅ Implemented complete HubSpot integration (OAuth2 + CRM data fetching)
✅ Submitted code via form: Gunjan_Deshpande_technical_assessment.zip
✅ Submitted screen recording: Gunjan_Deshpande_screenrecording.mp4
✅ Created GitHub PR: [link]

The implementation follows the existing Airtable/Notion patterns and includes:
- Backend OAuth2 flow with Redis state management
- Frontend React component with popup OAuth
- Fetches Contacts, Companies, and Deals from HubSpot CRM

Looking forward to the next round!

Best regards,
Gunjan Deshpande
```

---

**🎯 DEADLINE: Sunday 11:59 PM IST**

Good luck! 🚀

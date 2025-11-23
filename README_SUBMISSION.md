# VectorShift Technical Assessment - HubSpot Integration

**Candidate:** Gunjan Deshpande  
**Date:** November 21, 2025  
**Assessment:** Integrations Technical Assessment

## 📝 Assignment Overview

Implement a HubSpot integration following the existing patterns for Airtable and Notion integrations, including OAuth2 authentication and CRM data fetching.

## ✅ Implementation Summary

### Backend Implementation (`backend/integrations/hubspot.py`)

**OAuth2 Authentication Flow:**
- `authorize_hubspot()` - Generates OAuth2 authorization URL with state management
- `oauth2callback_hubspot()` - Handles OAuth callback, validates state, and exchanges code for tokens
- `get_hubspot_credentials()` - Retrieves stored credentials from Redis

**Data Fetching:**
- `create_integration_item_metadata_object()` - Creates standardized IntegrationItem objects
- `get_items_hubspot()` - Fetches data from HubSpot CRM:
  - Contacts (firstname, lastname)
  - Companies (name)
  - Deals (dealname)

**Technical Details:**
- OAuth2 authorization code flow with PKCE-style state validation
- Redis-based state storage (10-minute expiry)
- HubSpot CRM API v3 integration
- Required scopes: `crm.objects.contacts.read`, `crm.objects.companies.read`, `crm.objects.deals.read`

### Frontend Implementation (`frontend/src/integrations/hubspot.js`)

**React Component Features:**
- OAuth popup window management
- Connection state tracking (disconnected → connecting → connected)
- Material-UI styled interface matching existing integrations
- Automatic credential passing to parent component
- Loading indicators and error handling

### Integration Points

**Updated Files:**
- `backend/main.py` - Fixed endpoint naming to match pattern (`/integrations/hubspot/load`)
- `frontend/src/integration-form.js` - Added HubSpot to integration mapping
- `frontend/src/data-form.js` - Added HubSpot endpoint mapping

## 🏗️ Architecture & Design Decisions

### Following Existing Patterns
I closely followed the implementation patterns from Airtable and Notion integrations to maintain consistency:

1. **State Management:** Used Redis for OAuth state storage with identical key structure
2. **Error Handling:** Consistent HTTPException patterns for validation errors
3. **Response Format:** Window-closing script after OAuth completion
4. **Data Model:** IntegrationItem class for standardized metadata

### Key Differences from Reference Integrations

**HubSpot-Specific Considerations:**
- HubSpot uses simpler OAuth2 flow (no PKCE challenge like Airtable)
- Token exchange uses form data instead of JSON body
- Multiple CRM object types (Contacts, Companies, Deals) vs single type
- Different property naming conventions per object type

### Code Quality
- Type hints for function parameters and return values
- Proper async/await patterns throughout
- Error handling with try-catch blocks in data fetching
- Clean separation of concerns (auth vs data fetching)

## 📊 Data Flow

```
User clicks "Connect to HubSpot"
    ↓
Frontend calls /integrations/hubspot/authorize
    ↓
Backend generates auth URL + stores state in Redis
    ↓
OAuth popup opens, user authorizes
    ↓
HubSpot redirects to /integrations/hubspot/oauth2callback
    ↓
Backend validates state, exchanges code for tokens
    ↓
Tokens stored in Redis, popup closes
    ↓
Frontend polls and calls /integrations/hubspot/credentials
    ↓
Credentials returned and stored in React state
    ↓
User clicks "Load Data"
    ↓
Frontend calls /integrations/hubspot/load with credentials
    ↓
Backend fetches Contacts, Companies, Deals from HubSpot API
    ↓
Data returned as list of IntegrationItem objects
    ↓
Data displayed in frontend
```

## 🔧 Technical Stack

**Backend:**
- FastAPI (Python web framework)
- Redis (State management)
- httpx (Async HTTP client)
- requests (HubSpot API calls)

**Frontend:**
- React 18.2.0
- Material-UI (@mui/material)
- Axios (HTTP client)

## 📁 File Structure

```
integrations_technical_assessment/
├── backend/
│   ├── integrations/
│   │   ├── hubspot.py          ← NEW: HubSpot integration
│   │   ├── airtable.py
│   │   ├── notion.py
│   │   └── integration_item.py
│   ├── main.py                  ← UPDATED: Added HubSpot endpoints
│   └── redis_client.py
├── frontend/
│   └── src/
│       ├── integrations/
│       │   ├── hubspot.js       ← NEW: HubSpot React component
│       │   ├── airtable.js
│       │   └── notion.js
│       ├── integration-form.js  ← UPDATED: Added HubSpot mapping
│       └── data-form.js         ← UPDATED: Added HubSpot endpoint
└── SETUP_GUIDE.md               ← NEW: Complete setup instructions
```

## 🚀 Running the Application

See `SETUP_GUIDE.md` for detailed setup instructions.

**Quick Start:**
```powershell
# Terminal 1 - Backend
cd backend
pip install -r requirements.txt
# Start Redis server first
uvicorn main:app --reload

# Terminal 2 - Frontend
cd frontend
npm install
npm start
```

**Prerequisites:**
- Python 3.8+
- Node.js 16+
- Redis server

## 🎯 Testing Instructions

1. Configure HubSpot OAuth credentials in `backend/integrations/hubspot.py`
2. Start Redis, Backend, and Frontend
3. Navigate to http://localhost:3000
4. Select "HubSpot" from dropdown
5. Click "Connect to HubSpot" and authorize
6. Click "Load Data" to fetch CRM data

## 💡 Future Enhancements

If given more time, I would implement:

1. **Pagination:** Handle large datasets with HubSpot's pagination
2. **Refresh Tokens:** Implement token refresh for long-term access
3. **Error Recovery:** More granular error messages and retry logic
4. **Data Filtering:** Allow users to select which object types to fetch
5. **Caching:** Cache API responses to reduce redundant calls
6. **Unit Tests:** Add pytest tests for backend functions
7. **Type Safety:** Add TypeScript to frontend for better type checking

## 📞 Contact

**Gunjan Deshpande**  
GitHub: [Your GitHub Profile]  
Email: [Your Email]

---

Thank you for considering my application. I look forward to discussing this implementation in the next interview round!

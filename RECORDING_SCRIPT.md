# Screen Recording Script - VectorShift Assessment

**Duration Target:** 5-7 minutes  
**File Name:** `Gunjan_Deshpande_screenrecording.mp4`

---

## 🎬 Recording Checklist

Before you start:
- [ ] Close unnecessary applications
- [ ] Clear browser cookies/cache
- [ ] Restart backend and frontend servers
- [ ] Have HubSpot test account ready
- [ ] Test microphone audio
- [ ] Open all code files in VS Code

---

## 📝 Script Outline

### PART 1: Introduction (30 seconds)

**Say:**
> "Hi, I'm Gunjan Deshpande. This is my submission for the VectorShift technical assessment. I've implemented a complete HubSpot integration following the existing patterns for Airtable and Notion. Let me walk you through the functionality and code."

**Show:**
- Your desktop with browser and VS Code ready

---

### PART 2: Functionality Demo (2-3 minutes)

#### Step 1: Show the Application Running
**Say:**
> "First, let me show you the application. I have the backend FastAPI server running on port 8000, and the React frontend on port 3000."

**Show:**
- Terminal 1: Backend running (`uvicorn main:app --reload`)
- Terminal 2: Frontend running (`npm start`)
- Browser: http://localhost:3000

#### Step 2: Configure Integration
**Say:**
> "The interface allows users to enter their User ID and Organization ID, then select an integration type. I'll select HubSpot, which is the integration I implemented."

**Do:**
- Type "TestUser" in User field
- Type "TestOrg" in Organization field
- Select "HubSpot" from dropdown

#### Step 3: OAuth Flow
**Say:**
> "When I click 'Connect to HubSpot', the application initiates an OAuth2 authorization flow. A popup window opens with HubSpot's authorization page."

**Do:**
- Click "Connect to HubSpot" button
- **POPUP APPEARS** - Login to HubSpot (if not logged in)
- Click "Authorize" on HubSpot page
- **POPUP CLOSES** automatically

**Say:**
> "After authorization, the popup closes automatically, and you can see the button changes to 'HubSpot Connected' in green, indicating successful authentication."

**Show:**
- Button now shows "HubSpot Connected" (green)

#### Step 4: Load Data
**Say:**
> "Now I can fetch data from HubSpot. When I click 'Load Data', the application retrieves contacts, companies, and deals from the HubSpot CRM API."

**Do:**
- Click "Load Data" button
- Wait for data to appear

**Say:**
> "As you can see, the data has been successfully loaded. This includes all contacts, companies, and deals from my HubSpot test account, formatted as IntegrationItem objects."

**Show:**
- Data displayed in the "Loaded Data" text field

---

### PART 3: Code Walkthrough (3-4 minutes)

#### Backend Code (`backend/integrations/hubspot.py`)

**Say:**
> "Now let me walk through the implementation. I'll start with the backend code in hubspot.py."

**Show in VS Code:**

1. **File Overview**
   > "This file follows the same pattern as the existing Airtable and Notion integrations. I've implemented five main functions."

2. **authorize_hubspot() function (lines ~19-28)**
   > "The authorize_hubspot function generates the OAuth authorization URL. It creates a unique state token for CSRF protection, stores it in Redis with a 10-minute expiry, and returns the authorization URL that the frontend will open in a popup."

   **Highlight:**
   ```python
   state_data = {
       'state': secrets.token_urlsafe(32),
       'user_id': user_id,
       'org_id': org_id
   }
   ```

3. **oauth2callback_hubspot() function (lines ~30-64)**
   > "When HubSpot redirects back, this callback function validates the state parameter against what we stored in Redis. If valid, it exchanges the authorization code for an access token using HubSpot's token endpoint."

   **Highlight:**
   ```python
   if not saved_state or original_state != json.loads(saved_state).get('state'):
       raise HTTPException(status_code=400, detail='State does not match.')
   ```

4. **get_items_hubspot() function (lines ~87-end)**
   > "This function fetches data from three HubSpot CRM endpoints: contacts, companies, and deals. It makes parallel requests and transforms each response into our standardized IntegrationItem format."

   **Highlight:**
   ```python
   # Fetch Contacts
   contacts_response = requests.get(
       'https://api.hubapi.com/crm/v3/objects/contacts',
       headers=headers,
   )
   ```

5. **create_integration_item_metadata_object() function (lines ~73-85)**
   > "This helper function creates IntegrationItem objects. It handles the different property names for each object type - firstname/lastname for contacts, name for companies, and dealname for deals."

#### Frontend Code (`frontend/src/integrations/hubspot.js`)

**Say:**
> "Now the frontend implementation. This is a React component that manages the OAuth flow from the user's perspective."

**Show in VS Code:**

1. **Component Structure**
   > "The HubSpotIntegration component uses React hooks for state management. It tracks whether we're connected and whether a connection is in progress."

   **Highlight:**
   ```javascript
   const [isConnected, setIsConnected] = useState(false);
   const [isConnecting, setIsConnecting] = useState(false);
   ```

2. **handleConnectClick function (lines ~15-33)**
   > "When the user clicks Connect, we call the backend authorize endpoint, open the OAuth URL in a popup window, and poll to detect when the popup closes."

   **Highlight:**
   ```javascript
   const newWindow = window.open(authURL, 'HubSpot Authorization', 'width=600, height=600');
   
   const pollTimer = window.setInterval(() => {
       if (newWindow?.closed !== false) { 
           window.clearInterval(pollTimer);
           handleWindowClosed();
       }
   }, 200);
   ```

3. **handleWindowClosed function (lines ~36-53)**
   > "After the popup closes, we retrieve the credentials from the backend and update the component state. The credentials are passed up to the parent component for use in data loading."

#### Integration Points

**Say:**
> "Finally, I updated three files to integrate HubSpot into the application."

**Show quickly:**

1. **main.py (lines ~60-68)**
   > "Added the HubSpot endpoints to the FastAPI router, following the same pattern as Airtable and Notion."

2. **integration-form.js (line ~5-9)**
   > "Added HubSpot to the integration mapping so it appears in the dropdown."

3. **data-form.js (line ~11-14)**
   > "Added the HubSpot endpoint mapping for the Load Data functionality."

---

### PART 4: Architecture Summary (30 seconds)

**Say:**
> "To summarize the architecture: The frontend initiates OAuth through the backend, which manages state in Redis. After authorization, credentials are stored temporarily in Redis. When loading data, the frontend sends credentials to the backend, which calls HubSpot's CRM API and returns standardized IntegrationItem objects."

**Show:**
- README_SUBMISSION.md with the data flow diagram (optional)

**Say:**
> "This implementation maintains consistency with existing integrations while handling HubSpot's specific OAuth flow and CRM data structures. Thank you for watching, and I look forward to discussing this in the next round!"

---

## 🎯 Recording Tips

1. **Pace yourself** - Speak clearly and not too fast
2. **Show, don't just tell** - Highlight relevant code sections
3. **Test run first** - Do a practice recording
4. **Check audio** - Make sure your voice is clear
5. **Edit if needed** - You can trim the beginning/end
6. **Keep it under 8 minutes** - Respect reviewer's time

## 🛠️ Recommended Recording Tools

- **OBS Studio** (Free, professional): https://obsproject.com/
- **Loom** (Easy, browser-based): https://loom.com/
- **Windows Game Bar** (Built-in): Press Win + G

## ✅ Before Submitting

- [ ] Recording is clear (video and audio)
- [ ] All features are demonstrated
- [ ] Code walkthrough is complete
- [ ] File name is correct: `Gunjan_Deshpande_screenrecording.mp4`
- [ ] File size is reasonable (< 500MB if possible)

---

Good luck! 🚀

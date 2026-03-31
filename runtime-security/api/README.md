# Runtime API 


### Minimal Viable Environment

#### Environment

Prisma AIRs Runtime API is very flexible and can adapt to all code bases that are capable of making a calls to a REST API.

- If you are looking to protect/analyse input to your AI, then we can ingest the prompt and give a verdict.
- If you are looking to protect/analyse output from your AI, then we can ingest the output and give a verdict.

#### Targets

- Any codebase
- Python SDK
- n8n - integration 
- litellm - integration

-----


### Prerequisites

1. Create and associate a deployment profile for Prisma AIRS AI Runtime API intercept in your Customer Support Portal.
2. Onboard Prisma AIRS AI Runtime API in Strata Cloud Manager.
3. Manage applications, API keys, security profiles, and custom topics in Strata Cloud Manager.

### Requirements for API Usage

1. API Key Token: This token is generated during the onboarding process in Strata Cloud Manager (see the onboarding prerequisite step above). Include the API key token in all API requests using the x-pan-token header.
2. AI Security Profile Name: This is the API security profile you created during the onboarding process in Strata Cloud Manager (see the prerequisite step on creating an API security profile above). Specify this profile name or the profile ID in the API request payload in the ai_profile field.

### Scan API Endpoints:

The following are the API endpoints based on the regions you selected while creating Prisma AIRS AI Runtime: API intercept deployment profile:

- US: https://service.api.aisecurity.paloaltonetworks.com
- EU (Germany): https://service-de.api.aisecurity.paloaltonetworks.com
- IN: https://service-in.api.aisecurity.paloaltonetworks.com
- SG: https://service-sg.api.aisecurity.paloaltonetworks.com

### Example code snippet ( REST API )

```python
import requests, json
json_object = {
  "contents": [
    {
      "prompt": "Prompt string"
    }
  ],
  "ai_profile": {
    "profile_name": "Security Profile Name"
  }
}
url = "API URL"
header = {'x-pan-token': 'API Key'}

def makeRequest():
    response = requests.post(url, json = json_object, headers = header)
    json_data = json.loads(response.text)
    recommendedAction = json_data['action']
    print("The recommended action for this prompt is: " + recommendedAction + ".")

makeRequest()
```
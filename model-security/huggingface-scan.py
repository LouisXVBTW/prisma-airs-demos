import os
import sys
import warnings
from dotenv import load_dotenv

# Suppress Pydantic warnings for a clean demo output
warnings.filterwarnings("ignore")

from model_security_client.api import ModelSecurityAPIClient 

# Load variables from the .env file into the environment
load_dotenv(override=True)

def scan_huggingface_model(hf_uri: str, sg_uuid: str):
    print(f"Scanning Hugging Face model: {hf_uri}...")
    
    # Initialize the client using the endpoint from the .env file 
    client = ModelSecurityAPIClient(
        base_url=os.getenv("MODEL_SECURITY_API_ENDPOINT", "https://api.sase.paloaltonetworks.com/aims") 
    )
    
    try:
        # Execute the scan using model_uri 
        result = client.scan(
            security_group_uuid=sg_uuid, 
            model_uri=hf_uri 
        )
        print(result)
        
        # Check the eval_outcome property 
        if result.eval_outcome == "BLOCKED": 
            print("🚨 SECURITY VERDICT: BLOCKED. Do not load this model.")
            sys.exit(1) # Halt progress 
            
        print("✅ SECURITY VERDICT: ALLOWED. Model is safe.") 
        return True

    except Exception as e:
        print(f"⚠️ Scan failed to complete: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Pull your Hugging Face specific Security Group UUID from the .env file 
    HF_SECURITY_GROUP = os.getenv("HF_SECURITY_GROUP")
    
    # Safety check to ensure the .env variable loaded correctly
    if not HF_SECURITY_GROUP:
        print("Error: HF_SECURITY_GROUP is missing from your .env file.")
        sys.exit(1)
        
    MODEL_TO_SCAN = "https://huggingface.co/microsoft/DialoGPT-medium"
    
    scan_huggingface_model(MODEL_TO_SCAN, HF_SECURITY_GROUP)
    
    print("Proceeding to load the model into memory...")
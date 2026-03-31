import os
import sys
import warnings
from dotenv import load_dotenv

# Suppress warnings
warnings.filterwarnings("ignore")

# Force load environment variables from .env, overriding any stale terminal exports
load_dotenv(override=True)

from model_security_client.api import ModelSecurityAPIClient 

def scan_local_model(local_dir: str, sg_uuid: str):
    print(f"Scanning local model at: {local_dir}...")
    
    # Initialize the client 
    client = ModelSecurityAPIClient(
        base_url=os.getenv("MODEL_SECURITY_API_ENDPOINT", "https://api.sase.paloaltonetworks.com/aims") 
    )
    
    try:
        # Use model_path for local directories 
        result = client.scan(
            security_group_uuid=sg_uuid, 
            model_path=local_dir 
        )
        
        print(f"Scan Outcome: {result.eval_outcome}") 
        
        if result.eval_outcome == "ALLOWED": 
            print("✅ Model passed all local security checks.")
        else:
            print("🚨 Model failed security checks. Do not deploy.")

    except Exception as e:
        print(f"Error scanning local model: {e}")

if __name__ == "__main__":
    # Use your Local Disk specific Security Group UUID 
    # Pulling from .env, fallback to the known good one if missing
    LOCAL_SECURITY_GROUP = os.getenv("LOCAL_SECURITY_GROUP")
    LOCAL_MODEL_PATH = "path/to/model/folder" 
    
    scan_local_model(LOCAL_MODEL_PATH, LOCAL_SECURITY_GROUP)

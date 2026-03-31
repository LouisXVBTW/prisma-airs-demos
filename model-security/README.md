# Model Security demo

## Minimal Viable Environment


### Environment

You need to run either Python 3.11/3.12/3.13

Follow the instructions for installing the Model Security SDK as this has a specific set of steps.

### Targets

You can scan AI models hosted on the following platforms and registries:
- Hugging Face 
- Amazon S3 
- Google Cloud Storage (GCS) 
- Azure Blob Storage 
- JFrog Artifactory 
- GitLab Model Registry 
- Local Storage / Local Disk 

The demos are currently support:
- Hugging Face
- Local Storage / Local Disk

-----

## How to set up

#### Creating deployment profile

[Follow this guide on how to assign your credits to a Model Security Deployment Profile. This is needed to license the product within SCM (Strata Cloud Manager)](https://docs.paloaltonetworks.com/ai-runtime-security/ai-model-security/model-security-to-secure-your-ai-models/get-started-with-ai-model-security/create-a-deployment-profile-for-prisma-airs-ai-model-security)

#### Configure IAM (Identity and Access Management)

[Follow this guide to set up the required IAM within SCM. This is the where you will get all the required secrets](https://docs.paloaltonetworks.com/ai-runtime-security/ai-model-security/model-security-to-secure-your-ai-models/get-started-with-ai-model-security/configure-identity-and-access-management)

#### Install AI Model Security

[Follow this guide to install the correct python package for Model Security](https://docs.paloaltonetworks.com/ai-runtime-security/ai-model-security/model-security-to-secure-your-ai-models/get-started-with-ai-model-security/install-ai-model-security)

The above should have all you need to get it working initially.

The following is what I have done which. Use the secrets from the IAM set up:

```bash
export MODEL_SECURITY_CLIENT_ID="<your-client-id>"
export MODEL_SECURITY_CLIENT_SECRET="<your-client-secret>"
export TSG_ID="<your-tsg-id>"
export MODEL_SECURITY_API_ENDPOINT="https://api.sase.paloaltonetworks.com/aims"

./get_pypi_url.sh
pip install "model-security-client[all]" --extra-index-url $(get_pypi_url.sh)
```

Once done, don't forget to create and fill out your environment file to keep your secrets consistent and safe.

```bash
cp .env.template .env
```

Then fill out the `.env`. This is needed for the demos to work.

This set up also installs the CLI. This will not be used in the demos but here is an example use:

```bash
model-security scan --model-uri https://huggingface.co/microsoft/DialoGPT-medium -sg 7d7418df-51b1-4d71-87b8-e661d2863276
```


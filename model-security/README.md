# Model Security demo



Official how to install guide:

[Install AI Model Security Docs](https://docs.paloaltonetworks.com/ai-runtime-security/ai-model-security/model-security-to-secure-your-ai-models/get-started-with-ai-model-security/install-ai-model-security)

The above should have all you need to get it working initially.

The following is what I have done:

```bash
python3.12 -m venv venv
source venv/bin/activate

export MODEL_SECURITY_CLIENT_ID="<your-client-id>"
export MODEL_SECURITY_CLIENT_SECRET="<your-client-secret>"
export TSG_ID="<your-tsg-id>"
export MODEL_SECURITY_API_ENDPOINT="https://api.sase.paloaltonetworks.com/aims"

./get_pypi_url.sh
pip install "model-security-client[all]" --extra-index-url $(get_pypi_url.sh)
```

the CLI works too:

```bash
model-security scan --model-uri https://huggingface.co/microsoft/DialoGPT-medium -sg 7d7418df-51b1-4d71-87b8-e661d2863276
```


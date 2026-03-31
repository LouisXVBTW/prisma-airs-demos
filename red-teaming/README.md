# Red Teaming

### Minimal Viable Environment

To use Prisma AIRs Red Teaming you will need to have the following AI API Structure/Standard avaible for us to work with. 

For testing models/applications:
- OpenAI api
- HuggingFace api
- AWS Bedrock access
- Databricks access
- REST API/Streaming/WebSockets
  - Must be a simple request/response architecture. We need to send our Red Teaming prompt and receive the model's response
  - Can be done over public internet or over a private chanel we call Network Channel.

For testing AI Agents with Agentic workflows:
- REST API/Streaming
  - Must be a simple request/response architecture. We need to send our Red Teaming prompt and receive the model's response
  - Can be done over public internet or over a private channel we call Network Channel.


---

Most of the red teaming is to be done via GUI but if you like most users understand that AI is non-deterministic. You will know that every change to your AI Agents will result in a change of behaviour so we want to programitically test the agent on every change or on a regular scheduled basis. 

Great for automatic auditing worthy reporting too. 

Will build that later. 


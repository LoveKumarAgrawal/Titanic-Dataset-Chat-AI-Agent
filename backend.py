from fastapi import FastAPI
from pydantic import BaseModel
from langchain_groq import ChatGroq
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from dotenv import load_dotenv
import os
import uvicorn

# Load environment variables from .env file
load_dotenv()

# Now you can access the API key
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize FastAPI app
app = FastAPI()

# Initialize the language model (Groq's model)
llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)

# Create the CSV agent using your Titanic CSV file
agent_executor = create_csv_agent(llm, "train.csv", allow_dangerous_code=True)


# Pydantic model for the request
class QueryRequest(BaseModel):
    query: str


@app.post("/query/")
async def query_titanic_data(request: QueryRequest):
    # Call the agent to get answers from the Titanic CSV data
    resp = agent_executor.invoke({"input": request.query})
    print(resp)
    return {"response": resp.get("output")}

if __name__ == "__main__":
    uvicorn.run("backend:app", host="0.0.0.0", port=8000, reload=True)
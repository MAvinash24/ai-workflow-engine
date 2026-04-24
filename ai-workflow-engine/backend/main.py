from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.agents.planner_agent import create_plan
from src.agents.executor_agent import execute_step
from src.agents.evaluator_agent import evaluate
from src.memory.context_store import add_memory
from src.memory.history_tracker import add_history

app = FastAPI()

# ✅ ADD THIS (VERY IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for dev (later restrict)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class GoalRequest(BaseModel):
    goal: str

@app.get("/")
def root():
    return {"message": "AI Workflow Engine Running"}

@app.post("/run")
def run(goal_request: GoalRequest):
    goal = goal_request.goal

    logs = []
    plan = create_plan(goal)
    previous_result = None
    for step in plan:
        result = execute_step(step, previous_result)
        evaluation = evaluate(step, result)

        add_memory(step, result)
        add_history(goal, step, result, evaluation)
        previous_result = result

        logs.append({
            "step": step,
            "result": str(result)[:200],
            "evaluation": evaluation
        })

    return {
        "goal": goal,
        "plan": plan,
        "logs": logs
    }
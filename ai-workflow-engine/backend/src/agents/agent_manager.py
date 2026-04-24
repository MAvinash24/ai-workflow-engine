from src.agents.planner_agent import create_plan
from src.agents.executor_agent import execute_step
from src.agents.evaluator_agent import evaluate
from src.memory.context_store import add_memory

def run_workflow(goal):
    logs = []

    plan = create_plan(goal)

    for step in plan:
        result = execute_step(step)
        evaluation = evaluate(step, result)

        add_memory(step, result)

        logs.append({
            "step": step,
            "result": str(result)[:200],
            "evaluation": evaluation
        })

    return logs
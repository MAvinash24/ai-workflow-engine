memory = []

def add_memory(step, result):
    memory.append({"step": step, "result": result})

def get_memory():
    return memory
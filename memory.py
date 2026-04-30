user_memory = {}

def update_memory(user_id, new_data):
    if user_id not in user_memory:
        user_memory[user_id] = {}

    user_memory[user_id].update(new_data)

def get_memory(user_id):
    return user_memory.get(user_id, {})

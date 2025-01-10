def log_activity(username, action):
    with open("activity.log", "a") as file:
        file.write(f"User: {username}, Action: {action}\n")

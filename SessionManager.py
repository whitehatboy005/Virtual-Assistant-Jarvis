class SessionManager:
    def __init__(self, filename='session_data.json'):
        self.filename = filename
        self.sessions = self.load_sessions()

    def load_sessions(self):
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_session(self, user_input, ai_response):
        self.sessions.append({"user_input": user_input, "ai_response": ai_response})
        with open(self.filename, 'w') as f:
            json.dump(self.sessions, f)

    def get_session(self):
        return self.sessions
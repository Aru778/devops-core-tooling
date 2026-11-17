
def get_user_dashboard(username):
    dashboard = {
        "username": username,
        "role": "DevOps Engineer",
        "status": "Active",
        "services": [
            "Monitoring",
            "Deployment",
            "Infrastructure"
        ]
    }

    return dashboard


if __name__ == "__main__":
    user = get_user_dashboard("Arun")

    print("User Dashboard")
    print("----------------")
    print("Name:", user["username"])
    print("Role:", user["role"])
    print("Status:", user["status"])
    print("Services:", user["services"])

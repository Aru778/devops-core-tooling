
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
    dashboard_data = get_user_dashboard("Arun")
    print("User Dashboard")
    print("----------------")
    print("Name:", dashboard_data["username"])
    print("Role:", dashboard_data["role"])
    print("Status:", dashboard_data["status"])
    print("Services:", dashboard_data["services"])

# technician_assignment.py

technician_map = {
    "Hardware Issue": {
        "team": "Hardware Support Team",
        "technicians": [
            {"name": "Raj", "id": 101, "current_load": 3},
            {"name": "Nisha", "id": 102, "current_load": 1},
            {"name": "Amit", "id": 103, "current_load": 5}
        ]
    },
    "Software Issue": {
        "team": "Software Support Team",
        "technicians": [
            {"name": "Priya", "id": 201, "current_load": 0},
            {"name": "Karan", "id": 202, "current_load": 4}
        ]
    },
    "Network Issue": {
        "team": "Network Team",
        "technicians": [
            {"name": "Neeraj", "id": 301, "current_load": 2},
            {"name": "Shreya", "id": 302, "current_load": 1}
        ]
    },
    "Login Issue": {
        "team": "Access Management Team",
        "technicians": [
            {"name": "Vikram", "id": 401, "current_load": 2}
        ]
    },
    "Access Request": {
        "team": "IAM Team",
        "technicians": [
            {"name": "Mahesh", "id": 501, "current_load": 0},
            {"name": "Aarti", "id": 502, "current_load": 3}
        ]
    },
    "SAP Issue": {
        "team": "SAP Support Team",
        "technicians": [
            {"name": "Sunil", "id": 601, "current_load": 4},
            {"name": "Megha", "id": 602, "current_load": 1}
        ]
    },
    "Email Issue": {
        "team": "Messaging Team",
        "technicians": [
            {"name": "Jaspreet", "id": 701, "current_load": 1}
        ]
    },
    "Printer Issue": {
        "team": "Peripheral Support",
        "technicians": [
            {"name": "Deepak", "id": 801, "current_load": 2}
        ]
    },
    "VPN Issue": {
        "team": "Remote Access Team",
        "technicians": [
            {"name": "Monika", "id": 901, "current_load": 3}
        ]
    },
    "System Performance Issue": {
        "team": "System Health Team",
        "technicians": [
            {"name": "Harsh", "id": 1001, "current_load": 4},
            {"name": "Rohit", "id": 1002, "current_load": 1}
        ]
    },
    "Power Issue": {
        "team": "Infra Support",
        "technicians": [
            {"name": "Arun", "id": 1101, "current_load": 0}
        ]
    },
    "Device Request": {
        "team": "Inventory & Procurement Team",
        "technicians": [
            {"name": "Lakshmi", "id": 1201, "current_load": 2}
        ]
    }
}


def assign_technician(category, priority):
    if category not in technician_map:
        return {
            "team": "General Support",
            "technician": {"name": "Fallback Technician", "id": 999, "current_load": 0}
        }

    team_info = technician_map[category]
    technicians = team_info["technicians"]

    # Sort technicians by lowest load
    sorted_techs = sorted(technicians, key=lambda x: x["current_load"])

    # Priority logic
    if priority in ["Critical", "High"]:
        selected = sorted_techs[0]
    elif priority == "Medium":
        selected = sorted_techs[min(1, len(sorted_techs)-1)]
    else:
        selected = sorted_techs[-1]

    return {
        "team": team_info["team"],
        "technician": selected
    }

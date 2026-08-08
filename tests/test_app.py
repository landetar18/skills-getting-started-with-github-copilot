from fastapi.testclient import TestClient

from src.app import app, activities

client = TestClient(app)


def test_unregister_participant_removes_from_activity():
    activity_name = "Chess Club"
    email = "michael@mergington.edu"
    original_participants = activities[activity_name]["participants"][:]

    try:
        response = client.delete(f"/activities/{activity_name}/participants/{email}")

        assert response.status_code == 200
        assert response.json()["message"] == f"Removed {email} from {activity_name}"

        updated = client.get("/activities").json()
        assert email not in updated[activity_name]["participants"]
    finally:
        activities[activity_name]["participants"] = original_participants

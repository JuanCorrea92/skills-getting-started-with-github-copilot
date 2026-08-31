from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_unregister_participant_removes_email_from_activity():
    activity_name = "Chess Club"
    email = "newstudent@mergington.edu"

    signup_response = client.post(f"/activities/{activity_name}/signup?email={email}")
    assert signup_response.status_code == 200

    unregister_response = client.delete(f"/activities/{activity_name}/unregister?email={email}")
    assert unregister_response.status_code == 200

    activities_response = client.get("/activities")
    assert email not in activities_response.json()[activity_name]["participants"]


def test_unregister_returns_404_when_activity_is_missing():
    response = client.delete("/activities/Unknown Activity/unregister?email=test@mergington.edu")
    assert response.status_code == 404

def test_create_user():
    from app.services.user_service import UserService
    service = UserService()
    user = service.create_user("Anna", "anna@example.com", "tajnehaslo", "member")
    assert user.email == "anna@example.com"

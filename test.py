import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_create_group(db_session):
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/group/", json={"name": "Test Group", "description": "A test group"})
    assert response.status_code == 201
    assert response.json()["name"] == "Test Group"

# Добавьте дополнительные тесты для остальных эндпоинтов и функций

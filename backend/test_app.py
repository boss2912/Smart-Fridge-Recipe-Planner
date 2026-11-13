import pytest
import app


@pytest.fixture
def client():
    return app.app.test_client()


# จุดที่ 1: ตรวจโครงโปรแกรม
def test_app_structure():
    assert hasattr(app, "app"), "ไม่พบตัวแปร app ใน backend/app.py"
    assert app.FRONTEND_DIR.name == "frontend", "FRONTEND_DIR ต้องชี้โฟลเดอร์ frontend"
    assert app.app.template_folder == str(app.FRONTEND_DIR / "templates"), "template ต้องอยู่ใน frontend/templates"
    assert app.app.static_folder == str(app.FRONTEND_DIR / "static"), "CSS / JS / รูป ต้องอยู่ใน frontend/static"


# จุดที่ 2: ตรวจว่าเปิดหน้าแรกได้
def test_index_page(client):
    res = client.get("/")

    assert res.status_code == 200, f"หน้าแรกต้องตอบ 200 (ค่าที่ได้: {res.status_code})"
    assert "Smart Fridge" in res.get_data(as_text=True), "หน้าแรกต้องมีคำว่า Smart Fridge"


# จุดที่ 3: ตรวจว่า Flask ส่ง CSS จาก frontend/static ได้
def test_css_file(client):
    res = client.get("/static/css/style.css")

    assert res.status_code == 200, f"ไฟล์ CSS ต้องตอบ 200 (ค่าที่ได้: {res.status_code})"
    assert "text/css" in res.content_type, f"ไฟล์ CSS ต้องเป็น text/css (ค่าที่ได้: {res.content_type})"
    res.close()

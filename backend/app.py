"""โปรแกรม Flask ของ Smart Fridge

รันจาก root ของ repo:  flask --app backend/app run --debug
วิธีติดตั้งอยู่ใน INSTALL.md

template กับ CSS / JS / รูป อยู่ในโฟลเดอร์ frontend/ (ADR-009)
ไฟล์นี้มีแค่ route ที่รับคำขอแล้วส่งหน้าเว็บ ยังไม่ต่อ database
"""

from pathlib import Path

from flask import Flask, render_template

FRONTEND_DIR = Path(__file__).resolve().parent.parent / "frontend"

app = Flask(
    __name__,
    template_folder=str(FRONTEND_DIR / "templates"),
    static_folder=str(FRONTEND_DIR / "static"),
)


@app.route("/")
def index():
    return render_template("index.html")

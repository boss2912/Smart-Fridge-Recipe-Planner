# อิมเมจ Python 3.14 บน Debian 12 (Bookworm) ล็อกเลขรุ่นตาม INSTALL.md
FROM python:3.14.10-slim-bookworm

# ไม่สร้างไฟล์ .pyc และให้แสดงข้อความจาก Python ทันทีใน docker compose logs
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# คัดลอกเฉพาะรายการ library มาลงก่อน ถ้าแก้แค่โค้ดจะได้ไม่ต้องลง library ใหม่ตอน build
COPY backend/requirements.txt backend/requirements.txt
RUN pip install --no-cache-dir -r backend/requirements.txt

# คัดลอกโค้ด backend และ frontend เข้าอิมเมจ
COPY backend backend
COPY frontend frontend

EXPOSE 5000

# รัน Flask บน 0.0.0.0 เพื่อให้เปิดจากเครื่องตัวเองผ่านพอร์ตที่ compose.yaml ผูกไว้ได้
CMD ["flask", "--app", "backend/app", "run", "--debug", "--host", "0.0.0.0"]

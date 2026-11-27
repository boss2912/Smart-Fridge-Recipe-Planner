# nginx/ — ทางเข้าเดียวของระบบ

👤 บอส

> 🟡 **มีโครง config + Docker แล้ว** ([#35](https://github.com/boss2912/Smart-Fridge-Recipe-Planner/issues/35)) — ทดสอบผ่าน 1 เครื่องได้ทันที · ทดสอบทั้งวงจร 2 เครื่องในรอบ 7 ([ADR-008](../docs/DECISIONS.md#adr-008--ทำเป็นเว็บแอปที่ใช้งานได้จริง)) · เป็นงานเพิ่มนอกงานส่ง 4 ชิ้นของอาจารย์ (Lecture 1 หน้า 11)

## หน้าที่

ส่งต่อทุกคำขอไปที่ Flask ใน [`backend/`](../backend/) · ส่งไฟล์ CSS / JS / รูปของ [`frontend/`](../frontend/) ให้เบราว์เซอร์เองได้ · วันนำเสนอรันบนเครื่อง 1 ([ADR-009](../docs/DECISIONS.md#adr-009--เลือกภาษาและวิธีรันเว็บแอป)) · ตอนพัฒนาในเครื่องตัวเองไม่ต้องใช้

สิ่งที่ส่วนนี้ต้องมี → [ตาราง "แต่ละส่วนต้องมีอะไร" ใน README](../README.md#แต่ละส่วนต้องมีอะไร)

## การแยกเส้นทางคำขอ

```text
Browser ──► Nginx (พอร์ต 8080 ตอนทดสอบ / พอร์ต 80 วันเดโม)
              ├── GET /static/*     ──► ส่งไฟล์จาก frontend/static/ เอง (ไม่ผ่าน Flask)
              ├── GET /nginx-health ──► ตอบ 200 ok (สำหรับ Docker healthcheck)
              └── คำขออื่นทั้งหมด /* ──► ส่งต่อไปที่ Flask (BACKEND_UPSTREAM)
```

## ไฟล์ในโฟลเดอร์นี้

| ไฟล์ | หน้าที่ |
|---|---|
| [`default.conf.template`](default.conf.template) | การตั้งค่า Nginx (reverse proxy + static + security headers) อิมเมจจะแทนค่า `${BACKEND_UPSTREAM}` ตอนเปิด container |
| [`compose.yaml`](compose.yaml) | ไฟล์ Docker Compose สำหรับรัน container `nginx:1.28.3-trixie` แยกเดี่ยว พร้อม healthcheck และ mount ไฟล์แบบ `:ro` |
| [`.env.example`](.env.example) | ตัวอย่างตัวแปรสภาพแวดล้อมสำหรับทดสอบ 1 เครื่อง และสำหรับเครื่อง 1 วันเดโม 2 เครื่อง |
| `README.md` | คู่มือรันและขั้นตอนตรวจผล (ไฟล์นี้) |

## วิธีทดสอบบนเครื่องเดียว

1. เปิด Flask บนพอร์ต `5000` ให้ทำงานอยู่ก่อน (จาก Docker Compose ที่ root ของโปรเจกต์ หรือรัน `flask --app backend/app run --debug`)
2. เปิด Nginx จากโฟลเดอร์นี้ (ค่าเริ่มต้นผูก `127.0.0.1:8080` และส่งต่อไป `host.docker.internal:5000`):

```bash
cd nginx
docker compose up -d
```

3. เปิดเบราว์เซอร์ไปที่ `http://127.0.0.1:8080` จะเห็นหน้า Smart Fridge พร้อมสไตล์จาก CSS
4. เมื่อทดสอบเสร็จ สั่งหยุดด้วย:

```bash
cd nginx
docker compose down
```

## วิธีรันบนเครื่อง 1 วันเดโม 2 เครื่อง (รอบ 7)

1. คัดลอก `.env.example` เป็น `.env` ในโฟลเดอร์ `nginx/` (ไฟล์ `.env` ถูกกันไว้ใน [`.gitignore`](../.gitignore) ไม่ขึ้น GitHub):

```bash
cd nginx
cp .env.example .env
```

2. แก้ค่าใน `nginx/.env` ให้รับการเชื่อมต่อจากภายนอกและชี้ไปยัง IP ของเครื่อง 2:

```dotenv
NGINX_BIND=0.0.0.0
NGINX_PORT=80
BACKEND_UPSTREAM=192.168.1.20:5000
```

3. สั่งรัน `docker compose up -d`

> ⚠️ **ข้อควรระวังวันเดโม (รอบ 7):** บนเครื่อง 2 ห้ามรัน Flask ด้วย `--debug` หรือผูกแค่ `127.0.0.1` — ต้องรันผ่าน WSGI server (เช่น `gunicorn`) และตั้งไฟร์วอลล์ให้เปิดพอร์ต 5000 เฉพาะ IP ของเครื่อง 1 และต้องมีสำเนาโฟลเดอร์ `frontend/static/` รุ่นล่าสุดอยู่บนเครื่อง 1 ด้วย

## วิธีตรวจว่าทำงานถูกต้อง

รันคำสั่งเหล่านี้จากโฟลเดอร์ `nginx/` ขณะที่ทั้ง Flask และ Nginx กำลังทำงานอยู่:

```bash
# 1. ตรวจไวยากรณ์ config ที่ถูกสร้างจาก template
docker compose exec nginx nginx -t

# 2. ตรวจสถานะ healthcheck ของ container
docker compose ps

# 3. ตรวจจุด healthcheck ของ Nginx เอง (ต้องได้ 200 ok)
curl -i http://127.0.0.1:8080/nginx-health

# 4. ตรวจหน้าหลักที่ส่งต่อมาจาก Flask (ต้องได้ 200 และมีข้อความ Smart Fridge + security headers)
curl -i http://127.0.0.1:8080/

# 5. ตรวจไฟล์ CSS ที่ Nginx ส่งเองโดยไม่ผ่าน Flask (ต้องได้ 200 text/css, Cache-Control, และไม่มี log โผล่ที่ Flask)
curl -i http://127.0.0.1:8080/static/css/style.css

# 6. ตรวจการกัน path traversal และ directory listing (ต้องถูกปฏิเสธ ไม่ได้ 200)
curl -i --path-as-is http://127.0.0.1:8080/static/../app.py
curl -i http://127.0.0.1:8080/static/
```

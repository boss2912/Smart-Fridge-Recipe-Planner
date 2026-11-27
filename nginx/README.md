# nginx/ — ทางเข้าเดียวของระบบ

👤 บอส

> 🟡 **มีโครง config + Docker แล้ว** ([#35](https://github.com/boss2912/Smart-Fridge-Recipe-Planner/issues/35)) — ทดสอบผ่าน 1 เครื่องได้ทุก OS ด้วย `docker compose --profile nginx up -d` · ทดสอบทั้งวงจร 2 เครื่องในรอบ 7 ([ADR-008](../docs/DECISIONS.md#adr-008--ทำเป็นเว็บแอปที่ใช้งานได้จริง) · [ADR-021](../docs/DECISIONS.md#adr-021--รันเว็บแอปและฐานข้อมูลด้วย-docker-compose)) · เป็นงานเพิ่มนอกงานส่ง 4 ชิ้นของอาจารย์ (Lecture 1 หน้า 11)

## หน้าที่

ส่งต่อทุกคำขอไปที่ Flask ใน [`backend/`](../backend/) · ส่งไฟล์ CSS / JS / รูปของ [`frontend/`](../frontend/) ให้เบราว์เซอร์เองได้ · วันนำเสนอรันบนเครื่อง 1 ([ADR-021](../docs/DECISIONS.md#adr-021--รันเว็บแอปและฐานข้อมูลด้วย-docker-compose)) · ตอนพัฒนาในเครื่องตัวเองไม่ต้องใช้

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
| [`compose.yaml`](compose.yaml) | ไฟล์ Docker Compose สำหรับรัน container `nginx:1.28.3-trixie` แยกบน **เครื่อง 1 วันเดโม 2 เครื่อง** |
| [`.env.example`](.env.example) | ตัวอย่างตัวแปรสภาพแวดล้อมสำหรับเครื่อง 1 วันเดโม 2 เครื่อง |
| `README.md` | คู่มือรันและขั้นตอนตรวจผล (ไฟล์นี้) |

## วิธีทดสอบบนเครื่องเดียว (ใช้ได้ทุก OS: Windows · macOS · Linux)

รันผ่าน profile `nginx` ใน [`compose.yaml`](../compose.yaml) ที่ root ของโปรเจกต์ เพื่อให้ `nginx` อยู่ Docker network เดียวกับ `web` และชี้ไป `web:5000` ได้โดยตรง (ไม่ติดข้อจำกัด `host.docker.internal` บน Linux):

```bash
# เปิด web + db + nginx จาก root ของโปรเจกต์
docker compose --profile nginx up -d
```

เปิดเบราว์เซอร์ไปที่ `http://127.0.0.1:8080` จะเห็นหน้า Smart Fridge พร้อมสไตล์จาก CSS

เมื่อทดสอบเสร็จ ปิดเฉพาะ Nginx (ให้ `web` กับ `db` รันต่อ) หรือปิดทั้งหมด:

```bash
# ปิดเฉพาะ container nginx
docker compose --profile nginx stop nginx && docker compose --profile nginx rm -f nginx

# หรือปิดทุก container (web + db + nginx)
docker compose --profile nginx down
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

> ⚠️ **ข้อควรระวังวันเดโม (รอบ 7):** บนเครื่อง 2 ห้ามรัน Flask ด้วย `--debug` หรือผูกแค่ `127.0.0.1` — ต้องรันผ่าน WSGI server (เช่น `gunicorn` ใน `compose.demo.yaml` ตาม [ADR-021](../docs/DECISIONS.md#adr-021--รันเว็บแอปและฐานข้อมูลด้วย-docker-compose)) ตั้งไฟร์วอลล์ให้เปิดพอร์ต 5000 เฉพาะ IP ของเครื่อง 1 และมีสำเนาโฟลเดอร์ `frontend/static/` รุ่นล่าสุดอยู่บนเครื่อง 1 ด้วย

## วิธีตรวจว่าทำงานถูกต้อง

รันคำสั่งเหล่านี้จาก **root ของโปรเจกต์** หลังเปิด `docker compose --profile nginx up -d`:

```bash
# 1. ตรวจไวยากรณ์ config ที่ถูกสร้างจาก template
docker compose --profile nginx exec nginx nginx -t

# 2. ตรวจสถานะ healthcheck ของ container
docker compose --profile nginx ps

# 3. ตรวจจุด healthcheck ของ Nginx เอง (ต้องได้ 200 ok)
curl -i http://127.0.0.1:8080/nginx-health

# 4. ตรวจหน้าหลักที่ส่งต่อมาจาก Flask (ต้องได้ 200 และมีข้อความ Smart Fridge + security headers)
curl -i http://127.0.0.1:8080/

# 5. ตรวจไฟล์ CSS ที่ Nginx ส่งเองโดยไม่ผ่าน Flask (ต้องได้ 200 text/css, Cache-Control, และไม่มี log โผล่ที่ Flask)
curl -i http://127.0.0.1:8080/static/css/style.css

# 6. ตรวจการกัน directory listing และ path traversal (ต้องถูกปฏิเสธ ไม่ได้ 200)
curl -i http://127.0.0.1:8080/static/
curl -i --path-as-is http://127.0.0.1:8080/static/../app.py
```

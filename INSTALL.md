# คู่มือติดตั้งและรัน Smart Fridge (Docker)

รองรับ **Windows** · **macOS** · **Linux** · ทุกส่วนรันอยู่ใน **Docker Compose** ไม่ต้องลง Python หรือ PostgreSQL แยกในเครื่องตัวเอง ([ADR-021](docs/DECISIONS.md#adr-021--รันเว็บแอปและฐานข้อมูลด้วย-docker-compose))

> ทุกเวอร์ชันทั้งใน [`Dockerfile`](Dockerfile) · [`compose.yaml`](compose.yaml) · และ [`backend/requirements.txt`](backend/requirements.txt) **ล็อกไว้ครบทุกตัว** ทุกคนจะได้สภาพแวดล้อมชุดเดียวกันทั้งหมด

---

## สารบัญ

1. [ต้องมีอะไรก่อน](#1-ต้องมีอะไรก่อน)
2. [ติดตั้ง Docker Desktop](#2-ติดตั้ง-docker-desktop)
3. [เริ่มรันโปรเจกต์](#3-เริ่มรันโปรเจกต์)
4. [ตรวจว่าติดตั้งสำเร็จ](#4-ตรวจว่าติดตั้งสำเร็จ)
5. [คำสั่งที่ใช้บ่อย](#5-คำสั่งที่ใช้บ่อย)
6. [โครงสร้างไฟล์และความปลอดภัย](#6-โครงสร้างไฟล์และความปลอดภัย)
7. [แก้ปัญหาที่เจอบ่อย](#7-แก้ปัญหาที่เจอบ่อย)
8. [ภาคผนวก — ชุดเวอร์ชันที่ล็อกไว้](#8-ภาคผนวก--ชุดเวอร์ชันที่ล็อกไว้)

---

## 1. ต้องมีอะไรก่อน

| ของ | เวอร์ชัน | หมายเหตุ |
|---|---|---|
| **Git** | อะไรก็ได้ | ใช้ดึงโค้ดและส่งงาน |
| **Docker Desktop** | รุ่นล่าสุด (มี `docker compose` ในตัว) | Linux ลง Docker Engine + Compose plugin แทนได้ |

ส่วน **Python 3.14.10** · **Flask 3.1.3** · และ **PostgreSQL 18.7** อยู่ใน container แล้ว ไม่ต้องลงเพิ่มในเครื่อง

### เช็คว่ามี Docker พร้อมใช้งานหรือยัง

เปิดโปรแกรม **Docker Desktop** ทิ้งไว้จนสถานะเป็น Running แล้วรันใน terminal:

```bash
docker --version
docker compose version
docker info
```

ถ้า `docker info` แสดงข้อมูล Server ได้โดยไม่ขึ้น error แปลว่าพร้อมเริ่มข้อ 3 ได้เลย

---

## 2. ติดตั้ง Docker Desktop

ทำเฉพาะเครื่องที่ยังไม่มี Docker

| ระบบ | วิธีติดตั้ง |
|---|---|
| **Windows** | `winget install Docker.DockerDesktop` หรือโหลดจาก [docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop/) · ติดตั้งเสร็จแล้วรีสตาร์ทเครื่อง 1 ครั้ง แล้วเปิดโปรแกรม **Docker Desktop** รอจนแถบล่างซ้ายขึ้น Engine running |
| **macOS** | `brew install --cask docker` หรือโหลดตัวติดตั้งให้ตรงชิป (Apple Silicon / Intel) จาก [docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop/) แล้วเปิดแอป **Docker** |
| **Linux** | ลง Docker Engine และ `docker-compose-plugin` ตามคู่มือ distro ใน [docs.docker.com/engine/install](https://docs.docker.com/engine/install/) |

---

## 3. เริ่มรันโปรเจกต์

```bash
# 1) clone แล้วไปที่ branch develop
git clone https://github.com/boss2912/Smart-Fridge-Recipe-Planner.git
cd Smart-Fridge-Recipe-Planner
git switch develop

# 2) สร้างอิมเมจและรันทั้ง Flask (web) + PostgreSQL 18 (db)
docker compose up -d --build
```

รันครั้งแรกจะใช้เวลาโหลดอิมเมจ Python กับ PostgreSQL สักครู่ รอบถัดไปจะขึ้นภายในไม่กี่วินาที

- ตอนนี้ Flask ยังไม่ต่อ PostgreSQL จนกว่า ER กับ Relational Schema จะเสร็จ (ต่อจริงรอบ 5 ตาม [`docs/ROADMAP.md`](docs/ROADMAP.md))
- โฟลเดอร์ `backend/` กับ `frontend/` เชื่อมเข้า container ไว้แล้ว แก้โค้ดหรือแก้ HTML / CSS บนเครื่องแล้วกดรีเฟรชหน้าเว็บเห็นผลทันที ไม่ต้องสั่ง `--build` ใหม่

---

## 4. ตรวจว่าติดตั้งสำเร็จ

รันจากโฟลเดอร์ของโปรเจกต์ให้ครบ 3 ข้อ:

### 4.1 รันเทส `pytest` ใน container `web`

```bash
docker compose exec web python -m pytest backend -v
```

ต้องได้ **`16 passed`** · เทสมี 2 ไฟล์

| ไฟล์ | ตรวจอะไร |
|---|---|
| [`backend/test_install.py`](backend/test_install.py) | Python เป็น 3.14 · library ทั้ง 12 ตัวบน Linux ตรงกับเวอร์ชันใน `requirements.txt` (ข้าม `colorama` ซึ่งเป็นตัวเฉพาะ Windows) |
| [`backend/test_app.py`](backend/test_app.py) | Flask เปิดหน้าแรกได้ · ส่ง CSS จาก `frontend/static/` ได้ |

### 4.2 เช็คว่า PostgreSQL 18 ทำงานอยู่

```bash
docker compose exec db psql -U postgres -d smartfridge -c "SELECT version();"
```

ต้องเห็นบรรทัดที่ขึ้นต้นด้วย `PostgreSQL 18`

### 4.3 เปิดหน้าเว็บ

เปิด http://127.0.0.1:5000 ในเบราว์เซอร์ ต้องเห็นหน้า **"Smart Fridge & Recipe Planner"**

---

## 5. คำสั่งที่ใช้บ่อย

```bash
docker compose up -d              # เปิดระบบ (ใช้ตอนสร้างอิมเมจไว้แล้ว)
docker compose up -d --build      # เปิดระบบพร้อมสร้างอิมเมจใหม่ (ใช้เมื่อ requirements.txt หรือ Dockerfile เปลี่ยน)
docker compose ps                 # ดูว่า web กับ db ทำงานอยู่ไหม
docker compose logs -f web        # ดูข้อความและ error ของ Flask แบบสด (ออกด้วย Ctrl+C)
docker compose exec db psql -U postgres -d smartfridge   # เข้าหน้าคำสั่ง SQL ของ PostgreSQL (ออกด้วย \q)
docker compose down               # หยุดระบบ (ข้อมูลในฐานข้อมูลยังอยู่)
docker compose down -v            # หยุดระบบและลบข้อมูลฐานข้อมูลทิ้งทั้งหมดเพื่อเริ่มใหม่จากศูนย์
```

---

## 6. โครงสร้างไฟล์และความปลอดภัย

```text
Smart-Fridge-Recipe-Planner/
├── Dockerfile              วิธีสร้างอิมเมจ Flask (Python 3.14.10)
├── compose.yaml            สั่งรันคู่กัน 2 ตัว: web (Flask) + db (PostgreSQL 18.7)
├── backend/
│   ├── app.py              โปรแกรม Flask + route
│   ├── requirements.txt    library ที่ล็อกเวอร์ชันไว้ (ASCII ล้วน)
│   ├── test_app.py         เทสหน้าเว็บ
│   └── test_install.py     เทสเวอร์ชัน Python และ library
└── frontend/
    ├── templates/          template HTML ที่ Flask เติมข้อมูล (base.html = โครงทุกหน้า)
    └── static/css/         CSS · JS กับรูปใส่ static/ เหมือนกัน
```

### 🔴 ห้ามลบ `127.0.0.1:` หน้าพอร์ตใน `compose.yaml` ตอนเปิด `--debug`

ใน `Dockerfile` ต้องสั่ง `--host 0.0.0.0` เพื่อให้เครื่องเราเข้าถึง Flask ข้างใน container ได้ ส่วน [`compose.yaml`](compose.yaml) ล็อกพอร์ตฝั่งเครื่องเราไว้ที่ `"127.0.0.1:5000:5000"` เท่านั้น ถ้าแก้เป็น `"5000:5000"` เฉยๆ เครื่องอื่นในวง Wi-Fi เดียวกันจะเปิดหน้า debugger ของ Flask แล้วรันโค้ด Python บนเครื่องเราได้ · การเปิดข้ามเครื่องทำผ่าน Nginx ในรอบ 7 ([`docs/ROADMAP.md`](docs/ROADMAP.md#-ปฏิทิน-9-รอบ-พุธ--อังคาร))

---

## 7. แก้ปัญหาที่เจอบ่อย

### ❌ `open //./pipe/dockerDesktopLinuxEngine: The system cannot find the file specified` (หรือ `Cannot connect to the Docker daemon`)

ยังไม่ได้เปิดโปรแกรม **Docker Desktop** หรือโปรแกรมยังเปิดไม่เสร็จ → เปิด Docker Desktop แล้วรอจนมุมซ้ายล่างขึ้นว่า Engine running ก่อนรันคำสั่งใหม่

---

### ❌ Docker Desktop แจ้งให้อัปเดต WSL 2 หรือเปิด Virtualization (Windows)

เปิด PowerShell แล้วรัน:

```powershell
wsl --install
wsl --update
```

แล้วรีสตาร์ทเครื่อง · ถ้ายังขึ้นว่า Virtualization is disabled ต้องเข้าไปเปิด Intel VT-x / AMD-V (SVM Mode) ใน BIOS ของเครื่อง

---

### ❌ `Bind for 127.0.0.1:5000 failed: port is already allocated`

มีโปรแกรมอื่นในเครื่องใช้พอร์ต 5000 อยู่ (เช่น AirPlay Receiver บน macOS หรือ Flask ที่รันค้างไว้ที่อื่น) → สั่งเปลี่ยนพอร์ตตอนรันได้โดยไม่ต้องแก้ไฟล์ `compose.yaml`:

**Windows (PowerShell)**
```powershell
$env:FLASK_PORT=5001; docker compose up -d
```

**macOS / Linux**
```bash
FLASK_PORT=5001 docker compose up -d
```

แล้วเปิด http://127.0.0.1:5001 แทน

---

### 💡 อยากใช้โปรแกรมดูตารางจากนอก Docker (เช่น DBeaver / pgAdmin / VS Code)

ค่าเดิมใน [`compose.yaml`](compose.yaml) ไม่ได้เปิดพอร์ตของ `db` ออกมาที่เครื่องตัวเอง เพื่อไม่ให้ชนกับ PostgreSQL ที่บางคนอาจเคยลงไว้ในเครื่อง (`5432`) ถ้าต้องการต่อโปรแกรมดูตารางจากข้างนอก ให้เอาเครื่องหมาย `#` หน้า `ports:` ของ `db` ใน `compose.yaml` ออก แล้วต่อเข้า `127.0.0.1` พอร์ต `5433` (อย่า commit การแก้ส่วนตัวนี้ขึ้น PR)

---

## 8. ภาคผนวก — ชุดเวอร์ชันที่ล็อกไว้

### เลือกเวอร์ชันยังไง

กติกาเดียวกันทุกตัว: **ใช้รุ่นแก้บั๊กล่าสุด ของสายที่ออกมาแล้วอย่างน้อย 2 เดือน และไม่มีช่องโหว่ที่รู้**

| ของ | เวอร์ชันที่ล็อก | ทำไมเลือกตัวนี้ |
|---|---|---|
| อิมเมจ Python (`web`) | `python:3.14.10-slim-bookworm` | Python 3.14 ยังได้รุ่นแก้บั๊กถึง ต.ค. 2027 · Debian 12 Bookworm เสถียรและใช้ `glibc` มาตรฐาน |
| อิมเมจ PostgreSQL (`db`) | `postgres:18.7-bookworm` | PostgreSQL 18 ดูแลถึง พ.ย. 2030 · รุ่น 18 เก็บข้อมูลใน `/var/lib/postgresql` |
| Flask | `3.1.3` | รุ่นแก้ช่องโหว่ ก.พ. 2026 |
| Werkzeug | `3.1.9` | รุ่นแก้ช่องโหว่ ก.ย. 2026 |
| Jinja2 | `3.1.6` | ใช้มาตั้งแต่ มี.ค. 2025 |
| MarkupSafe | `3.0.4` | รุ่นแก้บั๊ก ต.ค. 2026 |
| itsdangerous | `2.2.0` | |
| click | `8.5.1` | รุ่นแก้บั๊กของสาย 8.5 (ส.ค. 2026) |
| blinker | `1.9.0` | |
| pytest | `9.1.1` | `9.2.0` เพิ่งออก 27 ต.ค. 2026 และมีของที่เปลี่ยนแบบใช้ของเดิมไม่ได้ |
| pluggy | `1.6.0` | ตัวที่ใช้คู่ pytest 9.1.1 ตอนออก |
| iniconfig | `2.3.1` | |
| packaging | `26.3` | |
| Pygments | `2.21.0` | |
| colorama | `0.4.6` | ลงเฉพาะตอนรันบน Windows นอก container |

### เวลาจะอัปเกรดเวอร์ชัน

1. แก้เลขรุ่นใน [`Dockerfile`](Dockerfile) · [`compose.yaml`](compose.yaml) · หรือ [`backend/requirements.txt`](backend/requirements.txt) (ถ้าเปลี่ยนรุ่นหลักของ Python ต้องแก้ [`backend/test_install.py`](backend/test_install.py) ด้วย)
2. สั่งสร้างอิมเมจใหม่ทั้งหมดด้วย `docker compose build --no-cache` แล้วรัน `docker compose up -d`
3. รัน `docker compose exec web python -m pytest backend -v` ต้องได้ `16 passed`
4. แก้ตารางในหัวข้อ 8 นี้ให้ตรงกัน
5. เปิด PR แยกสำหรับอัปเกรด อย่าปนกับงานอื่น

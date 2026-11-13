# คู่มือติดตั้ง Smart Fridge

รองรับ **Windows** · **macOS** · **Linux** · **Conda** · ตอนพัฒนารัน Flask ตรงในเครื่องตัวเอง ไม่ผ่าน Nginx ([ADR-009](docs/DECISIONS.md#adr-009--เลือกภาษาและวิธีรันเว็บแอป))

> ทุกเวอร์ชันใน [`backend/requirements.txt`](backend/requirements.txt) **ล็อกไว้** ทุกคนจะได้ชุดเดียวกัน ไม่เกิดปัญหา "เครื่องผมรันได้"
> ทดสอบแล้วบน Windows 11: venv + Python 3.14.7 และ Conda + Python 3.14.10 · `pytest` 17/17 ผ่าน · เปิดหน้าแรกได้
> macOS / Linux ยังไม่มีใครลองจริง ใครลองแล้วติดตรงไหนให้เปิด issue

---

## สารบัญ

1. [ต้องมีอะไรก่อน](#1-ต้องมีอะไรก่อน)
2. [เลือกวิธีติดตั้ง](#2-เลือกวิธีติดตั้ง)
3. [วิธีที่ 1 — venv + pip (Windows)](#3-วิธีที่-1--venv--pip-windows)
4. [วิธีที่ 2 — venv + pip (macOS / Linux)](#4-วิธีที่-2--venv--pip-macos--linux)
5. [วิธีที่ 3 — Conda](#5-วิธีที่-3--conda)
6. [ติดตั้ง PostgreSQL 18](#6-ติดตั้ง-postgresql-18)
7. [ตรวจว่าติดตั้งสำเร็จ](#7-ตรวจว่าติดตั้งสำเร็จ)
8. [รันโปรเจกต์](#8-รันโปรเจกต์)
9. [แก้ปัญหาที่เจอบ่อย](#9-แก้ปัญหาที่เจอบ่อย)
10. [ภาคผนวก — ชุดเวอร์ชันที่ล็อกไว้](#10-ภาคผนวก--ชุดเวอร์ชันที่ล็อกไว้)

---

## 1. ต้องมีอะไรก่อน

| ของ | เวอร์ชัน | หมายเหตุ |
|---|---|---|
| **Python** | **3.14** | ทุก library ทดสอบบน 3.14 · ถ้าใช้ Conda ไม่ต้องลงเอง |
| **Git** | อะไรก็ได้ | |
| **PostgreSQL** | **18** | ลงไว้ก่อนรอบ 2 · ตอนนี้ Flask ยังไม่ต่อ database เพราะ ER ยังไม่เสร็จ ([หัวข้อ 6](#6-ติดตั้ง-postgresql-18)) |
| Conda | ถ้าใช้วิธีที่ 3 | Miniconda พอ |

### เช็คว่ามี Python 3.14 แล้วหรือยัง

**Windows (PowerShell)**
```powershell
py --list
py -3.14 --version
```

**macOS / Linux**
```bash
python3.14 --version
```

### ถ้ายังไม่มี Python 3.14

| ระบบ | วิธีติดตั้ง |
|---|---|
| **Windows** | ลง **Python install manager** จาก Microsoft Store หรือ `winget install 9NQ7512CXL7T` แล้วรัน `py install 3.14` · หรือโหลด **Windows installer (64-bit)** ของ 3.14 ตัวล่าสุดจาก [python.org](https://www.python.org/downloads/windows/) แล้วติ๊ก **"Add python.exe to PATH"** |
| **macOS** | `brew install python@3.14` (ยังไม่มี Homebrew: [brew.sh](https://brew.sh)) |
| **Linux** | ถ้า distro ไม่มี `python3.14` ให้ใช้[วิธีที่ 3 — Conda](#5-วิธีที่-3--conda) ง่ายกว่า |

---

## 2. เลือกวิธีติดตั้ง

| ถ้าคุณ... | ใช้วิธี |
|---|---|
| ใช้ Windows และไม่มี Conda | **วิธีที่ 1** |
| ใช้ Mac หรือ Linux | **วิธีที่ 2** |
| มี Conda อยู่แล้ว / ไม่อยากลง Python เอง | **วิธีที่ 3** |

ทุกวิธีลง library ชุดเดียวกันจาก [`backend/requirements.txt`](backend/requirements.txt) แล้วต้องลง PostgreSQL ตาม[หัวข้อ 6](#6-ติดตั้ง-postgresql-18)

---

## 3. วิธีที่ 1 — venv + pip (Windows)

```powershell
# 1) clone แล้วไปที่ branch develop
git clone https://github.com/boss2912/Smart-Fridge-Recipe-Planner.git
cd Smart-Fridge-Recipe-Planner
git switch develop

# 2) สร้าง virtual environment
py -3.14 -m venv .venv

# 3) activate
.\.venv\Scripts\Activate.ps1

# 4) อัปเดต pip ก่อน
python -m pip install --upgrade pip

# 5) ลง library ที่ล็อกไว้
pip install -r backend/requirements.txt
```

ถ้า `Activate.ps1` ขึ้น error เรื่อง execution policy → [หัวข้อ 9](#-activateps1-cannot-be-loaded-because-running-scripts-is-disabled)

ออกจาก venv: `deactivate`

---

## 4. วิธีที่ 2 — venv + pip (macOS / Linux)

```bash
# 1) clone แล้วไปที่ branch develop
git clone https://github.com/boss2912/Smart-Fridge-Recipe-Planner.git
cd Smart-Fridge-Recipe-Planner
git switch develop

# 2) สร้าง virtual environment
python3.14 -m venv .venv

# 3) activate
source .venv/bin/activate

# 4) อัปเดต pip
python -m pip install --upgrade pip

# 5) ลง library ที่ล็อกไว้
pip install -r backend/requirements.txt
```

ออกจาก venv: `deactivate`

---

## 5. วิธีที่ 3 — Conda

ใช้ได้เหมือนกันทั้ง Windows / macOS / Linux · Conda ลง Python 3.14 ให้เอง

```bash
# 1) clone แล้วไปที่ branch develop
git clone https://github.com/boss2912/Smart-Fridge-Recipe-Planner.git
cd Smart-Fridge-Recipe-Planner
git switch develop

# 2) สร้าง environment จาก environment.yml
conda env create -f environment.yml

# 3) activate
conda activate smartfridge
```

### คำสั่ง Conda ที่ใช้บ่อย

```bash
conda activate smartfridge                       # เข้า env
conda deactivate                                 # ออก
conda env update -f environment.yml --prune      # อัปเดตเมื่อ requirements.txt เปลี่ยน
conda env remove -n smartfridge                  # ลบ env ทิ้ง (พังก็สร้างใหม่ได้)
```

### ทำไม `environment.yml` ลง library ผ่าน `pip:`

[`environment.yml`](environment.yml) เอาแค่ `python` กับ `pip` จาก conda แล้วสั่ง `pip install -r backend/requirements.txt` · library จึงมาจากไฟล์เดียวกับวิธีที่ 1–2 แก้เวอร์ชันที่ `requirements.txt` ที่เดียว

---

## 6. ติดตั้ง PostgreSQL 18

ตอนนี้ยังไม่ต้องสร้าง database · Flask ยังไม่ต่อ PostgreSQL จนกว่า ER กับ schema จะเสร็จ (ROADMAP รอบ 2–5) · ลงไว้ก่อนแล้วเช็คว่า `psql` ใช้ได้

| ระบบ | วิธีติดตั้ง |
|---|---|
| **Windows** | `winget install PostgreSQL.PostgreSQL.18` หรือโหลด installer จาก [postgresql.org](https://www.postgresql.org/download/windows/) · ตอนติดตั้งจะให้ตั้งรหัสผ่านของ user `postgres` **จดไว้** · แล้วเพิ่ม `C:\Program Files\PostgreSQL\18\bin` เข้า PATH |
| **macOS** | `brew install postgresql@18` แล้ว `brew services start postgresql@18` · ตัวนี้ไม่ลิงก์เข้า PATH เอง ต้องเพิ่ม `$(brew --prefix)/opt/postgresql@18/bin` เข้า PATH |
| **Linux** | ใช้ repo ของ PostgreSQL ตาม [postgresql.org/download/linux](https://www.postgresql.org/download/linux/) แล้วลง `postgresql-18` |

### เช็คว่าใช้ได้

```bash
psql --version
# ควรได้: psql (PostgreSQL) 18.x
```

```bash
psql -U postgres -c "SELECT version();"
# ใส่รหัสผ่านที่ตั้งไว้ ต้องเห็นบรรทัดที่ขึ้นต้นด้วย PostgreSQL 18
```

macOS ที่ลงด้วย Homebrew ใช้ user ของเครื่องแทน `postgres`: `psql -d postgres -c "SELECT version();"`

---

## 7. ตรวจว่าติดตั้งสำเร็จ

activate venv หรือ conda env ก่อน แล้วรันจาก root ของ repo:

```bash
python -m pytest backend -v
```

ต้องได้ **17 passed** · เทสมี 2 ไฟล์

| ไฟล์ | ตรวจอะไร |
|---|---|
| [`backend/test_install.py`](backend/test_install.py) | Python เป็น 3.14 · library ทุกตัวตรงกับเวอร์ชันใน `requirements.txt` |
| [`backend/test_app.py`](backend/test_app.py) | Flask เปิดหน้าแรกได้ · ส่ง CSS จาก `frontend/static/` ได้ |

ถ้าไม่ผ่าน ข้อความบอกว่าอะไรไม่ตรง เช่น

```text
FAILED backend/test_install.py::test_python_version - AssertionError: ต้องใช้ Python 3.14 (ค่าที่ได้: 3.12)
FAILED backend/test_install.py::test_package_version[pytest-9.1.1] - AssertionError: pytest ต้องเป็น 9.1.1 (ค่าที่ได้: 9.2.0)
```

แก้: เช็คว่า activate env ถูกตัว แล้วลงใหม่ด้วย `pip install -r backend/requirements.txt`

---

## 8. รันโปรเจกต์

รันจาก root ของ repo (activate env ก่อน):

```bash
flask --app backend/app run --debug
```

แล้วเปิด http://127.0.0.1:5000 ต้องเห็นหน้า "Smart Fridge & Recipe Planner" · แก้ไฟล์แล้ว Flask โหลดใหม่เอง · หยุดด้วย `Ctrl+C`

### ไฟล์อยู่ตรงไหน

```text
backend/
├── app.py              โปรแกรม Flask + route
├── requirements.txt    library ที่ล็อกเวอร์ชันไว้
├── test_app.py         เทสหน้าเว็บ
└── test_install.py     เทสว่าติดตั้งถูก
frontend/
├── templates/          template HTML ที่ Flask เติมข้อมูล (base.html = โครงทุกหน้า)
└── static/css/         CSS · JS กับรูปใส่ static/ เหมือนกัน
```

### 🔴 ห้ามใช้ `--debug` คู่กับ `--host 0.0.0.0`

debugger ของ Flask **รันโค้ด Python จากหน้าเว็บได้** เมื่อเจอ error ถ้าเปิดให้เครื่องอื่นในวง LAN เข้าได้ด้วย ใครก็ยึดเครื่องคุณได้ · ตอนพัฒนาใช้ `127.0.0.1` (ค่าเดิม) พอ · ทดสอบ 2 เครื่องผ่าน Nginx ทำในรอบ 7 ([ROADMAP](docs/ROADMAP.md#-ปฏิทิน-9-รอบ-พุธ--อังคาร))

---

## 9. แก้ปัญหาที่เจอบ่อย

### ❌ `Activate.ps1 cannot be loaded because running scripts is disabled`

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

แล้ว activate ใหม่ · หรือใช้ `cmd` แทน: `.\.venv\Scripts\activate.bat`

---

### ❌ `py -3.14` ขึ้นว่าไม่พบ Python 3.14

ยังไม่ได้ลง 3.14 หรือลงแล้วแต่ `py` ไม่เห็น → `py --list` ดูว่ามีตัวไหน แล้วลงตาม[หัวข้อ 1](#ถ้ายังไม่มี-python-314) · ถ้าใช้ Python install manager สั่ง `py install 3.14`

---

### ❌ `ModuleNotFoundError: No module named 'flask'`

ลืม activate env หรือ activate ผิดตัว

```bash
python -c "import sys; print(sys.executable)"
```

ต้องชี้ไปที่ `.venv/` หรือ env `smartfridge` ของ conda ไม่ใช่ Python ของระบบ

---

### ❌ `UnicodeDecodeError` ตอน `pip install -r`

pip บน Windows อ่านไฟล์ด้วย codepage ของเครื่อง (ภาษาไทยคือ `cp874`) ถ้า `requirements.txt` มีตัวอักษรไทยจะพัง · ไฟล์นี้จึงเป็น **ASCII ล้วน** ห้ามใส่คอมเมนต์ภาษาไทย

---

### ❌ `Address already in use` / พอร์ต 5000 ถูกใช้อยู่

มีโปรแกรมอื่นใช้พอร์ต 5000 (macOS ใช้พอร์ตนี้กับ AirPlay Receiver) → เปลี่ยนพอร์ต:

```bash
flask --app backend/app run --debug --port 5001
```

---

### ❌ `psql` ขึ้นว่าไม่พบคำสั่ง

ลง PostgreSQL แล้วแต่ยังไม่ได้เพิ่มโฟลเดอร์ `bin` เข้า PATH → ดู[หัวข้อ 6](#6-ติดตั้ง-postgresql-18) · เพิ่มแล้วปิด terminal เปิดใหม่

---

## 10. ภาคผนวก — ชุดเวอร์ชันที่ล็อกไว้

### เลือกเวอร์ชันยังไง

กติกาเดียวกันทุกตัว: **ใช้รุ่นแก้บั๊กล่าสุด ของสายที่ออกมาแล้วอย่างน้อย 2 เดือน และไม่มีช่องโหว่ที่รู้** (ตรวจ 13 พ.ย. 2026 ด้วย `pip-audit` ไม่พบช่องโหว่)

| ของ | เวอร์ชัน | ทำไมเลือกตัวนี้ |
|---|---|---|
| Python | **3.14** | ยังได้รุ่นแก้บั๊กถึง ต.ค. 2027 · 3.12 กับ 3.13 เหลือแค่แก้ช่องโหว่ · 3.15 เพิ่งออก ต.ค. 2026 |
| PostgreSQL | **18** | ออก ก.ย. 2025 ดูแลถึง พ.ย. 2030 · ใช้ 18.x ตัวล่าสุด (รุ่นย่อยของ PostgreSQL แก้บั๊กอย่างเดียว) |
| Flask | 3.1.3 | รุ่นแก้ช่องโหว่ ก.พ. 2026 |
| Werkzeug | 3.1.9 | รุ่นแก้ช่องโหว่ ก.ย. 2026 |
| Jinja2 | 3.1.6 | ใช้มาตั้งแต่ มี.ค. 2025 |
| MarkupSafe | 3.0.4 | รุ่นแก้บั๊ก ต.ค. 2026 |
| itsdangerous | 2.2.0 | |
| click | 8.5.1 | รุ่นแก้บั๊กของสาย 8.5 (ส.ค. 2026) |
| blinker | 1.9.0 | |
| pytest | 9.1.1 | 9.2.0 เพิ่งออก 27 ต.ค. 2026 และมีของที่เปลี่ยนแบบใช้ของเดิมไม่ได้ |
| pluggy | 1.6.0 | ตัวที่ใช้คู่ pytest 9.1.1 ตอนออก · 1.7.0 เพิ่งออก ต.ค. 2026 |
| iniconfig | 2.3.1 | |
| packaging | 26.3 | |
| Pygments | 2.21.0 | |
| colorama | 0.4.6 | ลงเฉพาะ Windows |

### เวลาจะอัปเกรดเวอร์ชัน

1. แก้ pin ใน `backend/requirements.txt` ตามกติกาข้างบน · เปลี่ยน Python ต้องแก้ `environment.yml` กับ `backend/test_install.py` ด้วย
2. ลง env ใหม่จากศูนย์ (ลบ `.venv` แล้วสร้างใหม่) ไม่ใช่ `pip install -U` ทับ
3. รัน `python -m pytest backend` ต้องผ่านทั้งหมด
4. แก้ตารางข้างบนนี้
5. เปิด PR แยกสำหรับอัปเกรด อย่าปนกับงานอื่น

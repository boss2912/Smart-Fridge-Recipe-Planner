# Smart Fridge & Recipe Planner

<div align="center">
  <h3>🧊 Smart Fridge</h3>
  <p>ระบบตู้เย็นอัจฉริยะและแนะนำเมนูอาหาร · Smart fridge &amp; recipe planner database</p>
  <p><strong>310-2309 Database Systems · Mini-DB Group Project · CDTI</strong></p>

  <img src="https://img.shields.io/badge/stage-1%20Proposal%20done-brightgreen" alt="Stage 1 Proposal done">
  <img src="https://img.shields.io/badge/DBMS-PostgreSQL-336791" alt="DBMS PostgreSQL">
</div>

---

## 📌 สถานะปัจจุบัน (13 พ.ย. 2026)

> **ขั้นที่ 1 Proposal ส่งแล้ว** ใช้หัวข้ออันดับ 1 — ขั้นต่อไปคือขั้น 2 ER Diagram & Relational Schema (ดู [`docs/ROADMAP.md`](docs/ROADMAP.md))

| ขั้น | งานที่ต้องส่ง (Lecture 1 หน้า 11) | สถานะ |
|---|---|---|
| 1 | Project Proposal (Topic & Idea) | ✅ ส่งแล้ว → [`docs/proposal.md`](docs/proposal.md) |
| 2 | ER Diagram & Relational Schema | 🟡 กฎของระบบเสร็จแล้ว · ER เริ่มรอบ 1 (18 พ.ย.) → [`design/`](design/) |
| 3 | SQL Implementation Script | ⬜ ยังไม่เริ่ม · ใช้ PostgreSQL → [`database/`](database/) |
| 4 | Final Report & Presentation | ⬜ ยังไม่เริ่ม → [`report/`](report/) |

ตัดสินแล้ว: ใช้ PostgreSQL ([ADR-005](docs/DECISIONS.md#adr-005--เลือก-dbms)) · แบ่งงาน 7 คน → [`docs/TEAM_AND_WORKFLOW.md`](docs/TEAM_AND_WORKFLOW.md) · เว็บใช้ Python + Flask และวิธีรัน ([ADR-009](docs/DECISIONS.md#adr-009--เลือกภาษาและวิธีรันเว็บแอป)) · กติกา branch → [`CONTRIBUTING.md`](CONTRIBUTING.md)

---

## 🎯 Smart Fridge คืออะไร

หลายครัวเรือนใช้ระบบนี้ร่วมกัน ของที่ซื้อเข้าตู้ สมาชิกแต่ละบ้านจะบันทึกเป็นล็อต พร้อมวันซื้อ วันหมดอายุ และจำนวน จากนั้นระบบก็เตือนของที่ใกล้หมดอายุ และแนะนำเมนูที่ทำได้จากของที่ยังเหลืออยู่ในตู้

### ของในตู้เข้าทางเดียว ออกได้สองทาง

```text
ซื้อ ──► ล็อตในตู้ (วันซื้อ / วันหมดอายุ / จำนวน)
            │
            ├──► ทำอาหาร ──► ระบบหักวัตถุดิบตามสูตร
            │
            └──► ทิ้ง (หมดอายุหรือเสีย) ──► หักจากล็อตนั้น และเก็บประวัติการทิ้ง
```

จำนวนในตู้จึงเท่ากับของที่ซื้อ หักของที่ใช้ทำอาหาร และหักของที่ทิ้ง ถ้าไม่บันทึกทางออกทางใดทางหนึ่ง จำนวนในตู้จะมากกว่าของจริงไปเรื่อยๆ ระบบก็จะแนะนำเมนูที่ของหมดไปแล้ว

### ผู้ใช้ 2 กลุ่ม

| ผู้ใช้ | ทำอะไรได้ |
|---|---|
| สมาชิกในครัวเรือน | เพิ่มวัตถุดิบและสูตรของบ้านตัวเอง · บันทึกของที่ซื้อเข้าตู้ · บันทึกว่าทำเมนูไหน · บันทึกของที่ทิ้ง · ดูคำเตือนและเมนูที่ทำได้ |
| ผู้ดูแลระบบ | ดูบ้านทุกบ้านและของในตู้ (ดูอย่างเดียว) · ปิด / เปิดบัญชีบ้าน · ดูภาพรวมทุกบ้าน ([ADR-015](docs/DECISIONS.md#adr-015--ผู้ดูแลระบบดูได้ทุกบ้านและปิดบัญชีบ้านได้)) |

### ข้อมูลหลัก 8 อย่าง

1. ข้อมูลครัวเรือน (บัญชีบ้าน)
2. บัญชีผู้ดูแลระบบ
3. ข้อมูลหมวดหมู่และวัตถุดิบ (หน่วยมาตรฐาน · ของแต่ละบ้าน)
4. ข้อมูลของในตู้แต่ละล็อต (วันซื้อ/วันหมดอายุ/จำนวน)
5. ข้อมูลสูตรอาหาร (ของแต่ละบ้าน)
6. วัตถุดิบที่ใช้ในแต่ละสูตร (ปริมาณ)
7. ประวัติการทำอาหาร (จำนวนเท่า · หักล็อตไหนไปเท่าไร)
8. ประวัติการทิ้งของ (ล็อต/จำนวน/วันที่ทิ้ง)

ต่างจาก proposal ที่ส่งไป: ไม่เก็บข้อมูลสมาชิก ([ADR-010](docs/DECISIONS.md#adr-010--บ้านหนึ่งมีบัญชีเดียว-ทุกคนในบ้านใช้ร่วมกัน)) · เพิ่มบัญชีผู้ดูแลระบบ ([ADR-015](docs/DECISIONS.md#adr-015--ผู้ดูแลระบบดูได้ทุกบ้านและปิดบัญชีบ้านได้)) · วัตถุดิบและสูตรเป็นของแต่ละบ้าน ([ADR-016](docs/DECISIONS.md#adr-016--บ้านเพิ่มวัตถุดิบและสูตรของตัวเอง))

รายการซื้อของกับราคาสินค้าไม่อยู่ในขอบเขต เหตุผลอยู่ใน [`docs/DECISIONS.md`](docs/DECISIONS.md)

---

## 🏗️ สถาปัตยกรรม — Distributed System

ระบบแบ่งเป็น 4 ส่วน คือ Nginx (ทางเข้า) · frontend (หน้าเว็บ) · backend (Flask) · database (DBMS) ผู้ใช้ทั้ง 2 กลุ่มเข้าใช้ผ่านเบราว์เซอร์ · frontend กับ backend รันเป็นโปรแกรม Flask ตัวเดียว · วันนำเสนอใช้ 2 เครื่อง: เครื่อง 1 Nginx · เครื่อง 2 Flask + PostgreSQL ([ADR-009](docs/DECISIONS.md#adr-009--เลือกภาษาและวิธีรันเว็บแอป))

```text
        Browser (สมาชิกในครัวเรือน / ผู้ดูแลระบบ)
                          │
                          ▼
                 ┌─────────────────┐
                 │      Nginx      │  ทางเข้าเดียว · เครื่อง 1
                 └────────┬────────┘
                          ▼
     ┌──────────────────────────────────────────┐
     │  Flask (Python)                          │  เครื่อง 2 · frontend กับ backend อยู่ในโปรแกรมเดียว
     │  ┌───────────────┐   ┌───────────────┐   │
     │  │   frontend    │◄──│    backend    │   │
     │  │  HTML CSS JS  │   │  route login  │   │
     │  └───────────────┘   └───────┬───────┘   │
     └──────────────────────────────┼───────────┘
                                    ▼
                           ┌─────────────────┐
                           │    database     │  PostgreSQL · เครื่อง 2
                           └─────────────────┘
```

### แต่ละส่วนต้องมีอะไร

| ส่วน | ต้องมี |
|---|---|
| **Nginx** | ทางเข้าเดียวของระบบ: ส่งต่อทุกคำขอไปที่ Flask · ส่งไฟล์ CSS / JS / รูป ให้เบราว์เซอร์เองได้ |
| **frontend** | หน้าของสมาชิกในครัวเรือน: เพิ่มวัตถุดิบและสูตร · บันทึกของที่ซื้อเข้าตู้ (ตะกร้า) · บันทึกว่าทำเมนูไหน (+ เครื่องปรุงเพิ่มเติม) · บันทึกของที่ทิ้ง · ดูของใกล้หมดอายุ · ดูเมนูที่ทำได้<br>หน้าของผู้ดูแลระบบ: ดูบ้านทุกบ้านและของในตู้ · ปิด / เปิดบัญชีบ้าน · dashboard ภาพรวมทุกบ้าน<br>เขียนเป็น template HTML + CSS ที่ Flask ส่ง · JavaScript เฉพาะที่จำเป็น ([ADR-009](docs/DECISIONS.md#adr-009--เลือกภาษาและวิธีรันเว็บแอป)) |
| **backend** | route ของ Flask ที่ส่งหน้าเว็บและรับฟอร์ม · ล็อกอิน (บ้านที่ถูกปิดล็อกอินไม่ได้) · แยกสิทธิ์ 2 กลุ่ม: บ้านเห็นและแก้ได้เฉพาะวัตถุดิบ สูตร และของในตู้ของบ้านตัวเอง · ผู้ดูแลระบบเห็นทุกบ้านแต่แก้ไม่ได้ ปิด / เปิดบัญชีบ้านได้ ([ADR-003](docs/DECISIONS.md#adr-003--ต้องมีการบันทึกการทิ้งของ) · [ADR-015](docs/DECISIONS.md#adr-015--ผู้ดูแลระบบดูได้ทุกบ้านและปิดบัญชีบ้านได้)) |
| **database** | ข้อมูลหลัก 8 อย่าง · PK / FK / NOT NULL / UNIQUE ตามตัวอย่างหน้า 31 · query 4 เรื่องใน [`database/`](database/) ซึ่งทำอาหารกับทิ้งของต้องอยู่ในธุรกรรมเดียว ([ADR-001](docs/DECISIONS.md#adr-001--ทำอาหารแล้วระบบหักวัตถุดิบตามสูตร) · [ADR-003](docs/DECISIONS.md#adr-003--ต้องมีการบันทึกการทิ้งของ)) · ใช้ PostgreSQL ([ADR-005](docs/DECISIONS.md#adr-005--เลือก-dbms)) |

> งานส่ง 4 ชิ้นของอาจารย์ (Lecture 1 หน้า 11) ไม่มีหน้าเว็บหรือ API ส่วน Nginx · frontend · backend จึงเป็นงานเพิ่มนอกงานส่ง เริ่มพร้อมขั้น 2 ([ADR-008](docs/DECISIONS.md#adr-008--ทำเป็นเว็บแอปที่ใช้งานได้จริง))

---

## 👥 ทีม (7 คน)

| ชื่อ - นามสกุล | รหัสนักศึกษา |
|---|---|
| พงศภัค เทียบพิมพ์ | 6710301006 |
| พชรพล เสรีกุล | 6710301005 |
| พีระพัส อัครศรีประไพ | 6710301008 |
| เจตน์ - | 6710301022 |
| ภากร กาเงิน | 6710301037 |
| วิรัชสัณห์ เจนนานาโชค | 6710301047 |
| คชา สวัสดิพิศาล | 6710301054 |

รายละเอียดหน้าที่และจุดที่ต้องคุยกันก่อนลงมือ → [`docs/TEAM_AND_WORKFLOW.md`](docs/TEAM_AND_WORKFLOW.md)

---

## 📁 โครงสร้างโปรเจกต์

```text
Smart-Fridge-Recipe-Planner/
├── docs/       ขั้น 1 Proposal + ข้อกำหนดอาจารย์
├── design/     ขั้น 2 ER Diagram + Schema
├── database/   ขั้น 3 SQL · ส่วน database
├── report/     ขั้น 4 รายงาน + สไลด์
├── nginx/      ส่วน Nginx · ทางเข้าเดียว
├── frontend/   ส่วน frontend · หน้าเว็บ
├── backend/    ส่วน backend · Flask + ล็อกอิน
└── .github/    แม่แบบ PR + issue
```

**ทุกโฟลเดอร์ยกเว้น `docs/` กับ `.github/` มี `README.md` ของตัวเอง** บอกว่าใส่อะไร ใครดูแล และอ้างอิงสไลด์หน้าไหน

โครง repo ดัดแปลงจาก [luma-webapp-g04](https://github.com/boss2912/luma-webapp-g04)

---

## 📚 เอกสารที่ต้องอ่าน

| ไฟล์ | อ่านเมื่อ |
|---|---|
| ⭐ [`docs/COURSE_REQUIREMENTS.md`](docs/COURSE_REQUIREMENTS.md) | **อ่านก่อนเริ่มทุกงาน** — ข้อกำหนดและเกณฑ์คะแนนจากอาจารย์ พร้อมเลขหน้าสไลด์ |
| [`docs/proposal.md`](docs/proposal.md) | อยากรู้ว่ากลุ่มเสนอระบบอะไรไป |
| [`docs/ROADMAP.md`](docs/ROADMAP.md) | อยากรู้ว่าตอนนี้อยู่ขั้นไหน ต่อไปทำอะไร |
| [`docs/DECISIONS.md`](docs/DECISIONS.md) | **ก่อนแก้อะไรที่ดูแปลก** — บันทึกว่าทำไมถึงตัดสินใจแบบนั้น |
| [`docs/TEAM_AND_WORKFLOW.md`](docs/TEAM_AND_WORKFLOW.md) | แบ่งงาน · จุดที่ต้องตกลงกันก่อนลงมือ |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | ก่อน commit หรือเปิด PR ครั้งแรก |
| [`INSTALL.md`](INSTALL.md) | ติดตั้ง — Windows · macOS · Linux · Conda · PostgreSQL 18 · แก้ปัญหา |

---

## 🚀 การติดตั้ง

📖 **คู่มือเต็ม → [`INSTALL.md`](INSTALL.md)** (Windows · macOS · Linux · Conda · PostgreSQL 18 · แก้ปัญหา)

**Python 3.14** · ทุกเวอร์ชันล็อกไว้ใน [`backend/requirements.txt`](backend/requirements.txt) — ตรวจด้วย `python -m pytest backend` ต้องได้ 17 passed

### ติดตั้งเร็วสุด (dev บนเครื่องเดียว)

**Windows**
```powershell
git clone https://github.com/boss2912/Smart-Fridge-Recipe-Planner.git
cd Smart-Fridge-Recipe-Planner
git switch develop
py -3.14 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r backend/requirements.txt
```

**macOS / Linux**
```bash
git clone https://github.com/boss2912/Smart-Fridge-Recipe-Planner.git
cd Smart-Fridge-Recipe-Planner
git switch develop
python3.14 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r backend/requirements.txt
```

**Conda** (ใช้ได้ทุกระบบ)
```bash
git clone https://github.com/boss2912/Smart-Fridge-Recipe-Planner.git
cd Smart-Fridge-Recipe-Planner
git switch develop
conda env create -f environment.yml
conda activate smartfridge
```

### รัน

```bash
flask --app backend/app run --debug
```

เปิด http://127.0.0.1:5000 · ตอนพัฒนารัน Flask ตรง ไม่ผ่าน Nginx · ยังไม่ต่อ database (รอ ER) แต่ให้ลง PostgreSQL 18 ไว้ก่อนรอบ 2 ตาม[หัวข้อ 6 ของ INSTALL.md](INSTALL.md#6-ติดตั้ง-postgresql-18)

---

## 🌿 Git Workflow

```text
main ──────────────────────────────●  ฉบับส่งอาจารย์เท่านั้น
                                   ↑ PR
develop ───●───●───●───●───●───●───●  รวมงานทุกคน ตรวจก่อนเข้า main
           ↑       ↑       ↑
      branch งานแต่ละชิ้น (ตั้งชื่อตามเลข issue)
```

- งานทุกอย่างทำบน branch ของตัวเอง แล้วเปิด PR เข้า `develop`
- ต้องมีคนอื่นรีวิวอย่างน้อย 1 คนก่อน merge

กติกาเต็มอยู่ใน [`CONTRIBUTING.md`](CONTRIBUTING.md) (แจ้งทีมในประชุมครั้งที่ 1) · ตั้งป้องกัน main กับ develop บน GitHub แล้ว

---

## 🎓 เกณฑ์ให้คะแนน (Lecture 1 หน้า 4)

| หัวข้อ | % |
|---|---|
| **Mini DB Group Project** | **20** |
| In-class check up and assignment | 20 |
| Mid-Term and/or Final Exam and/or unannounced quiz | 60 |

สไลด์ใช้คำว่า *Tentative* สัดส่วนนี้จึงยังเปลี่ยนได้ ส่วนคะแนน 20% ของโครงงานแบ่งเป็นนำเสนอ 10 · งาน 10 ([`docs/COURSE_REQUIREMENTS.md`](docs/COURSE_REQUIREMENTS.md#1-เงื่อนไขการให้คะแนน))

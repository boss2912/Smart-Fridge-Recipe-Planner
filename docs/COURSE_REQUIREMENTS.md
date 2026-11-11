# ข้อกำหนดโครงงานจากอาจารย์ — 310-2309 Database Systems

> สกัดจากสไลด์ `Lecture 1 - Introduction.pdf` (33 หน้า, Version 2026-2) และแบบฟอร์มนำเสนอโครงงานเวอร์ชัน 10 พ.ย. 69
> **นี่คือเอกสารอ้างอิงหลักของโปรเจกต์** — ทุก issue และทุก PR ต้องอ้างกลับมาที่นี่ได้

ทุกข้ออ้างเลขหน้าจริงในไฟล์ PDF ตรวจย้อนได้ เรื่องที่อาจารย์ยังไม่ได้บอก รวมไว้ที่หัวข้อ [5. ยังไม่รู้](#5-ยังไม่รู้--ต้องถามอาจารย์)

---

## 1. เงื่อนไขการให้คะแนน

**Lecture 1 หน้า 4** — Tentative Grading Method

| หัวข้อ | ร้อยละ |
|---|---|
| **Mini DB Group Project** | **20** |
| In-class check up and assignment | 20 |
| Mid-Term and/or Final Exam and/or unannounced quiz | 60 |

- คำว่า *Tentative* แปลว่าสัดส่วนนี้ยังเปลี่ยนได้
- ควิซที่ไม่บอกล่วงหน้า (unannounced quiz) อยู่ในก้อน 60%
- คะแนนโครงงาน 20% จะแบ่งให้แต่ละขั้นเท่าไร **อาจารย์ยังไม่ได้บอก**

---

## 2. ข้อกำหนดของโครงงาน

### 2.1 เป้าหมายและขนาดกลุ่ม

| ข้อกำหนด | สไลด์เขียนว่า | หน้า |
|---|---|---|
| เป้าหมาย | Design and implement a database system for a real-world scenario. | 11 |
| ขนาดกลุ่ม | 6 students per group. | 11 |
| ตั้งกลุ่ม | Form your group (6 members). | 12 |

### 2.2 งานที่ต้องส่ง 4 ชิ้น

**Lecture 1 หน้า 11** — Key Deliverables

| ขั้น | Key Deliverable | อยู่ในโปรเจกต์นี้ที่ |
|---|---|---|
| 1 | Project Proposal (Topic & Idea) | [`proposal.md`](proposal.md) |
| 2 | ER Diagram & Relational Schema | [`../design/`](../design/) |
| 3 | SQL Implementation Script | [`../database/`](../database/) |
| 4 | Final Report & Presentation | [`../report/`](../report/) |

### 2.3 ลำดับเนื้อหาที่งานต้องเดินตาม

**Lecture 1 หน้า 10** — Tentative Course Roadmap

```text
Phase 1  Database Design
         - Conceptual & Logical Design (ER & Relational Models)
         - Database Normalization
Phase 2  Database Implementation
         - SQL DDL, DML, Advanced Queries & Join
Phase 3  Mini-Project
         - Consultation & Final Presentation
```

หน้า 5 เรียงหัวข้อแบบเดียวกัน คือ Introduction → ER Model → Relational Model → Normalization → SQL → Mini-DB group project

### 2.4 ขั้นที่ 1 — Proposal

**Lecture 1 หน้า 12** — Brainstorming Your Domain

- เลือกหัวข้อที่สนใจ 3 หัวข้อ (*Pick 3 potential domains you are interested in.*)
- ตัวอย่างหัวข้อที่อาจารย์ยก: Cinema Booking, Gym Membership, Online Clothing Store, Parking Management
- กำหนดส่ง: *"Submit your top 3 choices by the end of today's class +1."* — ยังไม่ชัดว่านับจากคาบไหน ดูหัวข้อ 5

**แบบฟอร์มนำเสนอโครงงาน mini-DB group project เวอร์ชัน 10 พ.ย. 69** (Google Form)

| ช่อง | อาจารย์ให้ใส่อะไร |
|---|---|
| 1. Group Name | ชื่อทีมภาษาอังกฤษ ใช้คำสุภาพ เขียนแบบ CamelCase เช่น `TitanTheGreat` |
| 2. Group Members | สมาชิกทุกคน บรรทัดละคน รูปแบบ `ชื่อ นามสกุล, รหัสนักศึกษา, อีเมล` ใส่อีเมลเฉพาะหัวหน้าทีมซึ่งอยู่บรรทัดแรก คนอื่นใส่ `null` |
| 3. Proposed Topics | ชื่อระบบหรือชื่อธุรกิจ เช่น ระบบจองตั๋วโรงภาพยนตร์ (Cinema Booking System) |
| 4. Business Overview | อธิบายการทำงานของระบบในฝัน 2–3 ประโยค ใครทำอะไรได้บ้าง |
| 5. Key Users | ผู้ใช้หลัก เช่น 1. ลูกค้าทั่วไป, 2. พนักงานเคาน์เตอร์, 3. ผู้จัดการโรงหนัง |
| 6. Core Data | ข้อมูลสำคัญที่ระบบต้องบันทึก เช่น ข้อมูลภาพยนตร์, ข้อมูลโรงหนังและที่นั่ง, รอบฉาย, ข้อมูลลูกค้า, ประวัติการจอง |
| อันดับ 2 และ 3 | เขียนช่อง 3–6 ซ้ำสำหรับหัวข้อที่เหลือ |

> รายชื่อสมาชิกจริงไม่เก็บใน repo นี้ เพราะ repo เป็นสาธารณะ — ดู [ADR-006](DECISIONS.md#adr-006--รายชื่อสมาชิกไม่ขึ้น-repo-สาธารณะ)

### 2.5 ขั้นที่ 2 — ER Diagram & Relational Schema

- เครื่องมือที่อาจารย์ใช้: **draw.io** (หน้า 13)
- เนื้อหาที่ต้องใช้: Conceptual & Logical Design (ER & Relational Models) และ Database Normalization (หน้า 10)

### 2.6 ขั้นที่ 3 — SQL Implementation Script

- เนื้อหาที่ต้องใช้: SQL DDL, DML, Advanced Queries & Join (หน้า 10)
- DBMS: หน้า 9 ยกตัวอย่าง MySQL, PostgreSQL, Oracle, SQL Server แต่ไม่ได้บอกว่าโครงงานต้องใช้ตัวไหน กลุ่มจึงยังไม่เลือก ดู [ADR-005](DECISIONS.md#adr-005--เลือก-dbms)

### 2.7 ขั้นที่ 4 — Final Report & Presentation

- Phase 3 มี Consultation กับ Final Presentation (หน้า 10)
- รูปแบบรายงาน ความยาว และเวลานำเสนอ อาจารย์ยังไม่ได้บอก

---

## 3. ตัวอย่าง DB Requirement ของอาจารย์ (Lecture 1 หน้า 14–32)

สไลด์มีตัวอย่างการเขียน requirement 4 ระบบ แต่ละระบบมีกรอบเปล่าไว้วาด ER ในห้อง ตัวอย่างพวกนี้**ไม่ใช่ข้อกำหนดของโครงงานโดยตรง** แต่เป็นแบบที่ดีสำหรับเขียนกฎของ Smart Fridge

| ตัวอย่าง | หน้า requirement | หน้ากรอบ ER |
|---|---|---|
| mini-Instagram | 15–16 | 17 |
| mini-Facebook | 19–20 | 21 |
| University DB | 23–24 | 25 และ 26 (alternative solution) |
| Online Clothing Store | 28–31 | 32 |

ตัวอย่างร้านเสื้อผ้า (หน้า 28–31) ละเอียดที่สุด แบ่งเป็น 3 ส่วน คือ System Overview → Business Rules → Data Integrity & Constraints

**Data Integrity & Constraints ในตัวอย่างร้านเสื้อผ้า (หน้า 31)**

| ข้อ | สไลด์เขียนว่า |
|---|---|
| Primary Keys | Every table must have a designated Primary Key (PK). |
| Foreign Keys | Proper Foreign Keys (FK) must be enforced to maintain Referential Integrity. |
| Nullability | Essential fields like Email, Product Name, and Order Total cannot be NULL. |
| Uniqueness | User Emails must be unique across the system. |

> หน้า 29 มีคำใบ้ว่ากฎข้อหนึ่งตั้งใจบังคับให้ต้องสร้าง associative entity (ProductVariant)
> กฎของระบบที่ดีจึงไม่ได้บอกแค่ว่ามีข้อมูลอะไร แต่บอกด้วยว่าข้อมูลสัมพันธ์กันแบบไหน

---

## 4. ขอบเขตเนื้อหาวิชา (Lecture 1 หน้า 2 และ 5)

หน้า 2 เป็นคำอธิบายรายวิชา มีหัวข้อสีจาง 5 เรื่อง คือ การออกแบบฐานข้อมูลทางกายภาพ · ฐานข้อมูลแบบกระจาย · การบริหารจัดการระบบฐานข้อมูลขนาดใหญ่ · การรวมแหล่งข้อมูลจากหลายระบบ · การประมวลผลข้อมูลแบบกระแส หัวข้อพวกนี้อาจารย์บอกในห้องว่ายังไม่สอนตอนนี้ ถ้ามีเวลาจะกลับมาสอน

หัวข้อที่โครงงานต้องใช้ตามหน้า 5 คือ ER → Relational → Normalization → SQL

---

## 5. ยังไม่รู้ — ต้องถามอาจารย์

| เรื่อง | ที่รู้ตอนนี้ |
|---|---|
| กำหนดส่ง Proposal | หน้า 12 เขียนแค่ "by the end of today's class +1" ไม่บอกว่านับจากคาบไหน และ +1 คือ 1 วันหรือ 1 คาบ |
| คะแนน 20% แบ่งให้แต่ละขั้นเท่าไร | ไม่มีในสไลด์ |
| กำหนดส่งขั้น 2–4 | ไม่มีในสไลด์ |
| ต้องใช้ DBMS ตัวไหน | หน้า 9 ยกตัวอย่าง 4 ตัว แต่ไม่ได้กำหนด |
| รูปแบบรายงานและเวลานำเสนอ | ไม่มีในสไลด์ |

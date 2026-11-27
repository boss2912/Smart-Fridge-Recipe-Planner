# report/ — Final Report + Presentation

👤 ทุกคน (ภูมิ · แบงค์ · บอส · ภีม · กก · เจตน์ · ไอน์) · งานในโฟลเดอร์นี้: รายงาน + สไลด์นำเสนอ (ทุกคนเขียนส่วนของตัวเอง) — ดู [`../docs/TEAM_AND_WORKFLOW.md`](../docs/TEAM_AND_WORKFLOW.md)

> ⬜ **ขั้น 4 ยังไม่เริ่ม** — ร่างรายงานและสไลด์ในรอบที่ 8–9 (6–15 ม.ค.) · โครงรายงานตกลงไว้ข้างล่างแล้วตาม [#14](https://github.com/boss2912/Smart-Fridge-Recipe-Planner/issues/14)

## หน้าที่

เก็บงานขั้นที่ 4 ตาม Key Deliverables (Lecture 1 หน้า 11) คือ **Final Report & Presentation**

## ที่รู้ตอนนี้

- Phase 3 ของวิชามี Consultation กับ Final Presentation (Lecture 1 หน้า 10)
- นำเสนอ 15–20 นาที · คะแนนโครงงาน 20% แบ่งเป็นนำเสนอ 10 งาน 10 ([`COURSE_REQUIREMENTS.md`](../docs/COURSE_REQUIREMENTS.md#5-ยังไม่รู้--ต้องถามอาจารย์))
- รายงานไม่มีแบบบังคับ กลุ่มกำหนดหัวข้อเอง · ใช้โครงรายงานวิชา 311-3303 Embedded System Design (ต้นแบบ 2 ฉบับ: `Lab_Report_ADC_SAR_Program13-1.pdf` และ `Lab_Report_DoubleDabble_7Seg.pdf`) เป็นฐานด้านการจัดโครงสร้างและวิธีอ้างหลักฐาน แล้วปรับหัวข้อกลางให้ตรงกับวงจรออกแบบฐานข้อมูลตามสไลด์ Lecture 1 และตำราฐานข้อมูล

---

## 1. เทียบต้นแบบวิชา 311-3303 กับงานฐานข้อมูล

ต้นแบบทั้ง 2 ฉบับจากวิชา 311-3303 ใช้โครง 10 หัวข้อ โดยหัวข้อ 1–3 และ 8–10 เป็นโครงมาตรฐาน ส่วนหัวข้อ 4–7 เป็นพื้นที่งานจริงของวิชานั้น ตารางนี้แยกให้เห็นว่าหัวข้อไหนใช้ต่อได้และหัวข้อไหนต้องเปลี่ยนสำหรับงานฐานข้อมูล:

| หัวข้อในต้นแบบ 311-3303 (`ADC SAR` · `Double Dabble`) | สถานะ | การปรับใช้กับ Smart Fridge (310-2309) |
|---|---|---|
| 1. วัตถุประสงค์ (Objective) | **คงไว้ + ขยาย** | รวมที่มา ปัญหาของระบบเดิม ขอบเขตระบบ และกลุ่มผู้ใช้ 2 กลุ่มจาก [`docs/proposal.md`](../docs/proposal.md) |
| 2. ทฤษฎีที่เกี่ยวข้อง (Related Theory) | **ปรับเนื้อหา** | เปลี่ยนจากทฤษฎีฮาร์ดแวร์/ADC เป็นทฤษฎีฐานข้อมูลตาม Lecture 1 หน้า 5: ER Model · Relational Model · Normalization (1NF–3NF) · SQL DDL/DML และ ACID Transaction |
| 3. อุปกรณ์และเครื่องมือที่ใช้ | **ปรับชื่อและเนื้อหา** | เปลี่ยนเป็น **เครื่องมือและสถาปัตยกรรมระบบ** (PostgreSQL 18 · Python + Flask · Nginx · Docker Compose · draw.io · Git/GitHub) |
| 4. การออกแบบวงจร | **เปลี่ยนใหม่** | แทนด้วย **ข้อกำหนดและกฎของระบบ (Business Rules)** + **การออกแบบเชิงแนวคิด (ER Diagram)** (ตรงกับ Phase 1 ของ Lecture 1) |
| 5. การออกแบบโปรแกรม | **เปลี่ยนใหม่** | แทนด้วย **การออกแบบเชิงตรรกะและ Normalization** (แปลง ER → Relational Schema · PK/FK · Functional Dependencies · 1NF → 2NF → 3NF และข้อกำหนด Data Integrity) |
| 6. ผลการจำลอง | **เปลี่ยนใหม่** | แทนด้วย **การสร้างฐานข้อมูลและคำสั่ง SQL** (DDL สร้างตารางพร้อม constraint · ข้อมูลตัวอย่าง `seeds/` · query สำคัญ: JOIN, GROUP BY, Transaction หักล็อต/คืนล็อต) |
| 7. การเปรียบเทียบ | **เปลี่ยนใหม่** | แทนด้วย **การเชื่อมเว็บแอปและผลการทดสอบ** (ผังหน้าเว็บ 2 กลุ่มผู้ใช้ · ทดสอบกรณีผิดกฎและกรณีขอบเขต · เดโม 2 เครื่องผ่าน Nginx) |
| 8. ปัญหาที่พบระหว่างการทดลองและวิธีแก้ไข | **คงไว้ + เพิ่ม ADR** | เก็บจุดแข็งของต้นแบบ 311-3303 คือ **ตารางปัญหา–สาเหตุเชิงกลไก–วิธีแก้** และเพิ่ม **ตารางเปรียบเทียบทางเลือกการออกแบบ (ADR)** จาก [`docs/DECISIONS.md`](../docs/DECISIONS.md) พร้อมระบุข้อเสียของทางที่เลือกด้วย |
| 9. สรุปผลการทดลอง (Conclusion) | **คงไว้ + เพิ่มแนวทางต่อยอด** | สรุปผลเทียบวัตถุประสงค์ ข้อจำกัดของระบบปัจจุบัน และแนวทางพัฒนาต่อในอนาคต |
| 10. เอกสารอ้างอิง (References) | **คงไว้ + เพิ่มภาคผนวก** | อ้างอิงสไลด์อาจารย์ ตำราฐานข้อมูล เอกสารทางการของ PostgreSQL/Flask/Nginx และเพิ่ม **ภาคผนวก** สำหรับสคริปต์ SQL เต็มชุดและพจนานุกรมข้อมูล (Data Dictionary) |

---

## 2. โครงรายงานฉบับใช้จริงของกลุ่ม (10 บท + ภาคผนวก)

โครงนี้เรียงตามลำดับ **Database Design Lifecycle** (Requirements → Conceptual → Logical/Normalization → Physical SQL → Integration & Testing) เพื่อให้ครอบคลุม **Key Deliverables ทั้ง 4 ชิ้น** ใน Lecture 1 หน้า 11 และลำดับเนื้อหา 3 Phase ในหน้า 10 ครบทุกจุด:

| บท | ชื่อบท (ไทย / อังกฤษ) | เนื้อหาหลักที่ต้องมี | ที่มา (ต้นแบบ / แหล่งอ้างอิง) | ตรงกับงานส่ง (Lecture 1 หน้า 11) | หลักฐานใน repo & คนรับผิดชอบ |
|---|---|---|---|---|---|
| **ปก + สารบัญ** | หน้าปก · บทคัดย่อ · สารบัญ / สารบัญรูป / สารบัญตาราง | ชื่อโครงงาน รหัสนักศึกษาทั้ง 7 คน (ตาม ADR-007) รายวิชา และบทคัดย่อสั้นไม่เกินครึ่งหน้า | ต้นแบบ 311-3303 + รูปแบบรายงานวิชาการทั่วไป | ขั้น 4 | บอส (จัดรวมเล่ม) |
| **1** | บทนำ (Introduction & Project Proposal) | ที่มาและปัญหาของอาหารหมดอายุในครัวเรือน · วัตถุประสงค์ · ขอบเขตและสิ่งที่ไม่อยู่ในขอบเขต (ADR-002) · กลุ่มผู้ใช้ 2 กลุ่ม (บ้าน · ผู้ดูแลระบบ) · ข้อมูลหลัก 8 อย่าง | ต้นแบบ 311-3303 (ข้อ 1) · Lecture 1 หน้า 11–12 · Elmasri Ch. 3 | **ชิ้นที่ 1: Proposal** | [`docs/proposal.md`](../docs/proposal.md) · บอส |
| **2** | ทฤษฎีและเครื่องมือที่ใช้ (Related Theory, Tools & System Architecture) | ทฤษฎี ER / Relational / 1NF–3NF / ACID Transaction แบบกระชับ · เหตุผลที่เลือก PostgreSQL 18, Python + Flask, Nginx, Docker Compose · ผังสถาปัตยกรรม 1 เครื่อง (พัฒนา) และ 2 เครื่อง (เดโม) | ต้นแบบ 311-3303 (ข้อ 2–3) · Lecture 1 หน้า 5, 9 · Silberschatz Ch. 6–7 | พื้นฐานขั้น 2–3 | [`docs/DECISIONS.md`](../docs/DECISIONS.md) · [`INSTALL.md`](../INSTALL.md) · บอส + ทีม |
| **3** | ข้อกำหนดและกฎของระบบ (Requirements Analysis & Business Rules) | ภาพรวมระบบ · กฎของระบบข้อ 2.1–2.10 · ตารางกฎความถูกต้องของข้อมูล (PK, FK, NOT NULL, UNIQUE, CHECK, ของบ้านเดียวกัน) แยกให้ชัดว่าข้อไหนบังคับที่ฐานข้อมูล ข้อไหนบังคับที่ backend | Lecture 1 หน้า 28–31 (ตัวอย่างร้านเสื้อผ้า) · Silberschatz Ch. 6 · รูบริกรายงาน DB | **ชิ้นที่ 2: ER & Schema** | [`design/business-rules.md`](../design/business-rules.md) · ภูมิ · แบงค์ · บอส · ภีม |
| **4** | การออกแบบเชิงแนวคิด (Conceptual Design — ER Diagram) | รายชื่อ 10 entity พร้อม attribute และ PK · ความสัมพันธ์ 12 เส้น (1:N, M:N แตกเป็น associative entity) พร้อม cardinality และ participation (1..N vs 0..N) · รูป ER Diagram เต็มและแบ่งซูม 4 ส่วน | Lecture 1 หน้า 10, 13 · Silberschatz Ch. 6 · Elmasri Ch. 3 | **ชิ้นที่ 2: ER & Schema** | [`design/er-diagram.drawio.png`](../design/er-diagram.drawio.png) · ภูมิ · แบงค์ · บอส · ภีม |
| **5** | การออกแบบเชิงตรรกะและ Normalization (Logical Design & Normalization) | ขั้นตอนแปลง ER เป็น Relational Schema (ตาราง PK/FK และ Data Dictionary ย่อ) · Functional Dependencies (FDs) ของทุกตาราง · พิสูจน์ 1NF → 2NF → 3NF (รวมการตัดสินใจกรณี `lot.household_id` และ `cooking.household_id` พร้อมเหตุผลถ้าตัดออกหรือ Denormalize) | Lecture 1 หน้า 10 · Silberschatz Ch. 7 · Elmasri Ch. 9 | **ชิ้นที่ 2: ER & Schema** | `design/` (รอบ 4) · ไอน์ · กก |
| **6** | การสร้างฐานข้อมูลและสคริปต์ SQL (Physical Design & SQL Implementation) | ตัวอย่างคำสั่ง DDL (`CREATE TABLE` + constraint สำคัญ เช่น `UNIQUE ... NULLS NOT DISTINCT`, `ON DELETE RESTRICT`, `CHECK`) · โครงสร้างข้อมูลตัวอย่าง `seeds/` · ชุด query สำคัญพร้อมคำอธิบายและผลลัพธ์ (เตือนหมดอายุ · แนะนำเมนู · ธุรกรรมทำอาหาร FEFO · ทิ้งของ · ยกเลิกคืนล็อต · JOIN + GROUP BY สรุปผลและ dashboard) | Lecture 1 หน้า 10–11 · Silberschatz Ch. 6 · Elmasri Part 3 · รูบริกรายงาน DB | **ชิ้นที่ 3: SQL Script** | [`database/README.md`](../database/README.md) (`schema/`, `seeds/`, `queries/`) · ทุกคน (DDL ตารางตัวเอง) + เจตน์ + ทีม SQL กฎ |
| **7** | การเชื่อมเว็บแอปพลิเคชันและผลการทดสอบ (Web App Integration & Testing) | การเชื่อมต่อ Nginx → Flask → PostgreSQL 18 · ภาพหน้าจอจริงทั้งฝั่งบ้าน (หน้า Kiosk 6 หมวด + ตะกร้า · แนะนำเมนู · ทำอาหาร · เตือนหมดอายุ) และฝั่งผู้ดูแลระบบ (ดูทุกบ้าน · ปิด/เปิดบัญชี · dashboard) · ตารางผลการทดสอบกรณีขอบเขตและกรณีผิดกฎ (ของไม่พอ · หมดอายุวันนี้ · ข้ามบ้าน · เครื่องปรุงไม่พอ · ยกเลิกซ้ำพร้อมกัน) | ปรับจากต้นแบบ 311-3303 (ข้อ 6–7) + รูบริกรายงาน DB (Testing & Validation) | เสริมขั้น 3–4 (ADR-008) | `frontend/` · `backend/` · `nginx/` · ทีม frontend + backend + บอส |
| **8** | การตัดสินใจออกแบบ ปัญหาที่พบ และวิธีแก้ไข (Design Decisions, Challenges & Solutions) | ตารางเปรียบเทียบทางเลือกออกแบบสำคัญ (สรุปจาก ADR พร้อมระบุทั้งข้อดีและข้อเสียของทางที่เลือก เช่น แยกบัญชีบ้านเดียว · ยกเลิก = ลบแถว + `DELETE ... RETURNING` · ชุดเริ่มต้นไม่แก้ ER · Docker Compose) · ตาราง **ปัญหาที่เจอจริง–สาเหตุเชิงกลไก–วิธีแก้** (ดึงจาก PR review และ bug จริง ห้ามแต่งขึ้น) | ต้นแบบ 311-3303 (ข้อ 8: กฎหลักฐานจริง + ตารางเทียบทางเลือกที่มีข้อเสียของทางที่เลือก) | **ชิ้นที่ 4: Final Report** | [`docs/DECISIONS.md`](../docs/DECISIONS.md) · ประวัติ PR/Issue · ทุกคน |
| **9** | สรุปผลและแนวทางพัฒนาต่อ (Conclusion & Future Work) | สรุปว่าบรรลุวัตถุประสงค์และเงื่อนไขความถูกต้องของข้อมูลครบหรือไม่ · ข้อจำกัดที่ยังมีอยู่ (เช่น ยังไม่เก็บราคาซื้อ ไม่แยกรายคนในบ้าน) · แนวทางต่อยอด (เช่น สแกนบาร์โค้ด · แจ้งเตือนผ่าน LINE · ปรับ index เมื่อข้อมูลโต) | ต้นแบบ 311-3303 (ข้อ 9) · แนวทางรายงานโครงงานมหาวิทยาลัย | **ชิ้นที่ 4: Final Report** | ทุกคนช่วยกันสรุป |
| **10** | เอกสารอ้างอิง (References) | รายการอ้างอิงทั้งหมดที่ใช้จริง (สไลด์วิชา ตำราฐานข้อมูล เอกสารทางการ PostgreSQL / Flask / Nginx / Docker) | ต้นแบบ 311-3303 (ข้อ 10) | **ชิ้นที่ 4: Final Report** | บอส + ทุกคน |
| **ภาคผนวก** | Appendix A: Data Dictionary ฉบับเต็ม · Appendix B: สคริปต์ SQL ทั้งชุด · Appendix C: บันทึกการแบ่งงานและการมีส่วนร่วมของสมาชิก 7 คน | ตารางชนิดข้อมูลและ constraint ครบทุกคอลัมน์ · ไฟล์ SQL ที่รันซ้ำได้จริง · สรุปงานที่แต่ละคนรับผิดชอบ | แนวทางรายงานโครงงาน DB มหาวิทยาลัย | หลักฐานตรวจย้อนชิ้นที่ 2–3 | เจตน์ + ไอน์ + กก + บอส |

---

## 3. กฎการเขียนรายงานที่ยึดต่อจากต้นแบบ 311-3303

เพื่อให้รายงานมีน้ำหนักทางวิศวกรรมและตอบคำถามอาจารย์ได้ทุกหน้า ทีมยึดกฎ 4 ข้อนี้ตั้งแต่รอบ 2–8:

1. **ทุกตัวเลขและทุกปัญหาต้องมีที่มาจริง** — ตารางผลทดสอบและตารางปัญหาในบทที่ 7–8 ต้องมาจากผลรัน PostgreSQL / `pytest` / PR review ที่เกิดขึ้นจริง ห้ามแต่งตัวเลขหรือแต่งปัญหาขึ้นเอง
2. **ยกเฉพาะโค้ดและ SQL ชิ้นสำคัญในเนื้อหา** — บทที่ 6 ยกเฉพาะ SQL ชิ้นสั้นที่โชว์หลักการ (DDL constraint, FEFO, `DELETE ... RETURNING`, `JOIN + GROUP BY`) ส่วนสคริปต์เต็มชุดไว้ในภาคผนวก B
3. **ตารางเปรียบเทียบทางเลือกต้องบอกข้อเสียของทางที่เลือกด้วย** — ดึงตรงจากหัวข้อ "ผลที่ตามมา (⚠️)" ใน [`docs/DECISIONS.md`](../docs/DECISIONS.md)
4. **เก็บหลักฐานระหว่างทางตั้งแต่รอบ 4–7** — แคปผลรัน DDL/Query, ผลทดสอบ error ของ constraint, และหน้าจอเว็บเก็บไว้ตอนทำเสร็จแต่ละรอบ จะได้ไม่ต้องมาย้อนรันใหม่ทั้งหมดในรอบ 8

---

## 4. แหล่งที่มาที่ใช้กำหนดโครงรายงาน

1. **สไลด์รายวิชา 310-2309 ระบบฐานข้อมูล (Database System):** รศ.ดร. อานนท์ รุ่งสว่าง, *Lecture 1 - Introduction* (รุ่น 2026-2, คณะเทคโนโลยีดิจิทัล สถาบันเทคโนโลยีจิตรลดา) — หน้า 5 (ลำดับหัวข้อ), หน้า 10 (แผน 3 Phase), หน้า 11 (Key Deliverables 4 ชิ้น), หน้า 13 (draw.io), หน้า 28–31 (โครงสร้าง System Overview → Business Rules → Data Integrity & Constraints) · สรุปอ้างอิงอยู่ใน [`docs/COURSE_REQUIREMENTS.md`](../docs/COURSE_REQUIREMENTS.md)
2. **Silberschatz, A., Korth, H. F., & Sudarshan, S. (2020):** *Database System Concepts* (7th ed., McGraw-Hill; companion site: [db-book.com](https://www.db-book.com/)) — Part 2: Chapter 6 (*Database Design Using the E-R Model*: Requirements Analysis → Conceptual Design → Logical Design → Physical Design) และ Chapter 7 (*Relational Database Design*: Functional Dependencies, Lossless-Join Decomposition, 3NF / BCNF)
3. **Elmasri, R., & Navathe, S. B. (2016):** *Fundamentals of Database Systems* (7th ed., Pearson) — Part 2 Chapter 3 (*Data Modeling Using the ER Model*) และ Part 3 Chapter 9 (*Relational Database Design by ER- and EER-to-Relational Mapping*)
4. **ต้นแบบรายงานวิชา 311-3303 Embedded System Design ของทีม:** `Lab_Report_ADC_SAR_Program13-1.pdf` และ `Lab_Report_DoubleDabble_7Seg.pdf` — ใช้เป็นต้นแบบโครง 10 หัวข้อ, มาตรฐานการเขียนตารางปัญหา–สาเหตุเชิงกลไก–วิธีแก้, และตารางเปรียบเทียบทางเลือกที่มีข้อเสียของทางที่เลือก

---

## จะมีอะไรในโฟลเดอร์นี้

```text
report/
├── README.md            โครงรายงานและแหล่งอ้างอิง (ไฟล์นี้)
├── report.docx          รายงานฉบับส่ง (เริ่มร่างรอบ 8)
└── presentation.pptx    สไลด์นำเสนอ (เริ่มร่างรอบ 8)
```

> ⚠️ **git รวมงานในไฟล์ `.docx` กับ `.pptx` ให้ไม่ได้** ถ้า 2 คนแก้ไฟล์เดียวกันคนละ branch แล้ว merge git จะเหลือไว้ฉบับเดียวและแจ้ง conflict งานของอีกคนต้องไปใส่ใหม่เอง
>
> ✅ ประชุมครั้งที่ 1 ตกลงใช้ **Word** ไม่ใช้ Google Docs / Slides · ไฟล์เดียวแก้ทีละคน แบบเดียวกับไฟล์ ER

# design/ — ER Diagram + Relational Schema

👤 ยังไม่ได้ตกลงว่าใครรับ · งานในโฟลเดอร์นี้: ER Diagram · Relational Schema + Normalization — ดู [`../docs/TEAM_AND_WORKFLOW.md`](../docs/TEAM_AND_WORKFLOW.md)

> ⬜ **ขั้น 2 ยังไม่เริ่ม** — เริ่มเมื่ออาจารย์ยืนยันหัวข้อ

## หน้าที่

เก็บงานขั้นที่ 2 ตาม Key Deliverables (Lecture 1 หน้า 11) คือ **ER Diagram & Relational Schema**

## จะมีอะไรในโฟลเดอร์นี้

```text
design/
├── business-rules.md       กฎของระบบ เขียนแบบตัวอย่างร้านเสื้อผ้า (หน้า 28–31)
├── er-diagram.drawio       ไฟล์ draw.io (หน้า 13)
├── er-diagram.png          รูปที่ export จาก draw.io ไว้เปิดดูบน GitHub
└── relational-schema.md    ตาราง คอลัมน์ PK / FK และขั้นตอน Normalization
```

## ต้องครอบอะไรบ้าง

- ข้อมูลหลัก 8 อย่างใน [`../docs/proposal.md`](../docs/proposal.md) ข้อ 6
- กฎใน [`../docs/DECISIONS.md`](../docs/DECISIONS.md): หักตามสูตร (ADR-001) · บันทึกการทิ้ง (ADR-003) · หน่วยมาตรฐานเดียว (ADR-004)
- Data Integrity & Constraints แบบตัวอย่างหน้า 31: PK ทุกตาราง · FK · NOT NULL · UNIQUE

## อ้างอิง

- Lecture 1 หน้า 10 — Phase 1: Conceptual & Logical Design (ER & Relational Models), Database Normalization
- Lecture 1 หน้า 13 — draw.io
- Lecture 1 หน้า 14–32 — ตัวอย่าง DB Requirement 4 ระบบ ([สรุปไว้ที่นี่](../docs/COURSE_REQUIREMENTS.md#3-ตัวอย่าง-db-requirement-ของอาจารย์-lecture-1-หน้า-1432))

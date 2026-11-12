# Roadmap — 4 ขั้นของโครงงาน

อาจารย์กำหนดงานที่ต้องส่ง 4 ชิ้น (**Lecture 1 หน้า 11**) และลำดับเนื้อหา 3 phase (**หน้า 10**)

```text
ขั้น 1          ขั้น 2              ขั้น 3             ขั้น 4
Proposal   →   ER Diagram +   →    SQL           →    Final Report +
               Relational          Implementation     Presentation
               Schema              Script
  🟡              ⬜                  ⬜                  ⬜

               └ Phase 1 ┘         └ Phase 2 ┘        └ Phase 3 ┘

               Web app: Nginx · frontend · backend ────────────────►
                 ⬜
```

| สัญลักษณ์ | ความหมาย |
|---|---|
| ✅ | เสร็จและส่งแล้ว |
| 🟡 | กำลังทำ |
| ⬜ | ยังไม่เริ่ม |

---

## 🟡 ขั้น 1 · Project Proposal (Topic & Idea)

ส่งผ่านแบบฟอร์มของอาจารย์ ช่องที่ต้องกรอกอยู่ใน [`COURSE_REQUIREMENTS.md`](COURSE_REQUIREMENTS.md#24-ขั้นที่-1--proposal)

- [x] เลือกหัวข้ออันดับ 1: Smart Fridge & Recipe Planner
- [x] เลือกหัวข้ออันดับ 2–3: ระบบขายบัตรคอนเสิร์ต · ระบบจัดการหอพัก
- [x] ร่างข้อ 3–6 ของอันดับ 1 → [`proposal.md`](proposal.md)
- [ ] เขียนข้อ 4–6 ของอันดับ 2 และ 3
- [ ] ตรวจชื่อทีมกับรายชื่อสมาชิกให้ตรงรูปแบบในแบบฟอร์ม
- [ ] ส่งแบบฟอร์ม — กำหนดส่งยังไม่ชัด ดู [`COURSE_REQUIREMENTS.md`](COURSE_REQUIREMENTS.md#5-ยังไม่รู้--ต้องถามอาจารย์)

## ⬜ ขั้น 2 · ER Diagram & Relational Schema

เริ่มเมื่ออาจารย์ยืนยันหัวข้อ · วาดด้วย draw.io (หน้า 13) · งานอยู่ใน [`../design/`](../design/)

- [ ] เขียนกฎของระบบ (business rules) แบบตัวอย่างร้านเสื้อผ้า หน้า 28–31
- [ ] ER Diagram ที่ครอบข้อมูลหลักครบ 8 อย่าง
- [ ] แปลง ER เป็น relational schema พร้อม PK / FK
- [ ] Normalization

## ⬜ ขั้น 3 · SQL Implementation Script

ต้องเลือก DBMS ก่อน ([ADR-005](DECISIONS.md#adr-005--เลือก-dbms)) · งานอยู่ใน [`../database/`](../database/)

- [ ] DDL สร้างตารางพร้อม constraint
- [ ] ข้อมูลตัวอย่าง
- [ ] query ที่ระบบต้องทำ: เตือนของใกล้หมดอายุ · แนะนำเมนู · หักของตอนทำอาหาร · บันทึกการทิ้ง

## ⬜ ขั้น 4 · Final Report & Presentation

Phase 3 มี Consultation กับ Final Presentation (หน้า 10) · งานอยู่ใน [`../report/`](../report/)

- [ ] ถามอาจารย์เรื่องรูปแบบรายงานและเวลานำเสนอ
- [ ] รายงาน
- [ ] สไลด์นำเสนอ

## ⬜ เว็บแอป · Nginx · frontend · backend

เริ่มพร้อมขั้น 2 แล้วทำคู่กันไป ([ADR-008](DECISIONS.md#adr-008--ทำเป็นเว็บแอปที่ใช้งานได้จริง)) · งานอยู่ใน [`../nginx/`](../nginx/) · [`../frontend/`](../frontend/) · [`../backend/`](../backend/)

- [ ] ตกลงคำขอ `/api/` ระหว่าง frontend กับ backend ([จุดที่ต้องคุยกันก่อนลงมือ](TEAM_AND_WORKFLOW.md#จุดที่ต้องคุยกันก่อนลงมือ))
- [ ] Nginx · frontend · backend ตาม[ตารางใน README](../README.md#แต่ละส่วนต้องมีอะไร)
- [ ] backend ต่อ database (ต้องเลือก DBMS ก่อน · [ADR-005](DECISIONS.md#adr-005--เลือก-dbms))

# design/ — ER Diagram + Relational Schema

👤 ER Diagram: ภูมิ · แบงค์ · บอส · ภีม · Relational Schema + Normalization: ไอน์ · กก — ดู [`../docs/TEAM_AND_WORKFLOW.md`](../docs/TEAM_AND_WORKFLOW.md)

> 🟡 **ขั้น 2 เริ่มแล้ว** — [กฎของระบบ](business-rules.md) เสร็จแล้ว · ER เริ่มรอบที่ 1 (18 พ.ย.)

## หน้าที่

เก็บงานขั้นที่ 2 ตาม Key Deliverables (Lecture 1 หน้า 11) คือ **ER Diagram & Relational Schema**

## จะมีอะไรในโฟลเดอร์นี้

```text
design/
├── business-rules.md       ✅ กฎของระบบ เขียนแบบตัวอย่างร้านเสื้อผ้า (หน้า 28–31)
├── er-diagram.drawio       ไฟล์ต้นฉบับ draw.io (หน้า 13)
├── er-diagram.drawio.png   รูปของไฟล์ข้างบน เปิดดูบน GitHub ได้
└── relational-schema.md    ตาราง คอลัมน์ PK / FK และขั้นตอน Normalization
```

เก็บไฟล์ ER ทั้ง 2 แบบตาม [ADR-013](../docs/DECISIONS.md#adr-013--ไฟล์-er-เก็บทั้ง-drawio-และ-drawiopng)

## วาด ER แบบไหน

แบบเดียวกับตัวอย่างของวิชาสัปดาห์ที่ 1

- entity เป็นตาราง แถวบนสุดคือชื่อ entity แต่ละแถวข้างล่างคือ attribute มีช่อง PK / FK อยู่หน้าชื่อ
- ชื่อ entity และ attribute เป็นภาษาอังกฤษ ตัวเล็ก คั่นด้วย `_` เช่น `household_id`
- เส้นความสัมพันธ์แบบ crow's foot เช่น หนึ่งบ้านมีล็อตได้ศูนย์ถึงหลายล็อต

## ต้องครอบอะไรบ้าง

- ข้อมูลหลัก 8 อย่างใน [README](../README.md#ข้อมูลหลัก-8-อย่าง) (ต่างจาก proposal ข้อ 6: ตัดข้อมูลสมาชิก ADR-010 · เพิ่มบัญชีผู้ดูแลระบบ ADR-015)
- [กฎของระบบ](business-rules.md) ทุกข้อ
- กฎใน [`../docs/DECISIONS.md`](../docs/DECISIONS.md): หักตามสูตร (ADR-001) · บันทึกการทิ้ง (ADR-003) · หน่วยมาตรฐานเดียว (ADR-004) · บัญชีบ้าน (ADR-010) · บันทึกหักล็อต (ADR-012) · เครื่องปรุงลงตู้ (ADR-014) · ผู้ดูแลระบบปิดบัญชีบ้าน (ADR-015) · วัตถุดิบและสูตรของแต่ละบ้าน (ADR-016) · จำนวนเท่าของการทำอาหาร (ADR-017)
- Data Integrity & Constraints แบบตัวอย่างหน้า 31: PK ทุกตาราง · FK · NOT NULL · UNIQUE

## บันทึกและแก้ไฟล์ ER

- เปิดแก้: เปิด `er-diagram.drawio` ใน draw.io
- บันทึก: File → Save เป็น `er-diagram.drawio` แล้ว File → Export as → PNG… ติ๊ก **Include a copy of my diagram** ตั้งชื่อ `er-diagram.drawio.png` ทับไฟล์เดิม
- commit ทั้ง 2 ไฟล์ใน PR เดียวกันเสมอ รูปบน GitHub จะได้ตรงกับไฟล์ต้นฉบับ

> ⚠️ **git รวมงานในไฟล์ ER ให้ไม่ได้** `.drawio.png` เป็นรูป git รวมไม่ได้เลย ส่วน `.drawio` รวมได้แค่บางกรณี ถ้า 2 คนแก้คนละ branch แล้ว merge อาจเหลือไว้ฉบับเดียว งานของอีกคนต้องไปวาดใหม่เอง
>
> **กฎ: แก้ทีละคน** — ก่อนแก้ให้ pull develop ล่าสุดและบอกในกลุ่มว่ากำลังแก้ คนถัดไปเริ่มแก้ได้เมื่อ PR ของคนก่อน merge เข้า develop แล้ว

## อ้างอิง

- Lecture 1 หน้า 10 — Phase 1: Conceptual & Logical Design (ER & Relational Models), Database Normalization
- Lecture 1 หน้า 13 — draw.io
- Lecture 1 หน้า 14–32 — ตัวอย่าง DB Requirement 4 ระบบ ([สรุปไว้ที่นี่](../docs/COURSE_REQUIREMENTS.md#3-ตัวอย่าง-db-requirement-ของอาจารย์-lecture-1-หน้า-1432))

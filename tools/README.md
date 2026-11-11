# tools/ — สคริปต์ช่วยงาน

สคริปต์ที่ใช้ตรวจงาน **ไม่ใช่ส่วนของระบบฐานข้อมูล**
รันจาก root ของ repo · ใช้ Python stdlib ล้วน ไม่ต้องลง package เพิ่ม

| สคริปต์ | ทำอะไร |
|---|---|
| [`check_doc_links.py`](check_doc_links.py) | ลิงก์ในไฟล์ `.md` ต้องชี้ไปไฟล์และหัวข้อที่มีอยู่จริง |

## `check_doc_links.py` — ลิงก์ในเอกสารต้องชี้ถูก

```bash
python tools/check_doc_links.py
python tools/check_doc_links.py --external    # เช็คลิงก์ http ด้วย (ช้า ต้องต่อเน็ต)
python tools/check_doc_links.py --self-test   # ทดสอบการคำนวณ anchor
```

เอกสารในโปรเจกต์นี้ลิงก์หากันเยอะ ทั้ง README → docs → โฟลเดอร์งาน พอย้ายหรือเปลี่ยนชื่อไฟล์ ลิงก์ก็ตายเงียบๆ GitHub ไม่เตือน คนอ่านเจอ 404 เอาเอง

สคริปต์ตรวจทั้งลิงก์ไปไฟล์ **และหัวข้อ** (`ไฟล์.md#หัวข้อ`) โดยคำนวณ anchor แบบเดียวกับ GitHub

> จุดที่พลาดกันบ่อย: GitHub **ไม่ยุบ** ช่องว่างซ้ำให้เหลือขีดเดียว
> หัวข้อ `## ADR-005 — เลือก DBMS` ตัด `—` ออกแล้วเหลือช่องว่างติดกันสองตัว
> anchor จริงจึงมี **ขีดคู่** → `#adr-005--เลือก-dbms`

ยกมาจาก `tools/check_doc_links.py` ของ [luma-webapp-g04](https://github.com/boss2912/luma-webapp-g04) แก้ 3 จุด คือคำอธิบาย ชื่อ User-Agent และหมายเหตุที่มาของชุดทดสอบ

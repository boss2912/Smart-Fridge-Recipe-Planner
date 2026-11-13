# กติกาการทำงานร่วมกัน — Smart Fridge & Recipe Planner

> ✅ **แจ้งทีมในประชุมครั้งที่ 1 (13 พ.ย. 2026)** · ตั้งป้องกัน main กับ develop บน GitHub แล้ว

---

## Branch

```text
main ──────────────────────────────●  ฉบับส่งอาจารย์เท่านั้น
                                   ↑ PR
develop ───●───●───●───●───●───●───●  รวมงานทุกคน ตรวจก่อนเข้า main
           ↑       ↑       ↑
      branch งาน ตั้งชื่อ <เลข issue>-<เรื่อง>
```

| Branch | ใช้ทำอะไร |
|---|---|
| `main` | ฉบับที่ส่งอาจารย์ · 🔒 ตั้งป้องกันแล้ว |
| `develop` | รวมงานทุกคน ตรวจก่อนขึ้น `main` · 🔒 ตั้งป้องกันแล้ว |
| `<เลข issue>-<เรื่อง>` | งานแต่ละชิ้น เช่น `12-er-diagram`, `20-ddl-lot-table` |

"ป้องกันไว้" หมายถึงตั้ง ruleset บน GitHub เปิดกฎ *"Require a pull request before merging"* (Required approvals = 1 · *"Dismiss stale pull request approvals when new commits are pushed"* · *"Require approval of the most recent reviewable push"*) กับ *"Block force pushes"* ส่วน `develop` เปิด *"Restrict deletions"* เพิ่ม

- push ตรงเข้า branch นั้นไม่ได้ ต้องเปิด PR และมีคนอื่น approve 1 คนก่อน merge
- push แก้เพิ่มหลังได้ approve แล้ว approve เดิมหายไป ต้องให้คนอื่นที่ไม่ใช่คน push approve ใหม่
- ลบ `develop` ไม่ได้ แม้จะมีปุ่ม Delete branch ขึ้นหลัง merge PR develop→main
- ทุกคนต้องรอ approve · เจ้าของ repo (บอส) ปิดกฎชั่วคราวได้เฉพาะตอนจำเป็น แล้วเปิดคืนทันที

---

## Workflow ประจำวัน

```bash
# 1. ดึงงานคนอื่นมาก่อน
git checkout develop
git pull origin develop

# 2. แตก branch งานจาก develop
git checkout -b 12-er-diagram

# 3. ทำงาน แล้ว commit
git add design/
git commit -m "docs(design): ER diagram ฉบับแรก"

# 4. push แล้วเปิด PR เข้า develop บน GitHub
git push -u origin 12-er-diagram
```

ตอนเปิด PR ช่อง base ต้องเป็น `develop` GitHub จะตั้งเป็น `main` ให้เอง ต้องเปลี่ยนก่อนกดสร้าง

ถ้า `develop` บน GitHub ขยับไประหว่างทำ ให้ดึงของใหม่มาก่อนแล้ว merge เข้า branch ตัวเอง แก้ conflict ที่นั่น ไม่ใช่แก้ใน PR

```bash
git fetch origin
git merge origin/develop
```

---

## Commit message

```text
<type>(<scope>): <สรุปสั้นๆ>
```

**type**: `feat` · `fix` · `docs` · `chore`
**scope** (ใส่หรือไม่ใส่ก็ได้): `proposal` · `design` · `db` · `report` · `nginx` · `frontend` · `backend`

ตัวอย่างที่ดี:

```text
docs(design): ER diagram ฉบับแรก ครบข้อมูลหลัก 8 อย่าง
feat(db): DDL ตาราง lot พร้อม CHECK จำนวนห้ามติดลบ
fix(db): query แนะนำเมนูไม่นับล็อตที่หมดอายุ
```

ตัวอย่างที่ไม่ดี: `update` · `แก้งาน` · `fix bug`

---

## Pull Request

### ก่อนเปิด PR — ตรวจ 4 ข้อนี้

- [ ] ไม่มีอีเมลของสมาชิกใน diff ([ADR-007](docs/DECISIONS.md#adr-007--รายชื่อสมาชิกและรหัสนักศึกษาขึ้น-readme))
- [ ] ไม่มีไฟล์ฐานข้อมูล (`.db`, `.sqlite`) ใน diff
- [ ] อัปเดต `README.md` ของโฟลเดอร์ที่แก้
- [ ] ถ้าตัดสินใจเรื่องที่คนอื่นอาจแก้กลับ → เพิ่ม ADR ใน [`docs/DECISIONS.md`](docs/DECISIONS.md)

### กติกา review

- ต้องมีคนอื่น approve อย่างน้อย 1 คนก่อน merge
- คนเปิด PR ไม่ approve PR ตัวเอง
- push แก้หลังได้ approve → ต้องขอ approve ใหม่
- เจอปัญหา → บอกให้ชัดว่าปัญหาคืออะไร ไม่ใช่แค่ "แก้หน่อย"

### วิธี merge

ใช้ **Merge commit** ไม่ใช่ squash จะได้เห็นว่าใครทำอะไรเมื่อไหร่ งานกลุ่มที่ต้องแสดงการมีส่วนร่วมต้องเห็นตรงนี้

---

## สิ่งที่ห้ามทำ

| ห้าม | เพราะ |
|---|---|
| ใส่อีเมลของสมาชิกลง repo | repo เป็นสาธารณะ ([ADR-007](docs/DECISIONS.md#adr-007--รายชื่อสมาชิกและรหัสนักศึกษาขึ้น-readme)) |
| commit ไฟล์ `.db` / `.sqlite` | ฐานข้อมูลต้องสร้างใหม่ได้จากสคริปต์ SQL เสมอ |
| `git push --force` ไปที่ `main` / `develop` | ทับงานคนอื่น |
| แก้โฟลเดอร์ที่คนอื่นดูแลโดยไม่บอก | งานทับกันและ conflict |
| ทิ้ง PR ค้างเป็นสัปดาห์ | คนอื่นทำงานต่อบนของเก่า พอ merge ทีหลังก็ conflict |

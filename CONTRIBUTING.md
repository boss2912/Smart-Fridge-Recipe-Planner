# กติกาการทำงานร่วมกัน — Smart Fridge & Recipe Planner

> ⬜ **ร่าง — กลุ่มยังไม่ได้ตกลง** และยังไม่ได้ตั้งค่าป้องกัน branch บน GitHub

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
| `main` | ฉบับที่ส่งอาจารย์ · 🔒 ควรตั้งป้องกันไว้ |
| `develop` | รวมงานทุกคน ตรวจก่อนขึ้น `main` · 🔒 ควรตั้งป้องกันไว้ |
| `<เลข issue>-<เรื่อง>` | งานแต่ละชิ้น เช่น `12-er-diagram`, `20-ddl-lot-table` |

"ป้องกันไว้" หมายถึงตั้ง ruleset บน GitHub ว่า *"Changes must be made through a pull request"* ใครก็ push ตรงเข้า branch นั้นไม่ได้ ต้องเปิด PR เท่านั้น เจ้าของ repo ต้องตั้งเองในหน้า Settings

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

ถ้า `develop` ขยับไประหว่างทำ ให้ `git merge develop` เข้า branch ตัวเอง แล้วแก้ conflict ที่นั่น ไม่ใช่แก้ใน PR

---

## Commit message

```text
<type>(<scope>): <สรุปสั้นๆ>
```

**type**: `feat` · `fix` · `docs` · `chore`
**scope**: `proposal` · `design` · `db` · `report` · `nginx` · `frontend` · `backend`

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

import sys
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path

import pytest
from packaging.requirements import Requirement

REQUIREMENTS = Path(__file__).resolve().parent / "requirements.txt"


def locked_packages():
    """อ่าน requirements.txt คืน (ชื่อ, เวอร์ชันที่ล็อก) เฉพาะตัวที่ต้องลงในเครื่องนี้"""
    packages = []
    for line in REQUIREMENTS.read_text(encoding="ascii").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        req = Requirement(line)
        if req.marker is None or req.marker.evaluate():
            packages.append((req.name, str(req.specifier).removeprefix("==")))
    return packages


# จุดที่ 1: ตรวจเวอร์ชัน Python
def test_python_version():
    found = f"{sys.version_info.major}.{sys.version_info.minor}"
    assert found == "3.14", f"ต้องใช้ Python 3.14 (ค่าที่ได้: {found})"


# จุดที่ 2: ตรวจว่า library ทุกตัวตรงกับที่ล็อกไว้ใน requirements.txt
@pytest.mark.parametrize("name, locked", locked_packages())
def test_package_version(name, locked):
    try:
        found = version(name)
    except PackageNotFoundError:
        pytest.fail(f"ยังไม่ได้ลง {name} → pip install -r backend/requirements.txt")
    assert found == locked, f"{name} ต้องเป็น {locked} (ค่าที่ได้: {found})"

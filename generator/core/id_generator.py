from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
COUNTER_FILE = BASE_DIR / "generator" / ".counter"


def _read_counter():
    if COUNTER_FILE.exists():
        text = COUNTER_FILE.read_text(encoding="utf-8").strip()
        if text.isdigit():
            return int(text)
    return 0


def _write_counter(value):
    COUNTER_FILE.parent.mkdir(parents=True, exist_ok=True)
    COUNTER_FILE.write_text(str(value), encoding="utf-8")


def generate_id(prefix="KH", version="V1"):
    """Generate a stable, incrementing sample ID like KH-V1-000042."""
    count = _read_counter() + 1
    _write_counter(count)
    return f"{prefix}-{version}-{count:06d}"

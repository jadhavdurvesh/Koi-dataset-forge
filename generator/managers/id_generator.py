from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
COUNTER_FILE = BASE_DIR / "datasets" / ".counter"


def generate_id():
    if not COUNTER_FILE.exists():
        COUNTER_FILE.write_text("1")

    current = int(COUNTER_FILE.read_text().strip())

    sample_id = f"KH-V1-{current:06d}"

    COUNTER_FILE.write_text(str(current + 1))

    return sample_id
from collections import Counter

_emotion_counts = Counter()
_total = 0


def record(sample):
    """Track a saved sample for the end-of-run summary."""
    global _total
    _total += 1
    _emotion_counts[sample.get("emotion", "unknown")] += 1


def show():
    """Print a short summary of what this run generated."""
    if _total == 0:
        print("\nNo samples generated this run.")
        return

    print(f"\n📊 Session summary — {_total} sample(s) generated")
    for emotion, count in _emotion_counts.most_common():
        print(f"   {emotion:<12} {count}")

from collections import Counter

stats = Counter()


def record(sample):
    stats[sample["emotion"]] += 1


def show():
    print("\n📊 KOI Hearts Statistics")
    print("-------------------------")

    for emotion, count in stats.items():
        print(f"{emotion:<15} {count}")
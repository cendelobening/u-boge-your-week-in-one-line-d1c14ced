import os

# Final: "Monday's" pins a concrete weekday; 99 chars, every word earns its place.
LINE = "Twelve gas pleas, three entries shipped, two finals lost — Monday's bounty queued before breakfast."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

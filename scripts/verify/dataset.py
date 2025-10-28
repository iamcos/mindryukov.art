import csv
import os
from datetime import datetime

from scripts.downloader.config import POSTS_JSON
from scripts.downloader.utils import load_json


def main() -> None:
    posts = load_json(POSTS_JSON) or []

    missing = []
    for p in posts:
        issues = []
        if p.get("media") and not p.get("media_path"):
            issues.append("missing_media")
        if p.get("message") in (None, ""):
            issues.append("missing_text")
        if issues:
            missing.append({"id": p.get("id"), "issues": ";".join(issues)})

    out_dir = os.path.dirname(__file__)
    ts = datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    csv_path = os.path.join(out_dir, f"missing-{ts}.csv")

    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "issues"])
        writer.writeheader()
        for row in missing:
            writer.writerow(row)

    html_path = os.path.join(out_dir, f"report-{ts}.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write("<html><body>")
        f.write(f"<h1>Dataset Report {ts}</h1>")
        f.write(f"<p>Total posts: {len(posts)}</p>")
        f.write(f"<p>Items with issues: {len(missing)}</p>")
        f.write("</body></html>")

    print(f"Wrote {csv_path}\nWrote {html_path}")


if __name__ == "__main__":
    main()

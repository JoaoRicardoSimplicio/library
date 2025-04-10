from datetime import datetime


def parse_date(date_str: str) -> datetime:
    formats = [
        "%Y-%m-%d",
        "%Y-%m",
        "%Y",
    ]

    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt).date().isoformat()
        except ValueError:
            continue

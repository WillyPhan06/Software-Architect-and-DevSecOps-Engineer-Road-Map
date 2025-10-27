def parse_page_input(page_input: str, exclude_input: str = "") -> list[int]:
    """Parse user input like '1-5,8,10' and apply exclusions like '3,6'."""
    pages = set()
    for part in page_input.split(","):
        part = part.strip()
        if "-" in part:
            start, end = map(int, part.split("-"))
            pages.update(range(start, end + 1))
        elif part.isdigit():
            pages.add(int(part))

    exclude_pages = {int(x) for x in exclude_input.split(",") if x.strip().isdigit()}
    pages -= exclude_pages

    return sorted(pages)

def read_lines(fname: str) -> list[str]:
    with open(fname) as f:
        return f.read().strip().splitlines()
from test_fixtures import countries


def find_match_loop_no_key(iterable, value=None, default=None):
    for val in iterable:
        if (value is None and val) or (value is not None and val == value):
            return val
    return default


def find_match_loop(iterable, value=None, key=None, default=None):
    for val in iterable:
        _val = key(val) if callable(key) else val

        if (value is None and _val) or (value is not None and _val == value):
            return val
    return default


if __name__ == "__main__":
    target_match = {"country": "Puerto Rico", "population": 3195153}
    print(find_match_loop(countries, target_match))

    def match_scotland(data):
        return data["country"] == "Scotland"

    print(find_match_loop(countries, key=match_scotland))

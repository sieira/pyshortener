class Url:
    def __init__(self, long_url: str, short_url: str, click_count: int):
        self.short_url = short_url
        self.long_url = long_url
        self.click_count = click_count
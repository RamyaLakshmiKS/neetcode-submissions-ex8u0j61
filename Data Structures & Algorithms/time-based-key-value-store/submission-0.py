class TimeMap:
    def __init__(self):
        self.kv_dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.kv_dict:
            self.kv_dict[key] = {}
        if timestamp not in self.kv_dict[key]:
            self.kv_dict[key][timestamp] = []
        self.kv_dict[key][timestamp].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kv_dict:
            return ""
        seen = 0

        for time in self.kv_dict[key]:
            if time <= timestamp:
                seen = max(seen, time)
        if seen == 0:
            return ""
        else:
            return self.kv_dict[key][seen][-1]


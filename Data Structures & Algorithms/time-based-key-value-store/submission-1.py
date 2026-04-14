class TimeMap:
    def __init__(self):
        self.kv_dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.kv_dict:
            self.kv_dict[key] = []
        self.kv_dict[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        values = self.kv_dict.get(key, [])
        l = 0
        r = len(values) - 1
        while l <= r:
            m = (l+r) // 2
            if values[m][1] <= timestamp:
                result = values[m][0]
                l = m+1
            else:
                r = m-1
        return result
            


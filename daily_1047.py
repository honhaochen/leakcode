from bisect import bisect_left, insort_right


class MySet:

    def __init__(self):
        self.keys_to_time = {}
        self.keys_time_to_value = {}

    def set(self, key, value, time):
        if key not in self.keys_to_time:
            self.keys_to_time[key] = []

        insort_right(self.keys_to_time[key], time)
        self.keys_time_to_value[(key, time)] = value

    def get(self, key, time):
        if key not in self.keys_to_time:
            return None

        times = self.keys_to_time[key]
        idx = bisect_left(times, time) - 1

        if idx == -1:
            if len(times) == 0 or times[0] > time:
                return None

        closest_time = times[idx]
        return self.keys_time_to_value[(key, closest_time)]


# Example usage
d = MySet()
d.set(1, 1, 0)
d.set(1, 2, 2)
print(d.get(1, 1))  # Output: 1
print(d.get(1, 3))  # Output: 2
d = MySet()
d.set(1, 1, 5)
print(d.get(1, 0))  # Output: None
print(d.get(1, 10))  # Output: 1
d = MySet()
d.set(1, 1, 0)
d.set(1, 2, 0)
print(d.get(1, 0))  # Output: 2

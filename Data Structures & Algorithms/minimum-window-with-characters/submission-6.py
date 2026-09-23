class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""

        map_t = {}

        for ch in t:
            map_t[ch] = map_t.get(ch, 0) + 1

        window_map = {}

        required = len(map_t)
        formed = 0

        left = 0
        min_len = float("inf")
        min_start = 0

        for right in range(len(s)):

            ch = s[right]

            if ch in map_t:
                window_map[ch] = window_map.get(ch, 0) + 1

                if window_map[ch] == map_t[ch]:
                    formed += 1

            while formed == required:

                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left

                left_ch = s[left]

                if left_ch in map_t:

                    window_map[left_ch] -= 1

                    if window_map[left_ch] < map_t[left_ch]:
                        formed -= 1

                left += 1

        if min_len == float("inf"):
            return ""

        return s[min_start:min_start + min_len]
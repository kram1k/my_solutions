from typing import List

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks = sorted(tasks)
        workers = sorted(workers)
        print(tasks, workers)
        counter = 0

        for task in tasks:
            left, right = 0, len(workers) - 1
            while left <= right:
                mid = (left + right) // 2
                if workers[mid] < task:
                    left = mid + 1
                else:
                    right = mid - 1

            candidates = []
            if left < len(workers):
                candidates.append(workers[left])
            if left > 0:
                candidates.append(workers[left - 1])

            closest = min(candidates, key=lambda y: (y + strength, y))
            print(closest)
            if closest >= task:
                workers.remove(closest)
                counter += 1
            elif closest + strength >= task and pills != 0:
                workers.remove(closest)
                counter += 1
                pills -= 1

        return counter


s = Solution()
print(s.maxTaskAssign([5,9,8,5,9], [1,6,4,2,6], 1, 5))
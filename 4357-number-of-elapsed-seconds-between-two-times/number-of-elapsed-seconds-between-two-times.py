class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        s = int(startTime[:2]) * 3600 + int(startTime[3:5]) * 60 + int(startTime[6:])
        e = int(endTime[:2]) * 3600 + int(endTime[3:5]) * 60 + int(endTime[6:])
        return e - s
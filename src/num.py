from typing import List


class Num:
    def __init__(self, n=0, s="", t=None) -> None:
        """

        Args:
            n:
            s:
        """
        self.at = n
        self.txt = s
        self.n = 0
        self.ok = True
        self.has: List = []
        self.lo = float("inf")
        self.hi = float("-inf")
        self.w = -1 if s.endswith("-") else 1
        self.isSym = False

        self.mu = 0
        self.m2 = 0
        self.sd = 0
        for x in t or []:
            self.add(x)

    def add(self, x):
        self.n += 1
        d = x - self.mu
        self.mu = self.mu + d / self.n
        self.m2 = self.m2 + d * (x - self.mu)
        self.sd = 0 if self.n < 2 else (self.m2 / (self.n - 1)) ** 0.5

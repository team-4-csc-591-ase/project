class Sym:
    def __init__(self, n=0, s="") -> None:
        """

        Args:
            n:
            s:
        """
        self.n = 0
        self.has: dict = {}
        self.most = 0
        self.mode = None
        self.at = n
        self.txt = s
        self.isSym = True
        self.isKlass = False
        self.isIgnored = False
        self.isGoal = False
        self.ok = False

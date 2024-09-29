from jump import Jump

class Cell:
    jump: Jump = None

    def addJump(self, start, end):
        self.jump = Jump(start=start, end=end)

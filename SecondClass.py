class Degree:
    """Meant to hold student name, CWA and degree bagged"""
    def __init__(self, name, CWA, degree):
        self.name = name
        self.CWA = CWA
        self.degree = degree

    def rename(self, newname):
        self.name = newname



class Door:

    _present = None
    _locked = None
    _description = None

    def __init__(self):
        self._description = None
        self._present = False
        self._locked = False

    # Getters
    def present(self):
        return self._present
    def locked(self):
        return self._locked
    def description(self):
        return self._description
    
    # Setters
    def setLocked(self,l):
        self._locked = l
    def set_description(self,d):
        self._description = d
    def setPresent(self,p):
        self._present = p
class SDES:
    def __init__(self, _key):
        #self.master_key = [False] * 10
        self.master_key = [char == '1' for char in _key]

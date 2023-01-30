class A:
    id = 89
    name = "no name"
    __password = None
    def __init__(self,new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name
    def __repr__(self):
        return "45"
if __name__ == "__main__":
    import datetime
    a = A("john")
    print(a.is_new)
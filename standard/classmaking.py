# Class Variables

class TestParent:
    ID = 0
    def __init__(self):
        self.id = self.increaseid()
        print('Parent', self.id, self.ID)

    def increaseid(self,  value=1):
        self.ID += value
        return self.ID

    def __enter__(self):
        self.increaseid()


class TestThis(TestParent):
    def __init__(self, title='Class Placeholder Title'):
        TestParent.__init__(self)
        #super()
        self.title = title
        print('Child', self.ID,self.title)


print(TestThis())
print(TestThis())
print(TestThis())


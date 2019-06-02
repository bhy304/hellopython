class Test:
    def test(self):
        print("Puppy's test")
        self.__q()

    def __q(self):
        print("qqqqqqqqqqqqq")

test = Test()
#test.__q()
test.test()
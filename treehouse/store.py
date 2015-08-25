class Store():
    open = 9
    close = 5
  
    def hours(self):
        return "we're open from {} to {}".format(self.open, self.close)

mystore = Store()
print(mystore.hours())
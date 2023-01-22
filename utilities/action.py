import selenium

class action():

    def setText(self,element,input):
        element.send_keys(input)

    def click(self,element):
        element.click()
        

class Button():
    def __init__(self,font,colorL,colorD,width,height,text):
        self.font = font
        self.colorL = colorL
        self.colorD = colorD
        self.width = width
        self.height = height
        self.text = text
        
class chipButton():
    def __init__(self,value,width,height,image, xpos, ypos):
        self.value = value
        self.image = image
        self.width = width
        self.height = height
        self.xpos = xpos
        self.ypos = ypos
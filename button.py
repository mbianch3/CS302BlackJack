class Button():
    def __init__(self,width,height, image, imageL):
        self.width = width
        self.height = height
        self.image = image
        self.imageL = imageL
        
class chipButton():
    def __init__(self, image, imageL, width,height, xpos, ypos):
        self.image = image
        self.imageL = imageL
        self.width = width
        self.height = height
        self.xpos = xpos
        self.ypos = ypos
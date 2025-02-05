import cv2

class Encoder:
    
    def __init__(self, target_size):
        
        self.target_size = target_size
    #
    
    def process(self, image_path):
        
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (self.target_size[1], self.target_size[0]))
        image = image/255
        
        return image
    #
#
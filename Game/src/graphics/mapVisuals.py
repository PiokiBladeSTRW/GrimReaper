class Map:
    cords = {        
        "0": (260, 175),
        "1": (260, 130),
        "2": (260, 75),
        "3": (260, 45),
        "4": (280, 45),
        "5": (300, 45),
        "6": (155, 130),
        "7": (150, 90),
        "8": (90, 105),
        "9": (90, 205),
        "10": (67,205),
        "11": (45, 205),
        "12": (45, 115),
        "13": (90, 290),
        "14": (260, 290),
        "15": (260, 255),
        "16": (155, 255),
        "17": (305, 237),        
        "18": (325, 220),
        "19": (345, 75),
        "Atop": (150, 75),
        "Abottom": (150, 105),
        "Bbottom": (305, 255),
        "Btop": (305, 220),
        "Cright": (345, 220)
    }

    def __init__(self, canvas, x1, y1, x2, y2, lineColor ='white', iconColor='green'):
        self.canvas = canvas
        self.x1 = x1
        self.y1 = y1

        self.lineColor = lineColor
        self.iconColor = iconColor
        
        self.MarkerIDs = []

        self.x_scale = ((x2 - x1) - 90) / 340  # Subtracting 90 to account for 45 padding on both sides
        self.y_scale = ((y2 - y1) - 90) / 290  # Subtracting 90 to account for 45 padding on both sides


    def scalePoints(self, x,y):
        # Subtract the original padding (45) before scaling, then add 45 padding in the new rectangle
        new_x = self.x1 + 45 + (x - 45) * self.x_scale
        new_y = self.y1 + 45 + (y - 45) * self.y_scale
        return new_x, new_y
    
    def ovalPoints(self, x, y):      
        return x-5, y-5, x+5, y+5
    

    #Mark Player Position
    def playerMarker(self, currentLocation, usrcolor):
        if(len(self.MarkerIDs)>0):
            self.canvas.delete(self.MarkerIDs[0])
            self.MarkerIDs.pop()

        def marker_points(x,y):
            return x+6, y-9, x+12, y-3
        
        self.MarkerIDs.append(self.canvas.create_oval(*marker_points(*self.scalePoints(*self.cords[currentLocation])), fill=usrcolor))

    
    def drawMap(self):
        #Best Not to Mess with this
        self.canvas.create_line(*self.scalePoints(*self.cords["0"]), *self.scalePoints(*self.cords["1"]), fill = self.lineColor)
        
        self.canvas.create_line(*self.scalePoints(*self.cords["1"]), *self.scalePoints(*self.cords["2"]), fill = self.lineColor)
        self.canvas.create_line(*self.scalePoints(*self.cords["1"]), *self.scalePoints(*self.cords["6"]), fill = self.lineColor)
        
        self.canvas.create_line(*self.scalePoints(*self.cords["Atop"]), *self.scalePoints(*self.cords["19"]), fill = self.lineColor)
        self.canvas.create_line(*self.scalePoints(*self.cords["1"]), *self.scalePoints(*self.cords["3"]), fill = self.lineColor)
        
        self.canvas.create_line(*self.scalePoints(*self.cords["3"]), *self.scalePoints(*self.cords["5"]), fill = self.lineColor)
        
        self.canvas.create_line(*self.scalePoints(*self.cords["Atop"]), *self.scalePoints(*self.cords["Abottom"]), fill = self.lineColor)
        self.canvas.create_line(*self.scalePoints(*self.cords["Abottom"]), *self.scalePoints(*self.cords["8"]), fill = self.lineColor)
        
        self.canvas.create_line(*self.scalePoints(*self.cords["8"]), *self.scalePoints(*self.cords["9"]), fill = self.lineColor)
        
        self.canvas.create_line(*self.scalePoints(*self.cords["9"]), *self.scalePoints(*self.cords["11"]), fill = self.lineColor)
        self.canvas.create_line(*self.scalePoints(*self.cords["9"]), *self.scalePoints(*self.cords["13"]), fill = self.lineColor)
        
        self.canvas.create_line(*self.scalePoints(*self.cords["11"]), *self.scalePoints(*self.cords["12"]), fill = self.lineColor)
        
        self.canvas.create_line(*self.scalePoints(*self.cords["13"]), *self.scalePoints(*self.cords["14"]), fill = self.lineColor)
        self.canvas.create_line(*self.scalePoints(*self.cords["14"]), *self.scalePoints(*self.cords["15"]), fill = self.lineColor)
        self.canvas.create_line(*self.scalePoints(*self.cords["15"]), *self.scalePoints(*self.cords["16"]), fill = self.lineColor)
        self.canvas.create_line(*self.scalePoints(*self.cords["15"]), *self.scalePoints(*self.cords["Bbottom"]), fill = self.lineColor)
        self.canvas.create_line(*self.scalePoints(*self.cords["Bbottom"]), *self.scalePoints(*self.cords["Btop"]), fill = self.lineColor)
        self.canvas.create_line(*self.scalePoints(*self.cords["Btop"]), *self.scalePoints(*self.cords["Cright"]), fill = self.lineColor)
        self.canvas.create_line(*self.scalePoints(*self.cords["Cright"]), *self.scalePoints(*self.cords["19"]), fill = self.lineColor)
        
        self.canvas.create_line(*self.scalePoints(*self.cords["16"]), *self.scalePoints(*self.cords["6"]), fill = self.lineColor)


        for location in self.cords.keys():
            if(location not in ("Atop", "Abottom", "Bbottom", "Btop", "Cright")):
                self.canvas.create_oval(*self.ovalPoints(*self.scalePoints(*self.cords[location])), fill=self.iconColor)
# Original coordinates (with padding already accounted)
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

Marker_IDs = []

def draw_map(canvas, x1, y1, x2, y2, lineColor ='black', iconColor='green', cl=None):        
    
    x_scale = ((x2 - x1) - 90) / 340  # Subtracting 90 to account for 45 padding on both sides
    y_scale = ((y2 - y1) - 90) / 290  # Subtracting 90 to account for 45 padding on both sides
    
    
    #Scale the Points Based on Argument from original function call
    def scale_point(x, y):
        # Subtract the original padding (45) before scaling, then add 45 padding in the new rectangle
        new_x = x1 + 45 + (x - 45) * x_scale
        new_y = y1 + 45 + (y - 45) * y_scale
        return new_x, new_y

    
    if(cl):   
        global Marker_IDs
        if(len(Marker_IDs)>0):
            canvas.delete(Marker_IDs[0])
            Marker_IDs.pop()

        def marker_points(x,y):
            return x+6, y-9, x+12, y-3
        
        Marker_IDs.append(canvas.create_oval(*marker_points(*scale_point(*cords[cl])), fill='red'))

        return
    
    #Design the Base Map

    # Draw the map lines after scaling
    canvas.create_line(*scale_point(*cords["0"]), *scale_point(*cords["1"]), fill = lineColor)
    
    canvas.create_line(*scale_point(*cords["1"]), *scale_point(*cords["2"]), fill = lineColor)
    canvas.create_line(*scale_point(*cords["1"]), *scale_point(*cords["6"]), fill = lineColor)
    
    canvas.create_line(*scale_point(*cords["Atop"]), *scale_point(*cords["19"]), fill = lineColor)
    canvas.create_line(*scale_point(*cords["1"]), *scale_point(*cords["3"]), fill = lineColor)
    
    canvas.create_line(*scale_point(*cords["3"]), *scale_point(*cords["5"]), fill = lineColor)
    
    canvas.create_line(*scale_point(*cords["Atop"]), *scale_point(*cords["Abottom"]), fill = lineColor)
    canvas.create_line(*scale_point(*cords["Abottom"]), *scale_point(*cords["8"]), fill = lineColor)
    
    canvas.create_line(*scale_point(*cords["8"]), *scale_point(*cords["9"]), fill = lineColor)
    
    canvas.create_line(*scale_point(*cords["9"]), *scale_point(*cords["11"]), fill = lineColor)
    canvas.create_line(*scale_point(*cords["9"]), *scale_point(*cords["13"]), fill = lineColor)
    
    canvas.create_line(*scale_point(*cords["11"]), *scale_point(*cords["12"]), fill = lineColor)
    
    canvas.create_line(*scale_point(*cords["13"]), *scale_point(*cords["14"]), fill = lineColor)
    canvas.create_line(*scale_point(*cords["14"]), *scale_point(*cords["15"]), fill = lineColor)
    canvas.create_line(*scale_point(*cords["15"]), *scale_point(*cords["16"]), fill = lineColor)
    canvas.create_line(*scale_point(*cords["15"]), *scale_point(*cords["Bbottom"]), fill = lineColor)
    canvas.create_line(*scale_point(*cords["Bbottom"]), *scale_point(*cords["Btop"]), fill = lineColor)
    canvas.create_line(*scale_point(*cords["Btop"]), *scale_point(*cords["Cright"]), fill = lineColor)
    canvas.create_line(*scale_point(*cords["Cright"]), *scale_point(*cords["19"]), fill = lineColor)
    
    canvas.create_line(*scale_point(*cords["16"]), *scale_point(*cords["6"]), fill = lineColor)


    #5 Pixel Padding
    def oval_points(x,y):
        return x-5, y-5, x+5, y+5

    #Draw the Ovals at the Points of Locations
    for location in cords.keys():
        if(location not in ("Atop", "Abottom", "Bbottom", "Btop", "Cright")):
            canvas.create_oval(*oval_points(*scale_point(*cords[location])), fill=iconColor)



# import tkinter as tk

# root = tk.Tk()
# root.geometry('600x500')
# canvas = tk.Canvas(root, width=500, height=390, bg='gray')
# canvas.pack()
# draw_map(canvas, 0,0, 500, 390, cl='1')

# root.mainloop()

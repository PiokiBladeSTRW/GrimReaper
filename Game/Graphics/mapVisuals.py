def draw_map(canvas, x1, y1, x2, y2, lineColor ='black', iconColor='green'):
    import json
    import os
    
    loc_path = os.path.join(os.path.dirname(os.path.abspath(__file__)) , '../Travelling/locations.json')
    with open(loc_path, 'r') as LOC:
        Locations = json.load(LOC)

        
    x_scale = ((x2 - x1) - 90) / 340  # Subtracting 90 to account for 45 padding on both sides
    y_scale = ((y2 - y1) - 90) / 290  # Subtracting 90 to account for 45 padding on both sides

    # Original coordinates (with padding already accounted)
    cords = {        
        Locations["0"]: (260, 175),
        Locations["1"]: (260, 130),
        Locations["2"]: (260, 75),
        Locations["3"]: (260, 45),
        Locations["4"]: (280, 45),
        Locations["5"]: (300, 45),
        Locations["6"]: (155, 130),
        Locations["7"]: (150, 90),
        Locations["8"]: (90, 105),
        Locations["9"]: (90, 205),
        Locations["10"]: (67,205),
        Locations["11"]: (45, 205),
        Locations["12"]: (45, 115),
        Locations["13"]: (90, 290),
        Locations["14"]: (260, 290),
        Locations["15"]: (260, 255),
        Locations["16"]: (155, 255),
        Locations["17"]: (305, 237),        
        Locations["18"]: (325, 220),
        Locations["19"]: (345, 75),
        "Atop": (150, 75),
        "Abottom": (150, 105),
        "Bbottom": (305, 255),
        "Btop": (305, 220),
        "Cright": (345, 220)
    }
    
    def scale_point(x, y):
        # Subtract the original padding (45) before scaling, then add 45 padding in the new rectangle
        new_x = x1 + 45 + (x - 45) * x_scale
        new_y = y1 + 45 + (y - 45) * y_scale
        return new_x, new_y

    # Draw the map lines after scaling
    canvas.create_line(*scale_point(*cords[Locations["0"]]), *scale_point(*cords[Locations["1"]]), fill = lineColor)
    
    canvas.create_line(*scale_point(*cords[Locations["1"]]), *scale_point(*cords[Locations["2"]]), fill = lineColor)
    canvas.create_line(*scale_point(*cords[Locations["1"]]), *scale_point(*cords[Locations["6"]]), fill = lineColor)
    
    canvas.create_line(*scale_point(*cords["Atop"]), *scale_point(*cords[Locations["19"]]), fill = lineColor)
    canvas.create_line(*scale_point(*cords[Locations["1"]]), *scale_point(*cords[Locations["3"]]), fill = lineColor)
    
    canvas.create_line(*scale_point(*cords[Locations["3"]]), *scale_point(*cords[Locations["5"]]), fill = lineColor)
    
    canvas.create_line(*scale_point(*cords["Atop"]), *scale_point(*cords["Abottom"]), fill = lineColor)
    canvas.create_line(*scale_point(*cords["Abottom"]), *scale_point(*cords[Locations["8"]]), fill = lineColor)
    
    canvas.create_line(*scale_point(*cords[Locations["8"]]), *scale_point(*cords[Locations["9"]]), fill = lineColor)
    
    canvas.create_line(*scale_point(*cords[Locations["9"]]), *scale_point(*cords[Locations["11"]]), fill = lineColor)
    canvas.create_line(*scale_point(*cords[Locations["9"]]), *scale_point(*cords[Locations["13"]]), fill = lineColor)
    
    canvas.create_line(*scale_point(*cords[Locations["11"]]), *scale_point(*cords[Locations["12"]]), fill = lineColor)
    
    canvas.create_line(*scale_point(*cords[Locations["13"]]), *scale_point(*cords[Locations["14"]]), fill = lineColor)
    canvas.create_line(*scale_point(*cords[Locations["14"]]), *scale_point(*cords[Locations["15"]]), fill = lineColor)
    canvas.create_line(*scale_point(*cords[Locations["15"]]), *scale_point(*cords[Locations["16"]]), fill = lineColor)
    canvas.create_line(*scale_point(*cords[Locations["15"]]), *scale_point(*cords["Bbottom"]), fill = lineColor)
    canvas.create_line(*scale_point(*cords["Bbottom"]), *scale_point(*cords["Btop"]), fill = lineColor)
    canvas.create_line(*scale_point(*cords["Btop"]), *scale_point(*cords["Cright"]), fill = lineColor)
    canvas.create_line(*scale_point(*cords["Cright"]), *scale_point(*cords[Locations["19"]]), fill = lineColor)
    
    canvas.create_line(*scale_point(*cords[Locations["16"]]), *scale_point(*cords[Locations["6"]]), fill = lineColor)

    def oval_points(x,y):
        return x-5, y-5, x+5, y+5


    #Draw the Ovals at the Points of Interests
    for location in cords.keys():
        if(location not in ("Atop", "Abottom", "Bbottom", "Btop", "Cright")):
            canvas.create_oval(*oval_points(*scale_point(*cords[location])), fill=iconColor)
    




##import tkinter as tk
##
##root = tk.Tk()
##root.geometry('600x500')
##canvas = tk.Canvas(root, width=500, height=390, bg='gray')
##canvas.pack()
##draw_map(canvas, 0,0, 500, 390)
##
##root.mainloop()

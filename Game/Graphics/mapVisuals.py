def draw_map(canvas, x2, y2, x1, y1, color='black'):
    # Calculate scaling factors
    x_scale = ((x2 - x1) - 90) / 340  # Subtracting 90 to account for 45 padding on both sides
    y_scale = ((y2 - y1) - 90) / 290  # Subtracting 90 to account for 45 padding on both sides

    # Original coordinates (with padding already accounted in the original system)
    cords = {
        "Town Hall": (260, 175),
        "Forsaken Mansion": (260, 130),
        "Grim Gate": (260, 75),
        "Shade Bridge": (260, 45),
        "Forgotten Cemetery": (300, 45),
        "Lost Stories": (155, 130),
        "Atop": (150, 75),
        "Abottom": (150, 105),
        "Creep Wood": (90, 105),
        "Forsaken Bay": (90, 205),
        "Cursed Lighthouse": (45, 205),
        "Shadow Forest": (45, 115),
        "F": (90, 290),
        "E": (260, 290),
        "G": (260, 255),
        "Cursed Hollow": (155, 255),
        "Bbottom": (305, 255),
        "Btop": (305, 220),
        "Cright": (345, 220),
        "D": (345, 75)
    }

    # Function to scale a point
    def scale_point(x, y):
        # Subtract the original padding (45) before scaling, then add 45 padding in the new rectangle
        new_x = x1 + 45 + (x - 45) * x_scale
        new_y = y1 + 45 + (y - 45) * y_scale
        return new_x, new_y

    # Draw the map lines after scaling
    canvas.create_line(*scale_point(*cords["Town Hall"]), *scale_point(*cords["Forsaken Mansion"]), fill = color)
    
    canvas.create_line(*scale_point(*cords["Forsaken Mansion"]), *scale_point(*cords["Grim Gate"]), fill = color)
    canvas.create_line(*scale_point(*cords["Forsaken Mansion"]), *scale_point(*cords["Lost Stories"]), fill = color)
    
    canvas.create_line(*scale_point(*cords["Grim Gate"]), *scale_point(*cords["D"]), fill = color)
    canvas.create_line(*scale_point(*cords["Grim Gate"]), *scale_point(*cords["Atop"]), fill = color)
    canvas.create_line(*scale_point(*cords["Grim Gate"]), *scale_point(*cords["Shade Bridge"]), fill = color)
    
    canvas.create_line(*scale_point(*cords["Shade Bridge"]), *scale_point(*cords["Forgotten Cemetery"]), fill = color)
    
    canvas.create_line(*scale_point(*cords["Atop"]), *scale_point(*cords["Abottom"]), fill = color)
    canvas.create_line(*scale_point(*cords["Abottom"]), *scale_point(*cords["Creep Wood"]), fill = color)
    
    canvas.create_line(*scale_point(*cords["Creep Wood"]), *scale_point(*cords["Forsaken Bay"]), fill = color)
    
    canvas.create_line(*scale_point(*cords["Forsaken Bay"]), *scale_point(*cords["Cursed Lighthouse"]), fill = color)
    canvas.create_line(*scale_point(*cords["Forsaken Bay"]), *scale_point(*cords["F"]), fill = color)
    
    canvas.create_line(*scale_point(*cords["Cursed Lighthouse"]), *scale_point(*cords["Shadow Forest"]), fill = color)
    
    canvas.create_line(*scale_point(*cords["F"]), *scale_point(*cords["E"]), fill = color)
    canvas.create_line(*scale_point(*cords["E"]), *scale_point(*cords["G"]), fill = color)
    canvas.create_line(*scale_point(*cords["G"]), *scale_point(*cords["Cursed Hollow"]), fill = color)
    canvas.create_line(*scale_point(*cords["G"]), *scale_point(*cords["Bbottom"]), fill = color)
    canvas.create_line(*scale_point(*cords["Bbottom"]), *scale_point(*cords["Btop"]), fill = color)
    canvas.create_line(*scale_point(*cords["Btop"]), *scale_point(*cords["Cright"]), fill = color)
    canvas.create_line(*scale_point(*cords["Cright"]), *scale_point(*cords["D"]), fill = color)
    
    canvas.create_line(*scale_point(*cords["Cursed Hollow"]), *scale_point(*cords["Lost Stories"]), fill = color)





##
##import tkinter as tk
##
##root = tk.Tk()
##root.geometry('600x500')
##canvas = tk.Canvas(root, width=500, height=390, bg='gray')
##canvas.pack()
##draw_map(canvas, 500, 390, 0, 0)
##
##root.mainloop()

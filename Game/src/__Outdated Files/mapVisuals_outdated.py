##def draw_map(canvas, x2, y2,  x1, y1):
##    x_scale = ((x2-x1)-90) /340
##    y_scale = ((y2-y1)-90) /290
##    
##    cords= {
##        "Town Hall" : (x+215, y+130),
##        "Forsaken Mansion": (x+215, y+85),
##        "Grim Gate" : (x+215, y+30),
##        "Shade Bridge": (x+215, y),
##        "En Hill": (x+220, y),
##        "Forgotten Cemetary": (x+255, y),
##        "Lost Stories": (x+110, y+85),
##        "Atop": (x+105,y+30),
##        "Abottom": (x+105, y+60),
##        "Creep Wood": (x+45,y+60),
##        "Forsaken Bay": (x+45, y+160),
##        "Lake": (x+165,y+160),
##        "Cursed Lighthouse": (x, y+160),
##        "Shadow Forest": (x, y+70),
##        "F": (x+45, y+245),
##        "E" :(x+215, y+245),
##        "G": (x+215, y+ 210),
##        "Cursed Hollow": (x+110,y+210),
##        "Bbottom": (x+260,y+210),
##        "Btop": (x+260, y+175),
##        "Cright": (x+ 300,  y+175),
##        "D": (x+300,y+30)
##        }
##
##    
##
##    canvas.create_line(cords["Town Hall"][0], cords["Town Hall"][1], cords["Forsaken Mansion"][0], cords["Forsaken Mansion"][1])
##    canvas.create_line(cords["Forsaken Mansion"][0], cords["Forsaken Mansion"][1], cords["Grim Gate"][0], cords["Grim Gate"][1])
##    canvas.create_line(cords["Forsaken Mansion"][0], cords["Forsaken Mansion"][1], cords["Lost Stories"][0], cords["Lost Stories"][1])
##    canvas.create_line(cords["Grim Gate"][0], cords["Grim Gate"][1], cords["D"][0], cords["D"][1])
##    canvas.create_line(cords["Grim Gate"][0], cords["Grim Gate"][1], cords["Atop"][0], cords["Atop"][1])
##    canvas.create_line(cords["Grim Gate"][0], cords["Grim Gate"][1], cords["Shade Bridge"][0], cords["Shade Bridge"][1])
##    canvas.create_line(cords["Shade Bridge"][0], cords["Shade Bridge"][1],  cords["Forgotten Cemetary"][0], cords["Forgotten Cemetary"][1])
##    canvas.create_line(cords["Atop"][0], cords["Atop"][1], cords["Abottom"][0], cords["Abottom"][1])
##    canvas.create_line(cords["Abottom"][0], cords["Abottom"][1], cords["Creep Wood"][0], cords["Creep Wood"][1])
##    canvas.create_line(cords["Creep Wood"][0], cords["Creep Wood"][1], cords["Forsaken Bay"][0], cords["Forsaken Bay"][1])
##    canvas.create_line(cords["Forsaken Bay"][0], cords["Forsaken Bay"][1],  cords["Cursed Lighthouse"][0], cords["Cursed Lighthouse"][1])
##    canvas.create_line(cords["Forsaken Bay"][0], cords["Forsaken Bay"][1], cords["F"][0], cords["F"][1])
##    canvas.create_line(cords["Cursed Lighthouse"][0], cords["Cursed Lighthouse"][1], cords["Shadow Forest"][0], cords["Shadow Forest"][1])
##    canvas.create_line(cords["F"][0], cords["F"][1], cords["E"][0], cords["E"][1])
##    canvas.create_line(cords["E"][0], cords["E"][1], cords["G"][0], cords["G"][1])
##    canvas.create_line(cords["G"][0], cords["G"][1], cords["Cursed Hollow"][0], cords["Cursed Hollow"][1])
##    canvas.create_line(cords["G"][0], cords["G"][1], cords["Bbottom"][0], cords["Bbottom"][1])
##    canvas.create_line(cords["Bbottom"][0], cords["Bbottom"][1], cords["Btop"][0], cords["Btop"][1])
##    canvas.create_line(cords["Btop"][0], cords["Btop"][1], cords["Cright"][0], cords["Cright"][1])
##    canvas.create_line(cords["Cright"][0], cords["Cright"][1], cords["D"][0], cords["D"][1])
##    canvas.create_line(cords["Cursed Hollow"][0], cords["Cursed Hollow"][1], cords["Lost Stories"][0], cords["Lost Stories"][1])
      
##    # Adjusted y values
##    canvas.create_line(400, 80, 650, 80)         # A to D intersecting Grim Gate
##    canvas.create_line(650, 80, 650, 240)        # D to C
##    canvas.create_line(650, 240, 600, 240)       # C to Halfway B
##    canvas.create_line(600, 240, 600, 280)       # C to Other Halfway B
##    canvas.create_line(600, 280, 450, 280)       # B to Cursed Hollow
##    canvas.create_line(450, 280, 450, 130)        # Cursed Hollow to Lost Stories
##    canvas.create_line(450, 130, 550, 130)         # Lost Stories to Forsaken Mansion
##    canvas.create_line(550, 40, 550, 160)        # Shade Bridge to Town Hall
##    canvas.create_line(550, 280, 550, 320)       # G to E    
##    canvas.create_line(550, 40, 630, 40)         # Shade Bridge to Forgotten Cemetery
##    canvas.create_line(550, 320, 350, 320)       # E to F
##    canvas.create_line(350, 320, 350, 110)        # F to Creep Wood
##    canvas.create_line(350, 110, 400, 110)         # Creep Wood to halfway A'
##    canvas.create_line(400, 110, 400, 80)         # Creep Wood to Other Halfway A
##    canvas.create_line(350, 256, 290, 256)       # Forsaken Bay to Cursed Lighthouse
##    canvas.create_line(290, 256, 290, 150)       # Cursed Lighthouse to Shadow Forest

##    canvas.create_oval(645, 70, 655, 80, fill='green')   # D
##    canvas.create_oval(545, 70, 555, 80, fill='green')   # Grim Gate
##    canvas.create_oval(545, 115, 555, 125, fill='green') # Forsaken Mansion
##    canvas.create_oval(445, 115, 455, 125, fill='green') # Lost Stories
##    canvas.create_oval(445, 280, 455, 290, fill='green') # Cursed Hollow
##    canvas.create_oval(545, 280, 555, 290, fill='green') # G
##    canvas.create_oval(545, 35, 555, 45, fill='green')   # Shade Bridge
##    canvas.create_oval(625, 35, 635, 45, fill='green')   # Forgotten Cemetery
##    canvas.create_oval(545, 195, 555, 205, fill='green')  # E
##    canvas.create_oval(245, 195, 255, 205, fill='green')  # F
##    canvas.create_oval(245, 160, 255, 170, fill='green')  # Forsaken Bay
##    canvas.create_oval(85, 160, 95, 170, fill='green')    # Cursed Lighthouse
##    canvas.create_oval(85, 130, 95, 140, fill='green')    # Shadow Forest
##    canvas.create_oval(245, 80, 255, 90, fill='green')    # Creep Wood
##    canvas.create_oval(295, 65, 305, 75, fill='green')    # A
##    canvas.create_oval(620, 150, 630, 160, fill='green')  # C
##    canvas.create_oval(595, 160, 605, 170, fill='green')  # B
##
##    canvas.create_rectangle(318, 124, 322, 144, fill='blue')  # Lack
##    canvas.create_rectangle(588, 16, 592, 36, fill='gray')    # En Hill



##import tkinter as tk
##
##root = tk.Tk()
##root.geometry('600x500')
##canvas = tk.Canvas(root, width=500, height=390, bg='gray')
##canvas.pack()
##draw_map(canvas, 500, 390, 0, 0)
##
##root.mainloop()

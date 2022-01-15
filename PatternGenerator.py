import PySimpleGUI as sg
from PIL import Image, ImageFont, ImageDraw
from tkinter import messagebox
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def num_occurence(num, patternnum) :
    x = 0
    occurence = 0
    for x in ["0","1","2","3"] :
        if(patternnum[int(x)] == num):   
            occurence += 1
    return occurence

def paste_picture(width, height, resize, filename, basepic, xposition, yposition, rotateangle) :
    width = int((width - 0) * resize)
    height = int((height - 0) * resize)
    fileinclupath = resource_path(filename)
    im = Image.open(fileinclupath).rotate(angle=rotateangle, resample=0, expand=0, center=None, translate=None, fillcolor=None) 
    im = im.resize((width, height))
    basepic.paste(im, (xposition, yposition),im)
    return basepic

def display_pattern(patternnum) :
    
    absolutepath = os.path.dirname(os.path.realpath('__file__')) 
    
    #basepath = absolutepath+"\\image\\";
    #filename1 = basepath + patternnum[0] +".png"
    #filename2 = basepath + patternnum[1] +".png"
    #filename3 = basepath + patternnum[2] +".png"
    #filename4 = basepath + patternnum[3] +".png"
    
    filename1 = patternnum[0] +".png"
    filename2 = patternnum[1] +".png"
    filename3 = patternnum[2] +".png"
    filename4 = patternnum[3] +".png"

   #imwh = Image.open(basepath+"blank.png")

    imwh = Image.open(resource_path("blank.png"))
    
    d1 = ImageDraw.Draw(imwh)
    #myFont = ImageFont.truetype(absolutepath+"\\font\\calibrib.ttf", 65)
    myFont = ImageFont.truetype(resource_path("calibrib.ttf"), 65)
    d1.text((0, 0), patternnum, font=myFont, fill=(0, 0, 0))
    
    fileinclupath = resource_path(filename1)
    im1 = Image.open(fileinclupath)
    
    rotation1 = 0
    rotation2 = 0
    rotation3 = 0
    
    occurrenceof3 = num_occurence("3", patternnum)
    occurrenceof4 = num_occurence("4", patternnum)
    occurrenceof6 = num_occurence("6", patternnum)
    
    #print("Occurrence", occurrenceof3, occurrenceof4, occurrenceof6)
    
    if(occurrenceof3 > 0 or occurrenceof6 > 0 or occurrenceof4 > 0 ) :
            if(occurrenceof3 > 1 and occurrenceof6 <= 1 and occurrenceof4 <= 1) or (occurrenceof6 > 1 and occurrenceof3 <= 1 and occurrenceof4 <= 1)  :
                #print("Inside 3 or 6 more")                
                if(occurrenceof3 == 4 or occurrenceof6 == 4) :
                    rotation1 = 180
                    rotation2 = 0
                    rotation3 = 180
                elif(occurrenceof3 == 3) :
                    if patternnum.find("3") == 0 :
                        rotation1 = 180
                    elif patternnum.find("3") == 1 :
                        rotation2 = 180
                elif(occurrenceof6 == 3) :
                    if patternnum.find("6") == 0 :
                        rotation1 = 180
                    elif patternnum.find("6") == 1 :
                        rotation2 = 180
                elif(occurrenceof3 == 2) :
                    if patternnum.rfind("3") == 1 :
                        rotation1 = 180
                    elif patternnum.rfind("3") == 2 :
                        rotation2 = 180
                    elif patternnum.rfind("3") == 3 :
                        rotation3 = 180
                elif(occurrenceof6 == 2) :
                    if patternnum.rfind("6") == 1 :
                        rotation1 = 180
                    elif patternnum.rfind("6") == 2 :
                        rotation2 = 180
                    elif patternnum.rfind("6") == 3 :
                        rotation3 = 180        
            elif (occurrenceof3 == 2 and occurrenceof6 == 2 ) :
                #print("Inside 3 and 6 dual")
                if patternnum.rfind("3") == 1 :
                     rotation1 = 180
                elif patternnum.rfind("3") == 2 :
                     rotation2 = 180
                elif patternnum.rfind("3") == 3 :
                    rotation3 = 180
                if patternnum.rfind("6") == 1 :
                    rotation1 = 180
                elif patternnum.rfind("6") == 2 :
                    rotation2 = 180
                elif patternnum.rfind("6") == 3 :
                    rotation3 = 180            
            elif(occurrenceof4 == 2  and (occurrenceof3 == 2 or occurrenceof6 == 2)) :
                #print("Inside 4 dual and 3 or 6 dual")
                if patternnum.rfind("3") == 1 :
                     rotation1 = 180
                elif patternnum.rfind("3") == 2 :
                     rotation2 = 180
                elif patternnum.rfind("3") == 3 :
                    rotation3 = 180
                if patternnum.rfind("6") == 1 :
                    rotation1 = 180
                elif patternnum.rfind("6") == 2 :
                    rotation2 = 180
                elif patternnum.rfind("6") == 3 :
                    rotation3 = 180       
                if patternnum.rfind("4") == 1 :
                    rotation1 = 45
                elif patternnum.rfind("4") == 2 :
                    rotation2 = 45
                elif patternnum.rfind("4") == 3 :
                    rotation3 = 45       
      
            elif((occurrenceof4 > 1  and occurrenceof3 <= 1) or (occurrenceof4 > 1  and occurrenceof6 <= 1)) :
                    #print("Inside 4 more")
                    if(patternnum[0] == patternnum[1]) and patternnum[0] == "4" :
                            rotation1 = 45
    
                    if(rotation1 == 45 and patternnum[0] == patternnum[2] and patternnum[0] == "4" ) :
                            rotation2 = 180 # can be 0
                    else :
                        if(patternnum[2] == "4" and rotation1 == 0 and (patternnum[0] == patternnum[2] or patternnum[1] == patternnum[2] )) :
                            rotation2 = 45

                    if((rotation1 != 0 and rotation2 != 0) and patternnum[0] == patternnum[3] and patternnum[3] == "4" ) :
                        rotation3 = 45
                    else : 
                        if(patternnum[3] == "4" and (rotation1 != 0 or rotation2 != 0) and (patternnum[0] == patternnum[3] or patternnum[1] == patternnum[3])) :
                            rotation3 = 180 # can be 0
                        else :
                            if(patternnum[3] == "4" and (rotation1 == 0 and rotation2 == 0) and (patternnum[0] == patternnum[3] or patternnum[1] == patternnum[3]  or patternnum[2] == patternnum[3])) :
                                rotation3 = 45

    #print("Rotation angle : ", rotation1, rotation2, rotation3)
    
    imconsol = im1.copy()
    
    imconsol = paste_picture(width=1162, height=1162, resize=0.56, filename=filename2, basepic=imconsol, xposition=240, yposition=248, rotateangle=rotation1)
    
    imconsol = paste_picture(width=1162, height=1162, resize=0.30, filename=filename3, basepic=imconsol, xposition=382, yposition=408, rotateangle=rotation2)
    
    imconsol = paste_picture(width=1162, height=1162, resize=0.15, filename=filename4, basepic=imconsol, xposition=467, yposition=493, rotateangle=rotation3)
    
    #imwh.paste(imconsol, (0,0), imconsol)
    imwh = Image.alpha_composite(imwh, imconsol)
    
    imwh.putalpha(256) 
    
    return imwh

sg.theme('LightBlue')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Please enter pattern numbers (e.g. 4123, 6123-6234)')],
            [sg.InputText(default_text = "")],
            [sg.Button('Cancel'), sg.Button('Display')] ]

# Create the Window
window = sg.Window('Pattern Generator', layout, use_default_focus = True)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    sg.InputText(focus = True)
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    patternnum = values[0]

    genpath = resource_path("GenFiles")
    isExist = os.path.isdir(genpath)
    if(isExist == False) :
         os.mkdir(genpath)

    if len(patternnum) < 4 :
            messagebox.showinfo("Error","Please enter valid value")
            #print('Please enter valid value')
            #pass
    else :
        if patternnum.find("-") == -1 :
            #print('You entered ', patternnum)
            imwh = display_pattern(patternnum)
            savefile = genpath+"\\"+patternnum+".png";
            imwh.save(savefile)

            #if(event == 'Display') :
            os.startfile(savefile, "open")
            #elif(event == 'Print') :
                #os.startfile(savefile, "print")
                #messagebox.showinfo("Information","Image Printed - " + savefile)
            sg.InputText("",focus = True)
        else :
            if len(patternnum) != 9 :
                messagebox.showinfo("Error","Please enter valid value")
            else : 
                #print('You entered range values' , patternnum[:4])
                #print('You entered range values' , patternnum[5:9])
                
                startnum = int(patternnum[:4])
                endnum = int(patternnum[5:9])
                if endnum < startnum :
                    messagebox.showinfo("Error","Please enter valid range")
                    continue
                elif endnum - startnum > 100 :
                    messagebox.showinfo("Error","Please enter a range not exceeding 100")
                    continue
                imagelist = []
                counter = startnum
                
                if endnum - startnum > 20 :
                    messagebox.showinfo("Info","Please wait as this will take sometime")
                    
                while counter <= endnum :
                    #print(counter)
                    str_counter = str(counter)
                    if(str_counter.find("0") != -1) :
                        counter += 1
                        continue
                    else :
                        counter += 1
                        imwh = display_pattern(str_counter)
                        imwh = imwh.convert("RGB")
                        imagelist.append(imwh)
                    savefile = genpath+"\\Consolidated.pdf";     
                    imagelist[0].save(savefile, "PDF" ,resolution=100.0, save_all=True, append_images=imagelist[1:])    
      
            #if(event == 'Display') :
            os.startfile(savefile, "open")
                #messagebox.showinfo("Information","Files saved @" + savefile)
            #elif(event == 'Print') :
                #os.startfile(savefile, "print")
                #messagebox.showinfo("Information","Print initiated. Please continue printing in print dialog")
            sg.InputText("",focus = True)
            
window.close()
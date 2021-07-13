from tkinter import *
root = Tk(className='Python Example')
root.geometry("700x500")
root.title('Mad Libs Generator')
Label(root , text = 'Welcome to Mad Libs Generator \n have fun!', font = 'arial 20 bold').pack()
Label(root , text = 'Click Any one :' , font = 'arial 15 bold' ).place(x = 40 , y = 80)


# function for first Mad Lib


def madlib1():

    def newmad1():

        newmad = Tk()
        newmad.geometry("1200x300")
        newmad.title("final output")

        Label(newmad , text = ('say ' + str(foodentry.get()) + ', the photographer said as the camera flashed! ' + str(nameentry.get()) + ' and I had gone to ' + str(placeentry.get()) +' to get our photos taken on my birthday. \nThe first photo we really wanted was a picture of us dressed as ' + str(animalsentry.get()) + ' pretending to be a ' + str(professionentry.get()) + '.\n when we saw the second photo, it was exactly what I wanted. \nWe both looked like ' + str(thingsentry.get()) + ' wearing ' + str(clothentry.get()) + ' and ' + str(verbentry.get()) + ' --exactly what I had in mind')).pack()
        Button(newmad , text = 'Exit' , font = 'arial 15 bold', command = lambda:newmad.destroy() ,  bg = 'light green').place(x = 590 , y  = 100)

    
    #new Window
    photowin = Tk()
    photowin.geometry("600x400")
    #Heading
    Label(photowin , text = "Enter the Data" , font  = "comicsansms 13 bold").grid(row = 0 , column = 3)

    #Text for our data

    animals = Label(photowin , text = "Enter a animals name")
    profession = Label(photowin , text = "Enter a profession name")
    food = Label(photowin , text  = "Enter a food name")
    name = Label(photowin , text = "Enter a  name")
    place = Label(photowin , text = "Enter a place name")
    things = Label(photowin , text = "Enter a thing name")
    cloth = Label(photowin , text = "Enter a cloth type")
    verb = Label(photowin , text = "Enter a verb ")

    #Pack text for our form
    animals.grid(row = 1 , column = 2)
    profession.grid(row = 2 , column = 2)
    food.grid(row = 3 , column = 2)
    name.grid(row = 4 , column = 2)
    place.grid(row = 5 , column = 2)
    things.grid(row = 6 , column = 2)
    cloth.grid(row = 7 , column = 2)
    verb.grid(row = 8 , column = 2)

    # Tkinter variable for storing entries
    animalsvalue = StringVar()
    professionvalue = StringVar()
    foodvalue = StringVar()
    namevalue = StringVar()
    placevalue = StringVar()
    thingsvalue = StringVar()
    clothvalue = StringVar()
    verbvalue = StringVar()

    #Entries
    animalsentry = Entry(photowin , textvariable = animalsvalue)
    professionentry = Entry(photowin , textvariable = professionvalue)
    foodentry = Entry(photowin , textvariable = foodvalue)
    nameentry = Entry(photowin , textvariable = namevalue)
    placeentry = Entry(photowin , textvariable = placevalue)
    thingsentry = Entry(photowin , textvariable = thingsvalue)
    clothentry = Entry(photowin , textvariable = clothvalue)
    verbentry = Entry(photowin , textvariable = verbvalue)

    #Packing the Entries
    animalsentry.grid(row = 1 , column = 3)
    professionentry.grid(row = 2 , column = 3)
    foodentry.grid(row = 3 , column = 3)
    nameentry.grid(row = 4, column = 3)
    placeentry.grid(row = 5 , column = 3)
    thingsentry.grid(row = 6 , column = 3)
    clothentry.grid(row = 7 , column = 3)
    verbentry.grid(row = 8, column = 3)

    Button(photowin , text = "output" , command = newmad1 , font = "arial 15 bold").place(x = 300 , y = 300)
    Button(photowin , text = "Exit" , font = "arial 15 bold" , command = lambda:photowin.destroy()).place(x = 500 , y = 300)

    

def madlib2():

    def newmad2():

        newmad_s = Tk()
        newmad_s.geometry("1200x400")
        newmad_s.title("final output")

        Label(newmad_s , text = ('Last night I dreamed I was a ' +str(adjectiveentry.get())+ ' butterfly with ' + str(colorentry.get())+ ' splocthes that looked like '+str(thingentry.get())+ ' \n.I flew to ' + str(placeentry.get())+ ' with my bestfriend and '+str(personentry.get())+ ' who was a '+str(adjective1entry.get()) + ' ' + str(insectentry.get()) +' .\nWe ate some ' + str(foodentry.get()) + ' when we got there and then decided to '+ str(verbentry.get()) + ' and the dream ended when I said-- lets ' + str(verbentry.get()) + '.')).pack()
        Button(newmad_s , text = 'Exit' , font = 'arial 15 bold', command = lambda:newmad_s.destroy() ,  bg = 'light green').place(x = 590 , y  = 100)


    #new Window
    BFwin = Tk()
    BFwin.geometry("600x400")
    #Heading
    Label(BFwin , text = "Enter the Data" , font  = "comicsansms 13 bold").grid(row = 0 , column = 3)

    #Text for our data

    adjective = Label(BFwin , text = "Enter an adjective name")
    color = Label(BFwin , text = "Enter a color name")
    food = Label(BFwin , text  = "Enter a food name")
    person = Label(BFwin , text = "Enter a Person name")
    place = Label(BFwin , text = "Enter a place name")
    thing = Label(BFwin , text = "Enter a thing name")
    adjective1 = Label(BFwin , text = "Enter an adjective")
    verb = Label(BFwin , text = "Enter a verb ")
    insect = Label(BFwin , text = "Enter an insect name ")

    #Pack text for our form
    adjective.grid(row = 1 , column = 2)
    color.grid(row = 2 , column = 2)
    food.grid(row = 3 , column = 2)
    person.grid(row = 4 , column = 2)
    place.grid(row = 5 , column = 2)
    thing.grid(row = 6 , column = 2)
    adjective1.grid(row = 7 , column = 2)
    verb.grid(row = 8 , column = 2)
    insect.grid(row = 9 , column = 2)

    # Tkinter variable for storing entries
    adjectivevalue = StringVar()
    colorvalue = StringVar()
    foodvalue = StringVar()
    personvalue = StringVar()
    placevalue = StringVar()
    thingvalue = StringVar()
    adjective1value = StringVar()
    verbvalue = StringVar()
    insectvalue = StringVar()

    #Entries
    adjectiveentry = Entry(BFwin , textvariable = adjectivevalue)
    colorentry = Entry(BFwin , textvariable = colorvalue)
    foodentry = Entry(BFwin , textvariable = foodvalue)
    personentry = Entry(BFwin , textvariable = personvalue)
    placeentry = Entry(BFwin , textvariable = placevalue)
    thingentry = Entry(BFwin , textvariable = thingvalue)
    adjective1entry = Entry(BFwin , textvariable = adjective1value)
    verbentry = Entry(BFwin , textvariable = verbvalue)
    insectentry = Entry(BFwin , textvariable = insectvalue)

    #Packing the Entries
    adjectiveentry.grid(row = 1 , column = 3)
    colorentry.grid(row = 2 , column = 3)
    foodentry.grid(row = 3 , column = 3)
    personentry.grid(row = 4, column = 3)
    placeentry.grid(row = 5 , column = 3)
    thingentry.grid(row = 6 , column = 3)
    adjective1entry.grid(row = 7 , column = 3)
    verbentry.grid(row = 8, column = 3)
    insectentry.grid(row = 9 , column = 3)

    Button(BFwin, text = "output" , command = newmad2 , font = "arial 15 bold").place(x = 300 , y = 300)
    Button(BFwin , text = "Exit" , font = "arial 15 bold" , command = lambda:BFwin.destroy()).place(x = 500 , y = 300)


    


def madlib3():

   

    def newmad3():

        newmad_A = Tk()
        newmad_A.geometry("1200x400")
        newmad_A.title("final output")

        Label(newmad_A , text = ('Today we picked apple from '+str(personentry.get())+ "'s Orchard. \n had no idea there were so many different varieties of apples. \nI ate " +str(colorentry.get())+ ' apples straight off the tree that tested like '+str(foodsentry.get())+ '. \nThen there was a '+str(adjectiveentry.get())+ ' apple that looked like a ' + str(thingentry.get()) + '.When our bag were full, we went on a free hay ride to '+str(placeentry.get())+ ' and back. \nIt ended at a hay pile where we got to ' +str(verbentry.get())+ ' ' +str(adverbentry.get())+ '. \nI can hardly wait to get home and cook with the apples. \nWe are going to make apple '+str(foodentry.get())+ ' and '+str(thingsentry.get())+' pies!.')).pack()
        
        Button(newmad_A , text = 'Exit' , font = 'arial 15 bold', command = lambda:newmad_A.destroy() ,  bg = 'light green').place(x = 590 , y  = 150)

       

    #new Window
    AAwin = Tk()
    AAwin.geometry("600x400")
    #Heading
    Label(AAwin , text = "Enter the Data" , font  = "comicsansms 13 bold").grid(row = 0 , column = 3)

    #Text for our data

    adjective = Label(AAwin , text = "Enter an adjective name")
    color = Label(AAwin , text = "Enter a color name")
    food = Label(AAwin , text  = "Enter a food name")
    person = Label(AAwin , text = "Enter a Person name")
    place = Label(AAwin , text = "Enter a place name")
    thing = Label(AAwin , text = "Enter a thing name")
    adverb = Label(AAwin , text = "Enter an adverb")
    verb = Label(AAwin , text = "Enter a verb ")
    things = Label(AAwin , text = "Enter an thing name ")
    foods = Label(AAwin , text = "Enter a food name")

    #Pack text for our form
    adjective.grid(row = 1 , column = 2)
    color.grid(row = 2 , column = 2)
    food.grid(row = 3 , column = 2)
    person.grid(row = 4 , column = 2)
    place.grid(row = 5 , column = 2)
    thing.grid(row = 6 , column = 2)
    adverb.grid(row = 7 , column = 2)
    verb.grid(row = 8 , column = 2)
    things.grid(row = 9 , column = 2)
    foods.grid(row = 10 , column = 2)

    # Tkinter variable for storing entries
    adjectivevalue = StringVar()
    colorvalue = StringVar()
    foodvalue = StringVar()
    personvalue = StringVar()
    placevalue = StringVar()
    thingvalue = StringVar()
    adverbvalue = StringVar()
    verbvalue = StringVar()
    thingsvalue = StringVar()
    foodsvalue = StringVar()

    #Entries
    adjectiveentry = Entry(AAwin , textvariable = adjectivevalue)
    colorentry = Entry(AAwin , textvariable = colorvalue)
    foodentry = Entry(AAwin , textvariable = foodvalue)
    personentry = Entry(AAwin , textvariable = personvalue)
    placeentry = Entry(AAwin , textvariable = placevalue)
    thingentry = Entry(AAwin , textvariable = thingvalue)
    adverbentry = Entry(AAwin , textvariable = adverbvalue)
    verbentry = Entry(AAwin , textvariable = verbvalue)
    thingsentry = Entry(AAwin , textvariable = thingsvalue)
    foodsentry = Entry(AAwin , textvariable = foodsvalue)

    #Packing the Entries
    adjectiveentry.grid(row = 1 , column = 3)
    colorentry.grid(row = 2 , column = 3)
    foodentry.grid(row = 3 , column = 3)
    personentry.grid(row = 4, column = 3)
    placeentry.grid(row = 5 , column = 3)
    thingentry.grid(row = 6 , column = 3)
    adverbentry.grid(row = 7 , column = 3)
    verbentry.grid(row = 8, column = 3)
    thingsentry.grid(row = 9 , column = 3)
    foodsentry.grid(row = 10 , column = 3)

    Button(AAwin, text = "output" , command = newmad3 , font = "arial 15 bold").place(x = 300 , y = 300)
    Button(AAwin, text = "Exit" , font = "arial 15 bold" , command = lambda:AAwin.destroy()).place(x = 500 , y = 300)



def madlib4():

    def newmad4():
        newmad_F = Tk()
        newmad_F.geometry("1000x400")
        newmad_F.title("Output")

        Label(newmad_F , text = ("It does'nt matter if you're Irish...on St. Patrick's Day everybody wears shamrocks on their " + str(bodyentry.get())) , font = "arial 15 bold").pack()

        Button(newmad_F , text = 'Exit' , font = 'arial 15 bold', command = lambda:newmad_F.destroy() ,  bg = 'light green').place(x = 470 , y  = 100)

    #new Window
    funwin = Tk()
    funwin.geometry("600x400")
    funwin.title("Fun")
    #Heading

    Label(funwin , text = "Enter the Data" , font  = "comicsansms 13 bold").grid(row = 0 , column = 3)

    #Enter the data
    body = Label(funwin , text = "Enter body part name" , font = "arial 15 bold")

    #pack text for our form
    body.grid(row = 1 , column = 2)

    #Tkinter variable for storing values
    bodyvalue = StringVar()

    #Entries
    bodyentry = Entry(funwin , textvariable = bodyvalue)

    #packing the Entries
    bodyentry.grid(row = 1 , column = 3)

    Button(funwin , text = "output" , command = newmad4 , font = "arial 15 bold").place(x = 300 , y = 300)
    Button(funwin , text = "Exit" , font = "arial 15 bold" , command = lambda:funwin.destroy()).place(x = 500 , y = 300)

     

def exit():

    root.destroy();

Button(root , text = 'The photographer' , font = 'arial 16 bold' , command = madlib1,bg = 'lightgreen' ).place(x = 20, y = 150)
Button(root , text = 'Apple apple' , font = 'arial 16 bold' , command = madlib3,bg = 'light green' ).place(x = 200 , y = 250)
Button(root , text = 'The butterfly' , font = 'arial 16 bold' , command = madlib2,bg = 'light green' ).place(x = 400 , y = 350)
Button(root , text = 'The Fun' , font = 'arial 15 bold', command = madlib4 ,  bg = 'light green').place(x = 590 , y  = 450)
Button(root , text = 'Exit' , font = 'arial 15 bold', command = exit ,  bg = 'light green').place(x = 590 , y  = 20)

root.mainloop()
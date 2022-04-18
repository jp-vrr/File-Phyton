
Question = input("Create a file = 1, read a file = 2 or add a file = 3")

if Question == "1":
      f= open( "Texte.txt" , "w+" )

      f.close()
elif Question == "2":
    f = open("Texte.txt" , "r")

    if f.mode == 'r':
        contents =f.read()
        print(contents)
        f.close()

elif Question == "3":
    f = open("Texte.txt" , "a+")
    Add = input("Write what you want in the file")

    f.write(Add)
    f.close()

else :
    print("Enter a valid character")






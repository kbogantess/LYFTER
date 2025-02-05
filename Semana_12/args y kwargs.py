def nombres (*nombres):
    for i in nombres:
        print(i)

nombres("A", "B", "C","D")



############################################################
print("###################################################")
############################################################



def show_info(**kwargs): #Acá puede ir la info que tiene show_info
    for key, value in kwargs.items():
        print(f"{key} : {value}")

show_info(name ="Kev", age="19", city = "H") #Acá puede ir **kwargs as parameter
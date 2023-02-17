# light_theme={
#     "button":"red",
#     "title":"blue"
# }

# dark_theme={
#     "button":"black",
#     "title":"white"
# }


# av=56

# def average(a,b):
#     av=(a + b)/2

#     return av

# print(av)

# m=30
# y=40

# def check(a):
#     x=a*5
#     x=m+y

#     return x

# global variables=m,y
# local variable=x





# person ={
#     "name":"cathy",
#     "age":"26",
#     "pets":{
#         "dog":"x",
#         "cat":"y" 
#     }
# }

# person["pets"]


# profile={}
# profile["username"] = "user123"
# profile["age"]=20
# profile["email"]="mishybie@gmail.com"

profile={}

def register():
    username =input("Enter a username:")
    email=input("Enter email:")
    password=input("Enter password:")

#store in a dictionary
    profile["username"]=username
    profile["email"]=email
    profile["password"]=password

def get_profile():

    print(profile)

def change_username():
    new_username=input("Enter new username")
    profile["username"]= new_username
    
register()
get_profile()

change_username()
get_profile()
#ask for password
pwd = input("what is the master password\n")
def view():
    with open('passwords.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            name,pw = data.split("|")
            print("Name: ", name, "     *****        Password: ",pw)
def add():
    name = input('Account Name: ')
    pw = input('Password: ')
    with open('passwords.txt','a') as f:
        f.write(name + "|" + pw +"\n")

while True:
    mode = input ("would you like to add a new password or view the existing once (view,add)? or press q to quit\n")
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        continue
    
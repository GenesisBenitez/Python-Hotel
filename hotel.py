firstName = input("First Name: ")
lastName = input("Last Name: ")

print("Hello, Welcome Ms." + lastName + " Welcome to the Riverton Hotel.")

reservation = input("Do you have a reservation with us?")
if(reservation == "yes"):
    print("Lovely, your room is ready for you.")
    print("We hope you enjoy your stay with us")
else:
    print("No issues we can book for one for you now.")
    preferedRoom = input("We have rooms 111,222,333 available. Would you like on of these rooms, if so tell us the room you prefer: ")
    print("Excellent Ms." +lastName + ", we have room " + preferedRoom + " ready for you")
    print("We hope you enjoy your stay with us")
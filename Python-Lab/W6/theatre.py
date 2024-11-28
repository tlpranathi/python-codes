check = {}
while True:
    booking = input("enter name-movie-seatNo or exit: ")
    if booking != "exit":
        details = booking.split("-")
        if details[1] in check and check[details[1]] == details[2]:
            print("duplicate entry!!!", details)
        else:
            check[details[1]] = details[2]
    else:
        break

print(check)
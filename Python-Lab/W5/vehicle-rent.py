from datetime import datetime
# vehicles = [[(type, reg_no.), (name, ph_no.), (borrow_date, expected_return, rent, extra_rent, deposit, in_hand)], [vehicle 2]]
vh = [[("Car", 2478), ("Alice", 975318642), ("15/10/2024 10.30.15 AM", "18/10/2024 10.30.15 AM", 1000, 50, 1500, True)]]


choices = "1. Available Vehicles \n2. Check Rent \n3. Add Rent \n4.Calculate Rent"

while True:
    try:
        ch = int(input("Enter Choice or 0 to Exit: ").strip())
       
        if ch == 0:
            break
       
        elif ch == 1:
            available = False
            for i in range(len(vh)):
                if not vh[i][2][5]:
                    available = True
                    print(f"{i+1}. \nVehicle Type: {vh[i][0][0]} \nReg no.: {vh[i][0][1]}")
            if not available:
                print("No Available Vehicles")
       
        elif ch == 2:
            for i in range(len(vh)):
                    print(f"{i+1}. \nVehicle Type:", vh[i][0][0], "\nReg no.: ", vh[i][0][1], "\nRent: ", vh[i][2][2])

        elif ch == 3:
            num = int(input("Enter Reg no.: "))
            new_rent = int(input("Enter new rent: "))
            updated = False
            for i in range(len(vh)):
                if num == vh[i][0][1]:
                    updated = True
                    details = vh[i][2]
                    details_list = list(details)
                    details_list[2] = new_rent
                    vh[i][2] = tuple(details_list)
                    print("New rent updated successfully")
                    break
            if not updated:
                    print("Vehicle not found")

        elif ch == 4:
            for i in range(len(vh)):
                det = vh[i][2]
                start_date = det[0]
                end_date = det[1]
                rent_per_day = det[2]

                date1 = datetime.strptime(start_date, "%d/%m/%Y %I.%M.%S %p")
                date2 = datetime.strptime(end_date, "%d/%m/%Y %I.%M.%S %p")

                rental_duration = date2 - date1
                total_days = rental_duration.days
                total_seconds = rental_duration.total_seconds()
                extra_hours = (total_seconds % (24 * 3600)) / 3600


                rent_for_days = total_days*rent_per_day
                rent_for_extra_hours = extra_hours*50
                total_rent = rent_for_days + rent_for_extra_hours

                print(f"Rental Duration: {total_days} days and {extra_hours:.2f} hours")
                print(f"Total Rent: {total_rent:.2f}")

    except ValueError:
        print("Invalid input, try again.")
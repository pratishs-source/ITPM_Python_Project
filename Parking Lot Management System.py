parking_space = 5
parking_lot = []   # Stores vehicle number + type
bills = []          # Stores invoice details
count = 0

while True:
    print("\n------ PARKING LOT MANAGEMENT ------")
    print("1. Park a Vehicle")
    print("2. Remove a Vehicle")
    print("3. View Parked Vehicles")
    print("4. Check Available Slots")
    print("5. Show Parking Bills")
    print("6. Exit")

    choice = input("Enter your choice (1 to 6): ")

    #  Park a Vehicle
    if choice == '1':
        if count >= parking_space:
            print("Parking lot is full!")
        else:
            vehicle_no = input("Enter Vehicle Number: ")
            vehicle_type = input("Enter Vehicle Type (bike/car): ").lower()

            # Fee based on type
            if vehicle_type == "bike":
                fee = 50
            elif vehicle_type == "car":
                fee = 100
            else:
                print("Invalid vehicle type! Only 'bike' or 'car' allowed.")
                continue

            # Check duplicate
            duplicate = 0
            i = 0
            while i < count:
                if parking_lot[i][0] == vehicle_no:
                    duplicate = 1
                    break
                i += 1

            if duplicate == 1:
                print("Vehicle already parked!")
            else:
                print("Parking fee: ₹" + str(fee))
                pay = input("Pay ₹" + str(fee) + " to continue (yes/no): ").lower()

                if pay != "yes":
                    print("Payment not completed. Parking canceled.")
                    continue

                # Choose payment method
                print("\nSelect Payment Method:")
                print("1. Online Payment")
                print("2. Cash Payment")
                method_choice = input("Enter your choice (1 or 2): ")

                if method_choice == "1":
                    payment_method = "Online"
                    print("Please scan the QR code to complete your online payment.")
                elif method_choice == "2":
                    payment_method = "Cash"
                    print("Please submit cash at the payment counter.")
                else:
                    print("Invalid payment method! Transaction canceled.")
                    continue

                # Manual append for parking_lot
                new_list = [0] * (count + 1)
                i = 0
                while i < count:
                    new_list[i] = parking_lot[i]
                    i += 1
                new_list[count] = [vehicle_no, vehicle_type]
                parking_lot = new_list
                count += 1

                # Manual append for bills
                b_len = 0
                while b_len < 1000:
                    if b_len == len(bills):
                        break
                    b_len += 1

                new_bill_list = [0] * (b_len + 1)
                i = 0
                while i < b_len:
                    new_bill_list[i] = bills[i]
                    i += 1
                new_bill_list[b_len] = (
                    "Vehicle: " + vehicle_no +
                    " | Type: " + vehicle_type.capitalize() +
                    " | Fee: ₹" + str(fee) +
                    " | Payment: " + payment_method
                )
                bills = new_bill_list

                # Show invoice
                print("\n----- PARKING INVOICE -----")
                print("Vehicle Number:", vehicle_no)
                print("Vehicle Type:", vehicle_type.capitalize())
                print("Parking Fee: ₹" + str(fee))
                print("Payment Method:", payment_method)
                print("Status: Payment Received")
                print("---------------------------")
                print("Vehicle parked successfully!")
                print("Thank you for using our Parking Lot Service!")

    #  Remove a Vehicle
    elif choice == '2':
        if count == 0:
            print("Parking lot is empty!")
        else:
            vehicle_no = input("Enter Vehicle Number to Remove: ")
            found = -1
            i = 0
            while i < count:
                if parking_lot[i][0] == vehicle_no:
                    found = i
                    break
                i += 1

            if found == -1:
                print("Vehicle not found!")
            else:
                new_list = [0] * (count - 1)
                i = 0
                j = 0
                while i < count:
                    if i != found:
                        new_list[j] = parking_lot[i]
                        j += 1
                    i += 1
                parking_lot = new_list
                count -= 1

                print("\n----- EXIT INVOICE -----")
                print("Vehicle Number:", vehicle_no)
                print("Exit Successful — Have a nice day!")
                print("Thank you for visiting!")
                print("--------------------------")

    #  View Parked Vehicles
    elif choice == '3':
        if count == 0:
            print("No vehicles parked.")
        else:
            print("\n--- Parked Vehicles ---")
            i = 0
            while i < count:
                print(str(i + 1) + ". " + parking_lot[i][0] + " (" + parking_lot[i][1].capitalize() + ")")
                i += 1

    #  Check Available Slots
    elif choice == '4':
        slots_left = parking_space - count
        print("Available Slots:", slots_left)

    #  Show All Parking Bills
    elif choice == '5':
        if len(bills) == 0:
            print("No bills generated yet.")
        else:
            print("\n--- PARKING BILLS ---")
            i = 0
            while i < len(bills):
                print(str(i + 1) + ". " + bills[i] + " | Thank you!")
                i += 1

    #  Exit Program
    elif choice == '6':
        print("Exiting Parking Lot System. Thank you!")
        print("Have a wonderful day!")
        break

    # Invalid Choice
    else:
        print("Invalid choice! Try again.")

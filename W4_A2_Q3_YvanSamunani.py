
# Creating a car_collection to keep all the information regarding the Omondi's car collection
car_collection = []


# Car class handling all objects of Omondi's car collection
class Car:

    # init method helping to accept all the value passed to the variable that will be used in the car class
    def __init__(self, model, year_released, year_acquired, plate_number, times_rented, car_revenue):
        self.model = model
        self.year_released = year_released
        self.year_acquired = year_acquired
        self.plate_number = plate_number
        self.times_rented = times_rented
        self.car_revenue = car_revenue

    # add_car method handling the addition of cars to Omondi's collection
    def add_car(self):

        # Asking Omondi the number of cars he would like to add to his collection
        number_of_cars = int(input("How many cars would like to add in your collection: "))

        # Using "for loop" to get all the details about each car added in the car_collection list
        for i in range(number_of_cars):
            self.model = input("Please enter the model of the car: ")
            self.year_released = input("Enter when the car was released: ")
            self.year_acquired = input("When was the car acquired: ")
            self.plate_number = input("Car plate number: ")

            # Adding/appending the entered details to the car_collection list
            car_collection.append([self.model, self.year_released, self.year_acquired, self.plate_number,
                                   self.times_rented, self.car_revenue])
            print("\n")

    # display() function allowing Omondi to see all cars and their details in the car_collection list
    def display(self):

        # Printing the car_collection list
        print(car_collection)

    # rent_car() handling the car rental service
    def rent_car(self):

        # Asking Omondi the type of car he would like to rent out
        car_type = input("What model of the car would you like to rent: ")

        # Checking whether the type of car is in the collection and if yes, enters the rental cost of the car
        if car_type in str(car_collection):
            rental_cost = float(input("What is the rental cost (USD): "))
            self.car_revenue = rental_cost + self.car_revenue

            # Checking the index of the sublist where the car is located so that the program can insert the rent
            # revenue of the car
            for sub_list in car_collection:
                if car_type in sub_list:

                    # Getting the index of the sublist where the car is located
                    b = car_collection.index(sub_list)

                    # Inserting the car revenue to the sublist
                    car_collection[b].insert(5, rental_cost)

                    # Calculating the times the car is rented out and increments every time it is rented out
                    times_rented = +1

                    # inserting the times into the sublist of the car
                    car_collection[b].insert(4, times_rented)

        # If the car type is not among the car_collection list, Omondi is told it's not there.
        else:
            print("The car you entered does not belong to your collection!\n")

    # remove_car () function helping omondi to remove a certain car from his collection
    def remove_car(self):

        global new_car_collection

        # Asking Omondi which car to remove from his collection
        car_type = input("Enter the model of the car you would like to remove from your collection: ")

        # Removing the entered car from his collection using for loop to check the sublist the call is located in
        new_car_collection = [i for i in car_collection if i and (car_type not in i)]

        # printing the updated car_collection
        print("Here is your new collection: ", new_car_collection)

    # revenue() function accessing the revenues of the cars in car_collection
    def revenue(self):

        # Asking Omondi the car he wants to check the revenue for
        car_type = input("Which car model would you like to check its revenue: ")

        # Checking whether the type of car entered is in the car_collection
        if car_type in str(car_collection):

            # Using for loop to check the sublist of the car and access the index with revenue of the car
            for sub_list in car_collection:
                if car_type in sub_list:

                    # Accessing the car's index in the car_collection and print the revenue of the car
                    index = car_collection.index(sub_list)
                    print("USD ",car_collection[index][5])
                    print("\n")

        # If the car type is not among the car_collection list, Omondi is told it's not there.
        else:
            print("The car you entered does not belong to your collection!\n")

    # rental_times() function handling the process of accessing the times a certain car was rent out
    def rental_times(self):

        # Asking the type of car Omondi wants to check its rental times
        car_type = input("Which car model would you like to check the times rented out: ")

        # Checking whether the entered car type is in the car_collection
        if car_type in str(car_collection):

            # Using for loop to access the index of the car's sublist to view the number of times it was rent out
            for sub_list in car_collection:
                if car_type in sub_list:

                    # Getting the index of the sublist the car is located in and printing the number of times it was
                    # rent out
                    index = car_collection.index(sub_list)
                    print("The car was rent out ", car_collection[index][4], " times!")
                    print("\n")

        # If the car type is not among the car_collection list, Omondi is told it's not there.
        else:
            print("The car you entered does not belong to your collection!\n")


# main () function which is where the program starts and prints information that allows Omondi to interact with the
# program as well connects the program to the car class
def main():

    # Creating collection object to access car class and it's methods.
    collection = Car(0, 0, 0, 0, 0, 0)

    # Asking Omondi to choose what he would like the program to do for him
    print("Welcome to your car renting management system")
    print("Please select what you would like to do (1/2/3/4/5/6):")
    option = input("1) Add a new car \n2) View your collection \n3) Rent a car \n4) Remove a car from the collection "
                   "\n5) View times a car was rented out \n6) View revenue from each car\n: ")

    # Checking whether the entered option is valid
    if option == ['1', '2', '3', '4', '5', '6']:

        if option == '1':

            # Calling add_car() function for option = 1
            collection.add_car()

            # Asking Omondi would like to continue after adding cars to his collection
            choice = input("Would you like to continue back home [Y/N]: ")

            # If yes, the program calls main() function and the program restarts
            if choice == 'y' or choice == 'Y':
                main()

            # If not, the program ends
            else:
                print("Thank you for using the system!")

        if option == '2':

            # Calling display() function for option = 2
            collection.display()

            # Asking Omondi would like to continue after adding cars to his collection
            choice = input("Would you like to continue back home [Y/N]: ")

            # If yes, the program calls main() function and the program restarts
            if choice == 'y' or choice == 'Y':
                main()

            # If not, the program ends
            else:
                print("Thank you for using the system!")

        if option == '3':

            # Calling rent_car() function for option = 3
            collection.rent_car()

            # Asking Omondi would like to continue after adding cars to his collection
            choice = input("Would you like to continue back home [Y/N]: ")

            # If yes, the program calls main() function and the program restarts
            if choice == 'y' or choice == 'Y':
                main()

            # If not, the program ends
            else:
                print("Thank you for using the system!")

        if option == '4':

            # Calling remove_car() function for option = 4
            collection.remove_car()

            # Asking Omondi would like to continue after removing a car from his collection
            choice = input("Would you like to continue back home [Y/N]: ")

            # If yes, the program calls main() function and the program restarts
            if choice == 'y' or choice == 'Y':
                main()

            # If not, the program ends
            else:
                print("Thank you for using the system!")

        if option == '5':

            # Calling rental_times() function for option = 5
            collection.rental_times()

            # Asking Omondi would like to continue after checking the times a car was rent out
            choice = input("Would you like to continue back home [Y/N]: ")

            # If yes, the program calls main() function and the program restarts
            if choice == 'y' or choice == 'Y':
                main()

            # If not, the program ends
            else:
                print("Thank you for using the system!")

        if option == '6':

            # Calling revenue() function for option = 6
            collection.revenue()

            # Asking Omondi would like to continue after checking the revenue of car
            choice = input("Would you like to continue back home [Y/N]: ")

            # If yes, the program calls main() function and the program restarts
            if choice == 'y' or choice == 'Y':
                main()

            # If not, the program ends
            else:
                print("Thank you for using the system!")

    # Informing Omondi the inputted option is invalid and calls main() function to try again
    else:
        print("Invalid input, Try again!\n")
        main()

# Calling the main() function to start the program
main()

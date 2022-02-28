def cafe_menu():
    """
    The cafe_menu function is responsible for displaying:
    A Welcoming message 
    The menu of the resturant
    A clarification on how to exit
    
    Input:
                users_order: String

    Output:
    When the user enters an item, the program will return an acknowledgement of their input.
    """
    print(help(cafe_menu))

    menu_sections = ["appetizers","entrees", "desserts", "drinks"]

    appetizers = ["Wings", "Cookies", "Spring Rolls"]
    entrees = ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"]
    desserts = ["Ice cream", "Cake", "Pie"]
    drinks = ["Coffee", "Tea", "Unicorn Tears"]

    menu = list(map(lambda item:item.lower(),  appetizers + entrees + desserts + drinks))


    print(f"""
**********************
**  Welcome to the Snakes Cafe, Enjoy your meal!  **
**  Please choose your order from the menu below ;)  **
**
**  To quit at anytime, type "quit"  **
**********************
**Menu**
---------------
""")

    ordered_list = []
    for section in menu_sections:
        print()
        print(section.capitalize())
        print("------")
        for order in eval(section):
            print(order)

    print("""
What would you like to order? 
""")
    while True:
        user_input = input("> ").lower()

        if user_input in menu:
            ordered_list.append(user_input)
            print(f"{ordered_list.count(user_input)} order of {user_input} have been added to your meal")

        elif user_input == "quit":
            print("Your complete order is: " , "-".join(ordered_list))
            break          

        elif user_input == "":
            print("Kindly, enter your order!")

        else:
            ordered_list.append(user_input)
            print(f"Your order {user_input} is not in any of our menu sections but we will prepare it for you, {ordered_list.count(user_input)} order of {user_input} have been added to your meal")


if __name__ == "__main__":    
    cafe_menu()

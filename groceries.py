#### GROCERY LIST SCRIPT ######




groceries_list = []

while True:    ## Starts infinite input loop.

    ## This block is main menu and ask for "add, print or remove item".
    action = input('Do you want to add, print, or remove an item? ').lower()
    if action == "add": ## Add item block
        add2 = "yes"
        while add2 == "yes":
            item = input('What would you like to add? ')
            groceries_list.append(item)
            add2 = input('Add another? ').lower()
            if add2 != "yes" and add2 != "no":  ## Ensures user input is "yes" or "no".
                print('Please try again')


    elif action == "print":  ## Print item block.
        print("\nGrocery List: ")
        for index in range(len(groceries_list)):
            print(f'{index + 1}: {groceries_list[index].capitalize()}')
    elif action == "remove":  ## Remove item block.
        remove2 = "yes"
        while remove2 == "yes":
            remove1 = input('What would you like to remove? ')
            groceries_list.remove(remove1)
            remove2 = input('Remove another? ').lower()
            if remove2 != "yes" and remove2 != "no":
                print('Please try again')
    else: 
        print('Please try again')  ## Ensures user input is either "add", "print" or "remove".


        ## Things to do:
        ## Fix remove block so you can delete items that are duplicated.
        ## Allow list to mark duplicate items as multiples of same item (ex: "Milk X 2"). ".remove" will remove all
           ## instances of the listed item.
        ## Check item input for empty strings and re-prompt.
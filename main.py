# TODO: Import correct objects from woodshop folder

from plans.TablePlans import TablePlans as Table
from plans.ChairPlans import ChairPlans as Chair
from plans.BookshelfPlans import BookshelfPlans as Bookshelf

def main():

    # TODO: Instantiate/initialize objects necessary, namely:
    #       - Saw
    #       - WoodPile

    # TODO: Create Lumber, cut Lumber with Saw, add to WoodPile
    # Hint: Use a loop to get to total lumber that is needed
    # Hint: At each iteration of the loop:
    # - instantiate a Lumber object   
    # - cut lumber with saw (which method in Saw do you use?)
    # - add each cut lumber to the pile

    # TODO: Make plans
    # Hint: Instantiate each object from plans imported above,
    # passing cut pieces as an argument (parameter)
    # Print each object

if __name__ == "__main__":
    main()
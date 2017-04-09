"""List Assessment 

Edit the functions until all of the doctests pass when
you run this file.
"""


def all_odd(numbers):
    """Return a list of only the odd numbers in the input list.

    For example::

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []
    """

    odd_numbers = [] # New list for odd numbers within original list
    # Traverse list of numbers
    for number in numbers:
        # Check if number is odd
        if number % 2 != 0:
            # Add number to list
            odd_numbers.append(number)
    return odd_numbers # Return list of odd numbers



def print_indices(items):
    """Print index of each item in list, followed by item itself.

    Do this without using a "counting variable" --- that is, don't
    do something like this::

        count = 0
        for item in list:
            print count
            count = count + 1

    Output should look like this::

        >>> print_indices(["Toyota", "Jeep", "Volvo"])
        0 Toyota
        1 Jeep
        2 Volvo

        >>> print_indices(["Toyota", "Jeep", "Toyota", "Volvo"])
        0 Toyota
        1 Jeep
        2 Toyota
        3 Volvo
    
    """

    # Traverse list using index through range of numbers from 0
    # to the number before the length of items
    for index in range(len(items)):
        # prints the index with the item in the list
        print "{} {}".format(index, items[index])

def foods_in_common(foods1, foods2):
    """Find foods in common.

    Given 2 lists of foods, return the items that are in common
    between the two, sorted alphabetically.

    **NOTE**: for this problem, you're welcome to use any of the
    Python data structures you've been introduced to (not just
    lists). Is there another that would be a good idea?

    For example::

        >>> foods_in_common(
        ...     ["cheese", "bagel", "cake", "kale", "zebra cakes"],
        ...     ["hummus", "cheese", "beets", "kale", "lentils", "bagel", "cake" ]
        ... )
        ['bagel', 'cake', 'cheese', 'kale']

    The returned list should not have any duplicates::
        >>> foods_in_common(
        ...     ["cheese", "bagel", "cake", "cheese"],
        ...     ["hummus", "cheese", "beets", "kale", "bagel", "cake"]
        ... )
        ['bagel', 'cake', 'cheese']

    If there are no foods in common, return an empty list::

        >>> foods_in_common(
        ...     ["lamb", "chili", "cheese"],
        ...     ["cake", "ice cream"]
        ... )
        []

    """

    # List for common foods - list needs to be mutable and ordered
    common_foods = []

    # Loops through each item in the first list of food
    for first_food in foods1:
        # Loops through each item in the second list of food
        for second_food in foods2:
            # Compares every food in the first food list to
            # every food in the second food list
            if first_food == second_food:
                # Ensures the food doesn't already exist in the
                # list of common foods and adds it to the list
                if first_food not in common_foods:
                    common_foods.append(first_food)
    # Sorts the common foods list in place
    common_foods.sort()
    return common_foods # Return sorted common foods list


def every_other_item(items):
    """Return every other item in `items`, starting at first item.

    For example::

       >>> every_other_item([1, 2, 3, 4, 5, 6])
       [1, 3, 5]

       >>> every_other_item(["pickle", "pickle", "juice", "pickle", "juice", "pop"])
       ['pickle', 'juice', 'juice']

       >>> every_other_item(
       ...   ["you", "z", "are", "z", "good", "z", "at", "x", "code"]
       ... )
       ['you', 'are', 'good', 'at', 'code']
    """

    # List comprehension that adds items of index of every other item
    every_other_item_list = [items[index] for index in range(0, len(items), 2)]

    return every_other_item_list # Returns list of every other item


def largest_n_items(items, n):
    """Return the `n` largest integers in list, in ascending order.

    You can assume that `n` will be less than the length of the list.

    For example::

        >>> largest_n_items([2, 6006, 700, 42, 6, 59], 3)
        [59, 700, 6006]

    It should work when `n` is 0::

        >>> largest_n_items([3, 4, 5], 0)
        []

    If there are duplicates in the list, they should be counted
    separately::

        >>> largest_n_items([3, 3, 3, 2, 1], 2)
        [3, 3]
    """

    # New list of sorted items from the list items
    largest_items = sorted(items)
    items_len = len(items) # Variable for length of list
    
    # Splices list to only include last n items
    largest_items = largest_items[(items_len - n): items_len]
   
    return largest_items # Returns spliced list


#####################################################################
# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print("\nALL TESTS PASSED. GOOD WORK!\n")

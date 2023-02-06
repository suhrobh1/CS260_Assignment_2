# Name: Suhrob Hasanov
# OSU Email: hasanovs@oregon
# Course: CS261 - Data Structures
# Assignment: Assignment 2
# Due Date: 2/6/23
# Description: Bag ADT implementation. 


from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da.get_at_index(_))
                          for _ in range(self._da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.length()

    # -----------------------------------------------------------------------

    def add(self, value: object) -> None:
        """
        Adds item to the bag.
        """
        self._da.append(value)

    def remove(self, value: object) -> bool:
        """
        Removes item from the bag.
        """
        for i in range(0, self._da.length()):
            # Comparing to find the correct item for removal
            if (self._da.get_at_index(i) == value):
                self._da.remove_at_index(i)
                return True
        return False
       

    def count(self, value: object) -> int:
        """
        Counts the number of occurances of the passed item in the bag.
        """
        # Counter for tracking the occurances of the elem in the array
        counter = 0
        for i in range(0, self._da.length()):
            if (self._da.get_at_index(i) == value):
                # If we have a match, increment the counter
                counter += 1
        return counter


    def clear(self) -> None:
        """
        Clears the contents of the bag.
        """
        for i in range(0, self._da.length()):
            self._da.remove_at_index(0)

    def equal(self, second_bag: "Bag") -> bool:
        """
        Checks whether the two bags are equal to each other.
        """
        # If length are different, then bags are different
        if (self._da.length() != second_bag._da.length()):
            return False
            
        for i in range(0, self._da.length()):
            # If the counts of the elems at index are not equal, bags are different
            if(self.count(self._da.get_at_index(i)) != second_bag.count(self._da.get_at_index(i))):
                return False
        return True

        # index = 0
        # for i in self._da:
        #     isFound = None
        #     index2 = 0
        #     for j in second_bag._da:
                
        #         if isFound:
        #             break
                
        #         if(index2 == second_bag._da.length() -1  and isFound == False):
        #             return False

        #         if(i == j):
        #             isFound = True
        #             if(self.count(self._da.get_at_index(index)) !=second_bag.count(second_bag._da.get_at_index(index2))):
        #                 # print("Count A", self.count(self._da.get_at_index(index)) )
        #                 # print("Count A", second_bag.count(second_bag._da.get_at_index(index2)) )
        #                 # print("i", i)
        #                 # print("j", j)
        #                 return False

        #         else:

        #             pass
        #         index2 += 1
            
        #     index += 1
        # return True



    def __iter__(self):
        """
        Tracks the index for the iteration of the bag
        """
        # Tracking the index of the next item for iteration
        self._index = 0
        return self
    def __next__(self):
        """
        Keeps track of the value at given index and incements the index for iteration. 
        """
        # print("self._da", self._da)
        try:
            value = self._da.get_at_index(self._index)
        except DynamicArrayException:
            raise StopIteration
        self._index = self._index + 1
        return value


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    # print("\n# add example 1")
    # bag = Bag()
    # print(bag)
    # values = [10, 20, 30, 10, 20, 30]
    # for value in values:
    #     bag.add(value)
    # print(bag)

    # print("\n# remove example 1")
    # bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    # print(bag)
    # print(bag.remove(7), bag)
    # print(bag.remove(3), bag)
    # print(bag.remove(3), bag)
    # print(bag.remove(3), bag)
    # print(bag.remove(3), bag)

    # print("\n# count example 1")
    # bag = Bag([1, 2, 3, 1, 2, 2])
    # print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))

    # print("\n# clear example 1")
    # bag = Bag([1, 2, 3, 1, 2, 3])
    # print(bag)
    # bag.clear()
    # print(bag)

    # print("\n# equal example 1")
    # bag1 = Bag([10, 20, 30, 40, 50, 60])
    # bag2 = Bag([60, 50, 40, 30, 20, 10])
    # bag3 = Bag([10, 20, 30, 40, 50])
    # bag_empty = Bag()

    # print(bag1, bag2, bag3, bag_empty, sep="\n")
    # print(bag1.equal(bag2), bag2.equal(bag1))
    # print(bag1.equal(bag3), bag3.equal(bag1))
    # print(bag2.equal(bag3), bag3.equal(bag2))
    # print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    # print(bag_empty.equal(bag_empty))
    # print(bag1, bag2, bag3, bag_empty, sep="\n")

    # bag1 = Bag([100, 200, 300, 200])
    # bag2 = Bag([100, 200, 30, 100])
    # print(bag1.equal(bag2))


    print("BAG EQUAL SPECIAL CASE")
    bagA = Bag([1, 2, 2])
    bagB = Bag([2, 1, 2])
    print(bagA.equal(bagB))

    print("BAG EQUAL SPECIAL CASE 2")
    bagC = Bag([1265, 63061, -60474, -43787, -12265])
    bagD = Bag([-60474, -43787, 63061, -26449, 1265])
    print(bagC.equal(bagD))

    
    print("\n# __iter__(), __next__() example 1")
    bag = Bag([5, 4, -8, 7, 10])
    print(bag)
    for item in bag:
        print(item)

    print("\n# __iter__(), __next__() example 2")
    bag = Bag(["orange", "apple", "pizza", "ice cream"])
    print(bag)
    for item in bag:
        print(item)

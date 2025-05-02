def bubble_sort(our_list):
    # Goes through the list and compares each element with the next one
    for i in range(len(our_list)):
        # The last pair of adjacent elements should be (n-2, n-1)
        for j in range(len(our_list) - 1):
            if our_list[j] > our_list[j+1]:
                # Swap
                our_list[j], our_list[j+1] = our_list[j+1], our_list[j]  

our_list = [5, 2, 9, 1, 5, 6]
bubble_sort(our_list)
print(our_list)  # Output: [1, 2, 5, 5, 6, 9]
# Time complexity: O(n^2) in the worst case
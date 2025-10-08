"""
Problem 1: List Operations and Comprehensions
Practice working with Python lists - creating, modifying, filtering, and transforming them.
"""

def create_number_list(start, end):

    if type(start)!=int or type(end)!=int:
        raise TypeError("Arguments need to be integers")
    if start>end:
        raise ValueError("Start need to be < than end")    
    L=[]
    for i in range(start,end+1):
        L.append(i)
    return L


def filter_even_numbers(numbers):
    "Return a new list containing only the even numbers."
    return [e for e in numbers if e%2==0]

def square_numbers(numbers):
    "Return a new list with each number squared."
    return [e**2 for e in numbers]


def find_max_min(numbers):
    """
    Find the maximum and minimum values in a list"
    Returns:
        tuple:(max_value, min_value)
    """
    return (max(numbers),min(numbers))


def remove_duplicates(items):
    """
    Remove duplicate items from a list while preserving order.
    """
    L=[]
    seen = set()
    for e in items:
        if e not in seen:
            seen.add(e)
            L.append(e)
    return L


def merge_lists(list1, list2):
    """
    Merge two lists, alternating elements from each.
    Example:
        >>> merge_lists([1, 3, 5], [2, 4, 6])
        [1, 2, 3, 4, 5, 6]
        >>> merge_lists([1, 2], [10, 20, 30, 40])
        [1, 10, 2, 20, 30, 40]
    """
    L = []
    if len(list1)<=len(list2):
        small,large=list1,list2
    else:
        small,large=list2,list1

    for i in range(len(small)):
        L.append(small[i])
        L.append(large[i])

    L.extend(large[len(small):])
    
    return L


def list_statistics(numbers):
    """
    Example:
        >>> list_statistics([1, 2, 3, 4, 5])
        {'sum': 15, 'average': 3.0, 'count': 5, 'max': 5, 'min': 1}
    """
    if not numbers:
        return None

    stats={}
    stats['sum']=sum(numbers)
    stats['average']=sum(numbers)/len(numbers)
    stats['count']=len(numbers)
    stats['max']=max(numbers)
    stats['min']=min(numbers)
    return stats


def chunk_list(items, chunk_size):
    """
    Split a list into chunks of specified size.
    Example:
        >>> chunk_list([1, 2, 3, 4, 5, 6, 7], 3)
        [[1, 2, 3], [4, 5, 6], [7]]
    """
    L=[items[i:i+chunk_size] for i in range(0,len(items),chunk_size)]
    return L


# Test cases
if __name__ == "__main__":
    print("Testing List Operations...")
    print("-" * 50)

    # Test create_number_list
    print("Test 1: create_number_list(1, 5)")
    result = create_number_list(1, 5)
    print(f"Result: {result}")
    assert result == [1, 2, 3, 4, 5], "Failed!"
    print("✓ Passed\n")

    # Test filter_even_numbers
    print("Test 2: filter_even_numbers([1, 2, 3, 4, 5, 6])")
    result = filter_even_numbers([1, 2, 3, 4, 5, 6])
    print(f"Result: {result}")
    assert result == [2, 4, 6], "Failed!"
    print("✓ Passed\n")

    # Test square_numbers
    print("Test 3: square_numbers([1, 2, 3, 4])")
    result = square_numbers([1, 2, 3, 4])
    print(f"Result: {result}")
    assert result == [1, 4, 9, 16], "Failed!"
    print("✓ Passed\n")

    # Test find_max_min
    print("Test 4: find_max_min([3, 1, 4, 1, 5, 9, 2, 6])")
    result = find_max_min([3, 1, 4, 1, 5, 9, 2, 6])
    print(f"Result: {result}")
    assert result == (9, 1), "Failed!"
    print("✓ Passed\n")

    # Test remove_duplicates
    print("Test 5: remove_duplicates([1, 2, 2, 3, 4, 3, 5])")
    result = remove_duplicates([1, 2, 2, 3, 4, 3, 5])
    print(f"Result: {result}")
    assert result == [1, 2, 3, 4, 5], "Failed!"
    print("✓ Passed\n")

    # Test merge_lists
    print("Test 6: merge_lists([1, 3, 5], [2, 4, 6])")
    result = merge_lists([1, 3, 5], [2, 4, 6])
    print(f"Result: {result}")
    assert result == [1, 2, 3, 4, 5, 6], "Failed!"
    print("✓ Passed\n")

    # Test list_statistics
    print("Test 7: list_statistics([1, 2, 3, 4, 5])")
    result = list_statistics([1, 2, 3, 4, 5])
    print(f"Result: {result}")
    expected = {'sum': 15, 'average': 3.0, 'count': 5, 'max': 5, 'min': 1}
    assert result == expected, "Failed!"
    print("✓ Passed\n")

    # Test chunk_list
    print("Test 8: chunk_list([1, 2, 3, 4, 5, 6, 7], 3)")
    result = chunk_list([1, 2, 3, 4, 5, 6, 7], 3)
    print(f"Result: {result}")
    assert result == [[1, 2, 3], [4, 5, 6], [7]], "Failed!"
    print("✓ Passed\n")

    print("=" * 50)
    print("All tests passed! Great work!")

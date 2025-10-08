"""
Problem 2: Dictionary Operations and Nested Structures
Practice working with Python dictionaries - creating, accessing, modifying, and nesting them.
"""


def create_student_record(name, age, major, gpa):
    """
    Create a student record as a dictionary.
    Example:
        >>> create_student_record("Alice", 20, "Computer Science", 3.8)
        {'name': 'Alice', 'age': 20, 'major': 'Computer Science', 'gpa': 3.8}
    """
    record={
        'name':name,
        'age':age,
        'major':major,
        'gpa':gpa
    }
    return record


def get_value_safely(dictionary, key, default=None):
    """
    Get a value from a dictionary safely, returning default if key doesn't exist.
    Example:
        >>> d = {'a': 1, 'b': 2}
        >>> get_value_safely(d, 'a')
        1
        >>> get_value_safely(d, 'c', 'Not found')
        'Not found'
    """
    try:
        return dictionary[key]
    except KeyError:
        return default

def merge_dictionaries(dict1, dict2):
    """
    Merge two dictionaries. If keys conflict, dict2's values take precedence.
    Example:
        >>> merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
        {'a': 1, 'b': 3, 'c': 4}
    """
    d={}
    for key,value in dict1.items():
        d[key]=value
    for key,value in dict2.items():
        d[key]=value
    return d

import string
def count_word_frequency(text):
    """
    Count the frequency of each word in a text string.
    Convert to lowercase and ignore punctuation.
    """
    freq={}
    text=text.lower()
    for p in string.punctuation:
        text=text.replace(p,"")
    words=text.split()
    for w in words:
        freq[w]=freq.get(w,0)+1
    return freq


def invert_dictionary(dictionary):
    """
    Invert a dictionary (swap keys and values).
    Assume all values are unique.
    Example:
        >>> invert_dictionary({'a': 1, 'b': 2, 'c': 3})
        {1: 'a', 2: 'b', 3: 'c'}
    """
    d={}
    for key,value in dictionary.items():
        d[value]=key
    return d


def filter_dictionary(dictionary, keys_to_keep):
    """
    Create a new dictionary with only the specified keys.
    Example:
        >>> filter_dictionary({'a': 1, 'b': 2, 'c': 3, 'd': 4}, ['a', 'c'])
        {'a': 1, 'c': 3}
    """
    d={}
    for key,value in dictionary.items():
        if key in keys_to_keep:
            d[key]=value
    return d


def group_by_first_letter(words):
    """
    Group words by their first letter.
    Example:
        >>> group_by_first_letter(['apple', 'banana', 'apricot', 'blueberry'])
        {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry']}
    """
    d={}
    for word in words:
        word=word.lower()
        if word[0] not in d:
            d[word[0]]= [word]
        else:
            d[word[0]].append(word)
    return d


def calculate_grades_average(students):
    """
    Calculate the average grade for each student.
    Example:
        >>> calculate_grades_average({
        ...     'Alice': [90, 85, 88],
        ...     'Bob': [75, 80, 78]
        ... })
        {'Alice': 87.67, 'Bob': 77.67}
    """
    grades={}
    for key,value in students.items():
        grades[key]=round(sum(value)/len(value),2)
    return grades

def nested_dict_access(data, keys):
    """
    Access a nested dictionary using a list of keys.
    Return None if any key doesn't exist.
    Example:
        >>> data = {'a': {'b': {'c': 123}}}
        >>> nested_dict_access(data, ['a', 'b', 'c'])
        123
        >>> nested_dict_access(data, ['a', 'x'])
        None
    """
    d=data
    for key in keys:
        if key in d:
            d=d[key]
        else:
            return None
    return d

# Test cases
if __name__ == "__main__":
    print("Testing Dictionary Operations...")
    print("-" * 50)

    # Test create_student_record
    print("Test 1: create_student_record")
    result = create_student_record("Alice", 20, "CS", 3.8)
    print(f"Result: {result}")
    assert result == {'name': 'Alice', 'age': 20, 'major': 'CS', 'gpa': 3.8}
    print("✓ Passed\n")

    # Test get_value_safely
    print("Test 2: get_value_safely")
    d = {'a': 1, 'b': 2}
    assert get_value_safely(d, 'a') == 1
    assert get_value_safely(d, 'c', 'Not found') == 'Not found'
    print("✓ Passed\n")

    # Test merge_dictionaries
    print("Test 3: merge_dictionaries")
    result = merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
    print(f"Result: {result}")
    assert result == {'a': 1, 'b': 3, 'c': 4}
    print("✓ Passed\n")

    # Test count_word_frequency
    print("Test 4: count_word_frequency")
    result = count_word_frequency("hello world hello")
    print(f"Result: {result}")
    assert result == {'hello': 2, 'world': 1}
    print("✓ Passed\n")

    # Test invert_dictionary
    print("Test 5: invert_dictionary")
    result = invert_dictionary({'a': 1, 'b': 2, 'c': 3})
    print(f"Result: {result}")
    assert result == {1: 'a', 2: 'b', 3: 'c'}
    print("✓ Passed\n")

    # Test filter_dictionary
    print("Test 6: filter_dictionary")
    result = filter_dictionary({'a': 1, 'b': 2, 'c': 3, 'd': 4}, ['a', 'c'])
    print(f"Result: {result}")
    assert result == {'a': 1, 'c': 3}
    print("✓ Passed\n")

    # Test group_by_first_letter
    print("Test 7: group_by_first_letter")
    result = group_by_first_letter(['apple', 'banana', 'apricot', 'blueberry'])
    print(f"Result: {result}")
    assert result == {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry']}
    print("✓ Passed\n")

    # Test calculate_grades_average
    print("Test 8: calculate_grades_average")
    result = calculate_grades_average({
        'Alice': [90, 85, 88],
        'Bob': [75, 80, 78]
    })
    print(f"Result: {result}")
    assert result == {'Alice': 87.67, 'Bob': 77.67}
    print("✓ Passed\n")

    # Test nested_dict_access
    print("Test 9: nested_dict_access")
    data = {'a': {'b': {'c': 123}}}
    assert nested_dict_access(data, ['a', 'b', 'c']) == 123
    assert nested_dict_access(data, ['a', 'x']) is None
    print("✓ Passed\n")

    print("=" * 50)
    print("All tests passed! Excellent work!")

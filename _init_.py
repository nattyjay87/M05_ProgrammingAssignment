def custom_sum(iterable):
    try:
        result = sum(iterable)
        return result
    except TypeError:
        print("Unsupported data type in the iterable. Please provide a valid iterable containing numerical values.")

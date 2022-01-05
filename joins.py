def inner_join(left, right, condition, fields_filter):
    results = set()
    for left_row in left:
        for right_row in right:
            if condition(left_row, right_row):
                results.add(fields_filter(left_row, right_row))
    return results


def left_join(left, right, condition, fields_filter):
    results = set()
    for left_row in left:
        matches = set()
        for right_row in right:
            if condition(left_row, right_row):
                matches.add(fields_filter(left_row, right_row))
        if matches:
            results.update(matches)
        else:
            results.add(fields_filter(left_row, None))
    return results


def right_join(left, right, condition, fields_filter):
    results = set()
    for right_row in right:
        matches = set()
        for left_row in left:
            if condition(left_row, right_row):
                matches.add(fields_filter(left_row, right_row))
        if matches:
            results.update(matches)
        else:
            results.add(fields_filter(None, right_row))
    return results


def full_join(left, right, condition, fields_filter):
    results = left_join(left, right, condition, fields_filter)
    results.update(right_join(left, right, condition, fields_filter))
    return results

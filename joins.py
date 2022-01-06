def inner_join(left, right, condition, fields_filter):
    results = []
    for left_row in left:
        for right_row in right:
            if condition(left_row, right_row):
                results.append(fields_filter(left_row, right_row))
    return results


def left_join(left, right, condition, fields_filter):
    results = []
    for left_row in left:
        matches = []
        for right_row in right:
            if condition(left_row, right_row):
                matches.append(fields_filter(left_row, right_row))
        if matches:
            results.extend(matches)
        else:
            results.append(fields_filter(left_row, None))
    return results


def right_join(left, right, condition, fields_filter):
    results = []
    for right_row in right:
        matches = []
        for left_row in left:
            if condition(left_row, right_row):
                matches.append(fields_filter(left_row, right_row))
        if matches:
            results.extend(matches)
        else:
            results.append(fields_filter(None, right_row))
    return results


def full_join(left, right, condition, fields_filter):
    results = []
    indexes_of_used_pairs_of_rows = set()
    for right_row_index, right_row in enumerate(right):
        matches = []
        for left_row_index, left_row in enumerate(left):
            if condition(left_row, right_row):
                matches.append(fields_filter(left_row, right_row))
                indexes_of_used_pairs_of_rows.add(
                    (left_row_index, right_row_index)
                )
        if matches:
            results.extend(matches)
        else:
            results.append(fields_filter(None, right_row))
            indexes_of_used_pairs_of_rows.add((None, right_row_index))
    for left_row_index, left_row in enumerate(left):
        matches = []
        at_least_one_row_was_matched = False
        for right_row_index, right_row in enumerate(right):
            if condition(left_row, right_row):
                at_least_one_row_was_matched = True
                if (
                    (left_row_index, right_row_index)
                    not in indexes_of_used_pairs_of_rows
                ):
                    matches.append(fields_filter(left_row, right_row))
        if at_least_one_row_was_matched:
            results.extend(matches)
        else:
            results.append(fields_filter(left_row, None))
    return results

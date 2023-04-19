# class Rule:
#     def __init__(self, ranges, max_size):
#         self.t = []
#         for range in ranges:
#             self.t[range.txt] = self.t[range.txt] or {}
#             self.t[range.txt].append({"lo": range.lo, "hi": range.hi, "at": range.at})
#         self.prune(self.t, max_size)
#
#     def prune(self, rule, max_size):
#         n = 0
#         for txt, ranges in enumerate(rule):
#             n += 1
#             if len(ranges) == max_size[txt]:
#                 n += 1
#                 rule[txt] = None
#         if n > 0:
#             return rule


def RULE(ranges, max_size):
    t = {}
    for range in ranges:
        t[range.txt] = t[range.txt] if range.txt in t else []
        t[range.txt].append({"lo": range.lo, "hi": range.hi, "at": range.at})
    return prune(t, max_size)


"""
# Group by value range - urvashi
# Instead of simply grouping the ranges by their column id,
you can also group them by their value range.
# Specifically, you can create a group for each unique range of values
that appears in a given column.
#  This can be useful for identifying patterns in the data that are not
apparent from the column id alone.
#
# Here, we first create a key for each range by concatenating its
lower and upper bounds with a hyphen.
# We then group the ranges by their column and their range key. Finally,
# we return the pruned rule using the prune function as before.
#
# With this variation, you can identify which ranges of values are most
common in each column
# of your data. For example, you might find that a certain column tends
to have a large number
# of low values or a narrow range of values. This can help you to better
 understand the distribution
# of your data and to identify any potential issues or opportunities
for improvement.

def RULE(ranges, max_size):
    # In this variation, we first create a key for each range by concatenating
    # its lower and upper bounds with a hyphen.
    # We then group the ranges by their column and their range key.
    # Finally, we return the pruned rule using the prune function as before.
    t = {}
    for r in ranges:
        col = r.at
        key = str(r.lo) + "-" + str(r.hi)
        t[col] = t.get(col, {})
        t[col][key] = t[col].get(key, [])
        t[col][key].append(r)
    return prune(t, max_size)
"""


# Group by attribute - parth
# The group_by_attribute function takes two arguments:
#
# ranges: A list of Range objects that we want to group by their at attribute.
# max_size: A dictionary that specifies the maximum size that
# each group should have for each txt value.
# The function creates an empty dictionary called groups to
# hold the groups of ranges. It then iterates over each
# Range object in the ranges list. For each object, the function
# checks if it has already seen an object with the same at value.
# If it has, it appends the current Range object to the list of ranges
# for that at value in the groups dictionary. If it hasn't,
# it creates a new list for that at value in the groups dictionary,
# and appends the current Range object to that list.
#
# After iterating over all the Range objects, the
# function iterates over each key in the groups dictionary,
# which corresponds to a unique at value. It gets the length
# of the list associated with this key, and checks if it exceeds
# the max_size value specified in the max_size dictionary for
# the corresponding txt value. If it does, the function calls
# the prune function on the list of ranges for that at value.
# The prune function removes elements from the list until it
# has no more than max_size elements.
#
# Finally, the function returns the groups dictionary,
# which now contains a list of ranges for each unique at value,
# where each list has no more
'''
def RULE(ranges, max_size):
    """
    Groups a list of Range objects by their 'at' attribute,
    and returns a dictionary of lists of ranges.
    """
    # Create an empty dictionary to hold the groups of ranges.
    groups = {}

    # Iterate over each Range object in the list.
    for range_obj in ranges:
        # If this is the first time we've seen this attribute value,
        create a new list for it in the dictionary.
        if range_obj.at not in groups:
            groups[range_obj.at] = []
        # Add the current range object to the list for this attribute value.
        groups[range_obj.at].
        append({"txt": range_obj.txt, "lo": range_obj.lo, "hi": range_obj.hi})

    # Prune the groups to ensure that each one has no more than max_size elements.
    for group_key in groups.keys():
        group_size = len(groups[group_key])
        if group_size > max_size[group_key]:
            groups[group_key] = prune(groups[group_key], max_size)

    # Return the dictionary of groups.
    return groups
'''


def prune(rule, max_size):
    n = 0
    for txt, ranges in rule.items():
        n += 1
        if len(ranges) == max_size[txt]:
            n += 1
            rule[txt] = None
    if n > 0:
        return rule

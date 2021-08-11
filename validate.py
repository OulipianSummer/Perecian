import re

def validate_project_name(name):
    """Validate the project name argument"""
    if len(name) >= 150:
        raise SystemExit('Error: The provided project name, "{}", is greater than 150 characters. Please shorten it to continue'.format(name))


def validate_order(order):
    """Validate the project order argument"""
    if not order.isnumeric():
        raise SystemExit('Error: The provided order, "{}", is not a number. Please enter a numeric value to continue'.format(order))


def validate_start(start):
    """Validate the start argument"""
    if len(start) > 5:
        raise SystemExit('Error The provided tour starting coordinates, "{}", are longer than 5 characters. Please shorten it to continue'.format(start))
    
    search = re.search(r'\d{1,2},\d{1,2}|[a-z]\d{1,2}', start)
    
    try:
        search = search.group()
    except AttributeError:
        raise SystemExit('Error: The provided tour starting coordinates, "{}", are not formatted correctly. Please enter either two integers seperated by a comma, or a chess square in algebraic chess notation\n\tExamples: 1,10 or a10'.format(start))

    if search != start:
        raise SystemExit('Error: The provided tour starting coordinates, "{}", are not formatted correctly. Please enter either two integers seperated by a comma, or a chess square in algebraic chess notation\n\tExamples: 1,10 or a10'.format(start))

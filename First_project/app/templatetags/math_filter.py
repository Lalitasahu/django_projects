from django import template
import ast

register = template.Library()


# @register.filter
# def multiply(value, arg):
#     import re
#     try:
#         # Remove currency symbols, commas, and spaces
#         clean_value = re.sub(r'[^\d.]', '', str(value))
#         clean_arg = re.sub(r'[^\d.]', '', str(arg))
#         return float(clean_value) * float(clean_arg)
#     except (ValueError, TypeError):
#         return ''

@register.filter
def multiply(value, arg):
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0 
 

@register.filter(name='string_to_list')
# @register.filter
def stringToList(value,args):
    try:
        return ast.literal_eval(value)
    except (ValueError, TypeError):
        return ""



# @register.filter
# def getOneImage(value,args):
#     try:
#         return ast.literal_eval(value)[0]
#     except (ValueError, TypeError):
#         return ""


# @register.filter(name='first_image')
# def first_image(value, delimiter=","):
#     images = value.split(delimiter)
#     return images[0] if images else None



@register.filter(name='first_image')
def first_image(value, delimiter=","):
    if not value:
        return None

    # If the value is a string representation of a list, convert it
    if isinstance(value, str) and value.startswith("[") and value.endswith("]"):
        import ast
        value = ast.literal_eval(value)

    # If it's a list, return the first item
    if isinstance(value, list):
        return value[0].strip() if value else None

    # If it's a string, split it
    images = value.split(delimiter)
    return images[0].strip() if images else None

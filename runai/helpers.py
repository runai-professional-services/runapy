def snake_to_camel(snake_str):
    components = snake_str.split('_')
    # Capitalize the first letter of each component except the first one
    return components[0] + ''.join(x.title() for x in components[1:])

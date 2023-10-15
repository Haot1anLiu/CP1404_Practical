COLOUR_TO_HEX = {
    "gray10": "#1a1a1a", "gray11": "#1c1c1c", "gray12": "#1f1f1f",
    "gray13": "#212121", "gray14": "#242424", "gray15": "#262626",
    "gray16": "#292929", "gray17": "#2b2b2b", "gray18": "#2e2e2e",
    "gray19": "#303030"
}

colour_name = input("Enter colour name (or press enter to exit): ").lower()
while colour_name:
    hex_value = COLOUR_TO_HEX.get(colour_name)
    if hex_value:
        print(f"{colour_name} is {hex_value}")
    else:
        print("Invalid colour.")
    colour_name = input("Enter colour name (or press enter to exit): ").lower()

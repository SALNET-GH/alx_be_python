weather = input("What's the weather like today? (sunny/rainy/cold): ")
match weather:
    case str("sunny"):
        print("Wear a t-shirt and sunglasses.")
    case str("rainy"):
        print("Don't forget your umbrella and a raincoat.")
    case str("cold"):
        print("Make sure to wear a warm coat and a scarf.")
    case _:
        print("Sorry, I don't have recommendations for this weather.")

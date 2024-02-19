try:
    # Open and read the contents of the cats.txt file
    with open("cats", "r") as cats_file:
        print("Contents of cats.txt:")
        print(cats_file.read())

    # Open and read the contents of the dogs.txt file
    with open("dogs", "r") as dogs_file:
        print("\nContents of dogs.txt:")
        print(dogs_file.read())

except FileNotFoundError:
    # Fail silently if either file is missing
    pass
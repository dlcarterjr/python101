width = int(input("Width? "))
height = int(input("Height? "))

# builds and prints top of box.
star_count = 1
star = ""
while star_count <= width:
        star = star + ("*")
        star_count += 1
print(star)

middle_rows = 2
while middle_rows < height:

        # builds and prints one row of the middle lines with stars on each end.
        side_stars = ""
        char_count = 1

        while char_count <= width:
                if char_count == width - (width - 1):
                        side_stars = "*"
                elif char_count == width:
                        side_stars = side_stars + "*"
                else:
                        side_stars = side_stars + " "
                char_count += 1
        print(side_stars)
        middle_rows += 1
print(star)

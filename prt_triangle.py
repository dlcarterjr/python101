count = 1
levels = 4
stars = ""
while count <= levels:
    if count == 1:
        space_count = 1
        while space_count <= levels - count:
            stars = stars + " "
            space_count += 1
        stars = stars + "*"
        print(stars)
        stars = ""

  
    stars = stars + "**"
    print(stars)
    count += 1

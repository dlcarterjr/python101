num = int(input("How big is the square? " ))
count = 1
while count <= num:
    star = ""
    star_count = 1
    while star_count <= num:
        star = star + ("*")
        star_count += 1
    print(star)
    count += 1

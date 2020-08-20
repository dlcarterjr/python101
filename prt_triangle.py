levels = 4
row_count = 1
star_count = 0
last_stars = levels + (levels - 1)
while row_count <= levels:
    
    while star_count <= last_stars:#prints stars after spaces on row.
        space_count = 1
        row = ""
        while space_count <= levels - 1:#prints spaces before stars for one row.
            row = row + "_"
            space_count += 1
        row = row + "*"
        star_count += 2
    print(row)
    row_count += 1

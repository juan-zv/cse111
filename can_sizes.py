import math

def main ():
    my_list = [
    ["#1 Picnic", 6.83, 10.16], 
    ["#1 Tall", 7.78, 11.91], 
    ["#2", 8.73, 11.59], 
    ["#2.5", 10.32, 11.91], 
    ["#3 Cylinder", 10.79, 17.78], 
    ["#5", 13.02, 14.29], 
    ["#6Z", 5.40, 8.89],
    ["#8Z short", 6.83, 7.62], 
    ["#10", 15.72, 17.78], 
    ["#211", 6.83, 12.38], 
    ["#300", 7.62, 11.27], 
    ["#303", 8.10, 11.11]
    ]

    # for name, radius, height in list1:
    #     v = compute_volumes(radius, height)
    #     s = compute_surface_area(radius, height)

    #     print(f"{name}  {v}  {s}")

    for i in my_list:
        i = int(i + 1)
        list_name = my_list[i][i]
        list_radius = my_list[i][i + 1]
        list_height = my_list[i][i + 2]

        print(f"{list_name}  {list_radius}  {list_height}")







def compute_volumes(radius, height):
    volume = math.pi * radius ** 2 * height
    return volume

def compute_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

main()
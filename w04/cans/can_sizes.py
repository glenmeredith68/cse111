import math 

def main():
    can_sizes = [
        ["#1 Picnic", 6.83, 10.16, 0.28],
        ["#1 Tall", 7.78, 11.91, 0.43],
        ["#2", 8.73, 11.59, 0.45],
        ["#2.5", 10.32, 11.91, 0.61],
        ["#3 Cylinder", 10.79, 17.78, 0.86],
        ["#5", 13.02, 14.29, 0.83],
        ["#6Z", 5.4, 8.89, 0.22],
        ["#8Z short", 6.83, 7.62, 0.26],
        ["#10", 15.72, 17.78, 1.53],
        ["#211", 6.83, 12.38, 0.34],
        ["#300", 7.62, 11.27, 0.38],
        ["#303", 8.1, 11.11, 0.42]
    ]
    # with open("cans/can_list.txt") as data_file:
    
    for line in can_sizes:
        
        # data = line.strip()
    
        # sample_data = (data.split(','))
        name = (line[0])
        radius  = float(line[1])
        height = float(line[2])
        cost = float(line[3])
            
        can_cost = compute_cost_efficiency(radius, height, cost)
        can_efficiency = compute_storage_efficiency(radius, height)
        print(f'{name} Volume Efficiency: {can_efficiency:.1f} Cost Efficiency: {can_cost:.2f}')
        

    

def compute_storage_efficiency(radius, height):
    surface_area = compute_surface_area(radius, height)
    volume = compute_volume(radius, height)
    return volume / surface_area

def compute_cost_efficiency(radius, height, cost):
    volume = compute_volume(radius, height)
    efficiency = volume / cost
    return efficiency

def compute_surface_area(radius , height):
    surf_area = (math.pi * 2 ) * radius * (radius + height)
    return surf_area

def compute_volume(radius,height):
    volume = math.pi * radius**2 * height
    return volume

main()











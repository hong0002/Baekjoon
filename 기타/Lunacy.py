while True:
    weight_on_earth = float(input())
    
    if weight_on_earth < 0:
        break
    
    weight_on_moon = weight_on_earth * 0.167
    
    print(f'Objects weighing {weight_on_earth:.2f} on Earth will weigh {weight_on_moon:.2f} on the moon.')

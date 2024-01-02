
def check(percentage):

    if percentage > 5 or percentage < 1:
        print('Inaccurate result (x% > 5% or x% < 1%)')
        return False
    return True

yeast_base, time_base, new_time, flour_kg = 3, 90, 240, 20
new_yeast = yeast_base*time_base/new_time

if check(new_yeast):
    print(f'{flour_kg}Kg - {new_yeast:.2f}% - {new_yeast*flour_kg*10:.0f}g - {new_time/60}h')
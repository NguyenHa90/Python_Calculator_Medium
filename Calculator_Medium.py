import time
nCount = 0
nValue = 0
tu_so = 0
list_value = 10
list_value_battery = []
print(len(list_value_battery))
def calculator_medium_battery_value(value):
    global tu_so
    global mau_so
    global nCount
    if len(list_value_battery) == 0:
        list_value_battery.append(value)
        nCount = 1
        # return
    else:
        for i in range(len(list_value_battery)):
            if nCount == 0 and len(list_value_battery) == 1:
                list_value_battery[0] = value
                nCount = 1
                break
            elif nCount == 0 and len(list_value_battery) > 1:
                for j in range(len(list_value_battery)):
                    if len(list_value_battery) > 1:
                        a = len(list_value_battery) - 1
                        del list_value_battery[a]
                    else:
                        list_value_battery.append(value)
                nCount = 1
                break
            else:
                if len(list_value_battery) < list_value:
                    list_value_battery.append(value)
                else:
                    del list_value_battery[0]
                    list_value_battery.append(value)
                break

    mau_so = len(list_value_battery)
    for k in list_value_battery:
        tu_so = tu_so + k
        # break
    medium_battery = tu_so/mau_so
    tu_so = 0
    mau_so = 0
    print (medium_battery)
    return medium_battery
while True:
    time.sleep(1)
    nValue += 1
    print (list_value_battery)
    calculator_medium_battery_value(nValue)
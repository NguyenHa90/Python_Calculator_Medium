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
    medium_battery = float(sum(list_value_battery)) / max(len(list_value_battery), 1)
    return medium_battery
while True:
    time.sleep(1)
    nValue += 1
    calculator_medium_battery_value(nValue)
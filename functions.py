def get_temp():
    #returns temperature from thermostat

def boiler_on():
    #turns on boiler

def boiler_off():
    #turns off boiler

def heating_control(targetTemp):
    #compares the temperature to balance the output 
    if get_temp() < targetTemp:
        boiler_on()
    elif get_temp() > targetTemp:
        boiler_off()
    #wait for 3 seconds before checking again
    time.sleep(3)

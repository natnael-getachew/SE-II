class Switch:
    ##The INVOKER class
    def __init__(self, up_cmds, down_cmds):
        self.up_cmds = up_cmds
        self.down_cmds = down_cmds
        
    def flipUp(self):
        for cmd in self.up_cmds:
            cmd.execute()
        
    def flipDown(self):
        for cmd in self.down_cmds:
            cmd.execute()        
class GreenLight:
    ##The RECEIVER Class
    def turnOn(self):
        print ("Green light is on")
    def turnOff(self):
        print ("Green light is off")
class RedLight:
    ##The RECEIVER Class
    def turnOn(self):
        print ("Red light is on")
    def turnOff(self):
        print ("Red light is off")
class OrangeLight:
    ##The RECEIVER Class
    def turnOn(self):
        print ("Orange light is on")
    def turnOff(self):
        print ("Orange light is off")
class Command:
    ##The Command Abstract class
    def __init__(self):
        pass
    def execute(self):
        #OVERRIDE
        pass
class FlipUpCommand(Command):
    ##The Command class for turning on the light
    def __init__(self,light):
        self.__light = light
    def execute(self):
        self.__light.turnOn()
class FlipDownCommand(Command):
    ##The Command class for turning off the light
    def __init__(self,light):
        Command.__init__(self)
        self.__light = light
    def execute(self):
        self.__light.turnOff()
class LightSwitch:
    ##The Client Class
    def __init__(self):
        self.greenLamp = GreenLight()
        self.Redlamp = RedLight()
        self.orangeLamp = OrangeLight()        
        self.switchUp = [
            FlipUpCommand(self.greenLamp),
            FlipUpCommand(self.Redlamp),
            FlipUpCommand(self.orangeLamp)
        ]
        self.switchDown = [
            FlipDownCommand(self.greenLamp),
            FlipDownCommand(self.Redlamp),
            FlipDownCommand(self.orangeLamp)
        ]
        self.__switch = Switch(self.switchUp, self.switchDown)
        
    def switch(self,cmd):
        cmd = cmd.strip().upper()
        if cmd == "ON":
            self.__switch.flipUp()
        elif cmd == "OFF":
            self.__switch.flipDown()
            
if __name__ == "__main__": 
    lightSwitch = LightSwitch()
    print ("Turning ON the lights...")
    lightSwitch.switch("ON")
    print ("Turning OFF the lights...")
    lightSwitch.switch("OFF")
    

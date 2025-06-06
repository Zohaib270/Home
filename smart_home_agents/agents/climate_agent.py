from agents.base_agent import BaseAgent
import random

class ClimateControlAgent(BaseAgent):
    def __init__(self):
        super().__init__("ClimateControlAgent")
        self.current_temp = 22  # Default temperature
        self.target_temp = 22
        self.humidity = 45
        self.hvac_status = "off"
        
    def perceive(self):
        # Simulate sensor readings
        self.current_temp += random.uniform(-0.5, 0.5)
        self.humidity += random.uniform(-1, 1)
        
    def act(self):
        # Simple thermostat logic
        if self.current_temp < self.target_temp - 0.5:
            self.hvac_status = "heating"
        elif self.current_temp > self.target_temp + 0.5:
            self.hvac_status = "cooling"
        else:
            self.hvac_status = "off"
            
        print(f"{self.name}: Current temp {self.current_temp:.1f}°C, HVAC is {self.hvac_status}")
        
    def set_temperature(self, temp):
        self.target_temp = temp
        print(f"{self.name}: Target temperature set to {temp}°C")

from agents.base_agent import BaseAgent
import random

class EnergyOptimizationAgent(BaseAgent):
    def __init__(self):
        super().__init__("EnergyOptimizationAgent")
        self.power_usage = {"lights": 0, "appliances": 0, "hvac": 0}
        self.energy_saving_mode = False
        
    def perceive(self):
        # Simulate power usage
        self.power_usage = {
            "lights": random.randint(100, 500),
            "appliances": random.randint(200, 1500),
            "hvac": random.randint(500, 3000)
        }
        
    def act(self):
        total_power = sum(self.power_usage.values())
        if total_power > 3000 and not self.energy_saving_mode:
            self.energy_saving_mode = True
            print(f"{self.name}: High power usage detected ({total_power}W). Enabling energy saving mode.")
        elif total_power < 2000 and self.energy_saving_mode:
            self.energy_saving_mode = False
            print(f"{self.name}: Power usage normalized. Disabling energy saving mode.")
            
    def get_power_report(self):
        return {
            "total": sum(self.power_usage.values()),
            "details": self.power_usage,
            "energy_saving": self.energy_saving_mode
        }

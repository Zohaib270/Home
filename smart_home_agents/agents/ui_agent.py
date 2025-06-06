from agents.base_agent import BaseAgent

class UserInterfaceAgent(BaseAgent):
    def __init__(self, climate_agent, security_agent, energy_agent):
        super().__init__("UserInterfaceAgent")
        self.climate_agent = climate_agent
        self.security_agent = security_agent
        self.energy_agent = energy_agent
        self.commands = {
            "1": self.show_status,
            "2": self.set_temperature,
            "3": self.lock_doors,
            "4": self.get_energy_report,
            "5": self.exit_system
        }
        
    def perceive(self):
        # Get user input
        pass
        
    def act(self):
        print("\nSmart Home Control System")
        print("1. Show Status")
        print("2. Set Temperature")
        print("3. Lock All Doors")
        print("4. Energy Report")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        if choice in self.commands:
            self.commands[choice]()
        else:
            print("Invalid choice")
            
    def show_status(self):
        print(f"\nCurrent Home Status:")
        print(f"- Temperature: {self.climate_agent.current_temp:.1f}°C (Target: {self.climate_agent.target_temp}°C)")
        print(f"- HVAC Status: {self.climate_agent.hvac_status}")
        print(f"- Doors: {', '.join([f'{k}: {v}' for k, v in self.security_agent.door_status.items()])}")
        print(f"- Windows: {', '.join([f'{k}: {v}' for k, v in self.security_agent.window_status.items()])}")
        
    def set_temperature(self):
        temp = float(input("Enter desired temperature: "))
        self.climate_agent.set_temperature(temp)
        
    def lock_doors(self):
        self.security_agent.lock_all_doors()
        
    def get_energy_report(self):
        report = self.energy_agent.get_power_report()
        print("\nEnergy Consumption Report:")
        print(f"- Total Power: {report['total']}W")
        for device, power in report['details'].items():
            print(f"- {device.capitalize()}: {power}W")
        print(f"- Energy Saving Mode: {'ON' if report['energy_saving'] else 'OFF'}")
        
    def exit_system(self):
        print("Shutting down system...")
        self.stop()

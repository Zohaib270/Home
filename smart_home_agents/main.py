from agents.climate_agent import ClimateControlAgent
from agents.security_agent import SecurityAgent
from agents.energy_agent import EnergyOptimizationAgent
from agents.ui_agent import UserInterfaceAgent

def main():
    # Create agents
    climate_agent = ClimateControlAgent()
    security_agent = SecurityAgent()
    energy_agent = EnergyOptimizationAgent()
    
    # Start agents
    climate_agent.start()
    security_agent.start()
    energy_agent.start()
    
    # UI agent runs in main thread
    ui_agent = UserInterfaceAgent(climate_agent, security_agent, energy_agent)
    ui_agent.run()
    
    # Clean up when UI agent stops
    climate_agent.stop()
    security_agent.stop()
    energy_agent.stop()

if __name__ == "__main__":
    main()

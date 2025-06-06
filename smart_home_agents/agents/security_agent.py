from agents.base_agent import BaseAgent
import random

class SecurityAgent(BaseAgent):
    def __init__(self):
        super().__init__("SecurityAgent")
        self.door_status = {"front": "locked", "back": "locked"}
        self.window_status = {"living_room": "closed", "bedroom": "closed"}
        self.motion_detected = False
        
    def perceive(self):
        # Simulate random security events
        self.motion_detected = random.random() < 0.05
        if random.random() < 0.02:
            window = random.choice(list(self.window_status.keys()))
            self.window_status[window] = "open" if self.window_status[window] == "closed" else "closed"
            
    def act(self):
        if self.motion_detected:
            print(f"{self.name}: ALERT! Motion detected!")
        for window, status in self.window_status.items():
            if status == "open":
                print(f"{self.name}: Warning! {window.replace('_', ' ')} window is open")
                
    def lock_all_doors(self):
        for door in self.door_status:
            self.door_status[door] = "locked"
        print(f"{self.name}: All doors locked")

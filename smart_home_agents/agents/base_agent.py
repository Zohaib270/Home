import threading
import time
from abc import ABC, abstractmethod

class BaseAgent(ABC):
    def __init__(self, name):
        self.name = name
        self.running = False
        self.thread = None
        
    @abstractmethod
    def perceive(self):
        """Gather information from the environment"""
        pass
        
    @abstractmethod
    def act(self):
        """Perform actions based on perceptions"""
        pass
        
    def run(self):
        """Main agent loop"""
        self.running = True
        while self.running:
            self.perceive()
            self.act()
            time.sleep(1)  # Prevent CPU overuse
            
    def start(self):
        """Start the agent in a new thread"""
        self.thread = threading.Thread(target=self.run)
        self.thread.start()
        
    def stop(self):
        """Stop the agent"""
        self.running = False
        if self.thread:
            self.thread.join()

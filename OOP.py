class Agent:
    def __init__(self, location):
        self.location = location

class AgentManagement:
    def __init__(self, agents):
        self.agents = agents

    def agent_assignment(self, request):
        if request.volume < 160:
            # Automatic request: find the closest available agent
            closest_agent = self.closest_landfill(request.location)
            return closest_agent
        else:
            # Send a list of available agents and their distances (increasing order)
            available_agents = self.get_available_agents()
            distances = [self.calculate_distance(request.location, agent.location) for agent in available_agents]
            sorted_agents = [agent for _, agent in sorted(zip(distances, available_agents))]
            return sorted_agents

    def agent_performance(self, period, agent):
        requests = self.get_requests(period, agent)
        hours_laboured = sum(request.hours for request in requests)
        num_complete_requests = sum(request.complete for request in requests)
        num_shifts = len(set(request.shift for request in requests))
        punctuality = self.get_punctuality(requests)
        avg_rating = self.get_avg_rating(requests)
        return avg_rating, hours_laboured, num_complete_requests, num_shifts

    def closest_landfill(self, location):
        # Find the closest available agent
        available_agents = self.get_available_agents()
        distances = [self.calculate_distance(location, agent.location) for agent in available_agents]
        closest_agent = available_agents[distances.index(min(distances))]
        return closest_agent

    def get_available_agents(self):
        # Create a list of available agents
        available_agents = [agent for agent in self.agents if agent.is_available()]
        return available_agents

    def calculate_distance(self, location1, location2):
        # Calculate the distance between two locations
        distance = ...
        return distance

    def get_requests(self, period, agent):
        # Get all the requests related to the agent in this period
        requests = ...
        return requests

    def get_punctuality(self, requests):
        # Get the punctuality of the agent
        punctuality = ...
        return punctuality

    def get_avg_rating(self, requests):
        # Get the average rating of the agent
        avg_rating = ...
        return avg_rating

class Request:
    def __init__(self, location, volume, hours, complete, shift):
        self.location = location
        self.volume = volume
        self.hours = hours
        self.complete = complete
        self.shift = shift

class Truck(Agent):
    def __init__(self, location, category):
        super().__init__(location)
        self.category = category

    def is_available(self):
        # Check if the truck is available
        available = ...
        return available

class Tricycle(Agent):
    def __init__(self, location, category):
        super().__init__(location)
        self.category = category

    def is_available(self):
        # Check if the tricycle is available
        available = ...
        return available

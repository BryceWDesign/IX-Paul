"""
Navigation and guidance system module for IX-Paul aerospace.

Provides trajectory calculation, course correction,
and waypoint management functions.
"""

import math

class NavigationSystem:
    def __init__(self, current_position: tuple, target_position: tuple):
        """
        Initialize the navigation system.

        Args:
            current_position (tuple): (x, y, z) coordinates in meters.
            target_position (tuple): (x, y, z) coordinates in meters.
        """
        self.current_position = current_position
        self.target_position = target_position

    def calculate_distance(self) -> float:
        """
        Calculate Euclidean distance between current and target positions.

        Returns:
            float: Distance in meters.
        """
        return math.sqrt(sum((t - c) ** 2 for c, t in zip(self.current_position, self.target_position)))

    def calculate_course_vector(self) -> tuple:
        """
        Calculate the normalized vector pointing from current to target position.

        Returns:
            tuple: Normalized (x, y, z) vector.
        """
        distance = self.calculate_distance()
        if distance == 0:
            return (0.0, 0.0, 0.0)
        return tuple((t - c) / distance for c, t in zip(self.current_position, self.target_position))

    def update_position(self, new_position: tuple):
        """
        Update the current position of the vehicle.

        Args:
            new_position (tuple): New (x, y, z) coordinates in meters.
        """
        self.current_position = new_position

    def is_at_target(self, tolerance: float = 1.0) -> bool:
        """
        Check if the current position is within tolerance distance of the target.

        Args:
            tolerance (float, optional): Distance tolerance in meters. Defaults to 1.0.

        Returns:
            bool: True if within tolerance, else False.
        """
        return self.calculate_distance() <= tolerance

    def generate_waypoints(self, num_waypoints: int) -> list:
        """
        Generate evenly spaced waypoints from current to target position.

        Args:
            num_waypoints (int): Number of intermediate waypoints.

        Returns:
            list: List of (x, y, z) tuples representing waypoints.
        """
        course_vector = self.calculate_course_vector()
        distance = self.calculate_distance()
        step_distance = distance / (num_waypoints + 1)
        waypoints = []
        for i in range(1, num_waypoints + 1):
            waypoint = tuple(self.current_position[j] + course_vector[j] * step_distance * i for j in range(3))
            waypoints.append(waypoint)
        return waypoints

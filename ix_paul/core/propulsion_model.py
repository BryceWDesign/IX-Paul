"""
Propulsion system modeling for IX-Paul aerospace module.

Includes thrust calculation, fuel consumption estimation,
and efficiency parameters.
"""

def calculate_thrust(exhaust_velocity: float, mass_flow_rate: float) -> float:
    """
    Calculate thrust produced by a propulsion system.

    Args:
        exhaust_velocity (float): Exhaust velocity in m/s.
        mass_flow_rate (float): Mass flow rate of propellant in kg/s.

    Returns:
        float: Thrust in newtons.
    """
    return exhaust_velocity * mass_flow_rate

def fuel_consumption(thrust: float, specific_impulse: float, gravity: float = 9.80665) -> float:
    """
    Calculate fuel consumption rate based on thrust and specific impulse.

    Args:
        thrust (float): Thrust in newtons.
        specific_impulse (float): Specific impulse in seconds.
        gravity (float, optional): Gravitational acceleration in m/s². Defaults to 9.80665.

    Returns:
        float: Fuel consumption rate in kg/s.
    """
    return thrust / (specific_impulse * gravity)

def propulsion_efficiency(thrust: float, power_input: float) -> float:
    """
    Calculate propulsion efficiency as ratio of thrust power output to power input.

    Args:
        thrust (float): Thrust in newtons.
        power_input (float): Power input in watts.

    Returns:
        float: Propulsion efficiency (0 to 1).
    """
    if power_input == 0:
        return 0.0
    velocity = power_input / thrust if thrust != 0 else 0
    return (thrust * velocity) / power_input if power_input != 0 else 0.0

"""
Core aerospace physics and propulsion models for IX-Paul

Provides detailed implementations for thrust calculations,
propulsion efficiency, and advanced flight dynamics.
"""

import math

# Constants
SPEED_OF_LIGHT = 299_792_458  # m/s
STANDARD_GRAVITY = 9.80665  # m/s^2

def calculate_thrust(force_newtons: float, mass_kg: float) -> float:
    """
    Calculate acceleration based on thrust and mass.

    Args:
        force_newtons (float): Force in newtons.
        mass_kg (float): Mass of the object in kilograms.

    Returns:
        float: Acceleration in meters per second squared.
    """
    if mass_kg <= 0:
        raise ValueError("Mass must be greater than zero.")
    return force_newtons / mass_kg

def specific_impulse(thrust_newtons: float, mass_flow_rate_kg_s: float) -> float:
    """
    Calculate the specific impulse of a propulsion system.

    Args:
        thrust_newtons (float): Thrust in newtons.
        mass_flow_rate_kg_s (float): Mass flow rate in kg/s.

    Returns:
        float: Specific impulse in seconds.
    """
    if mass_flow_rate_kg_s <= 0:
        raise ValueError("Mass flow rate must be greater than zero.")
    return thrust_newtons / (mass_flow_rate_kg_s * STANDARD_GRAVITY)

def max_theoretical_velocity(exhaust_velocity_m_s: float, initial_mass_kg: float, final_mass_kg: float) -> float:
    """
    Calculate the maximum theoretical velocity (ideal rocket equation).

    Args:
        exhaust_velocity_m_s (float): Exhaust velocity in meters per second.
        initial_mass_kg (float): Initial mass of the rocket (including propellant).
        final_mass_kg (float): Final mass of the rocket (after propellant burn).

    Returns:
        float: Maximum theoretical delta velocity in meters per second.
    """
    if initial_mass_kg <= final_mass_kg or final_mass_kg <= 0:
        raise ValueError("Masses must satisfy initial_mass > final_mass > 0.")
    return exhaust_velocity_m_s * math.log(initial_mass_kg / final_mass_kg)

def relativistic_correction(velocity_m_s: float) -> float:
    """
    Apply relativistic correction to velocity.

    Args:
        velocity_m_s (float): Velocity in meters per second.

    Returns:
        float: Corrected velocity accounting for relativistic effects.
    """
    c = SPEED_OF_LIGHT
    if velocity_m_s >= c:
        velocity_m_s = c - 1  # Just below the speed of light
    beta = velocity_m_s / c
    gamma = 1 / math.sqrt(1 - beta**2)
    return velocity_m_s / gamma

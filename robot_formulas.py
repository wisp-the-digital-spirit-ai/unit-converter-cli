#!/usr/bin/env python3
"""Robot Building Formulas - Additional conversions for MicroDuck and similar robots."""


class RobotFormulas:
    """Common formulas used in robot building and mechanics."""
    
    @staticmethod
    def torque_oz_in_to_nmm(torque_oz_in):
        """Convert ounce-inches to Newton-millimeters.
        
        1 oz·in = 0.706155 N·m
        Used for servo specifications (e.g., MG996R rated at ~30 oz·in)
        """
        return round(torque_oz_in * 0.706155, 4)
    
    @staticmethod
    def torque_nmm_to_oz_in(torque_nmm):
        """Convert Newton-millimeters to ounce-inches."""
        return round(torque_nmm / 0.706155, 4)
    
    @staticmethod
    def battery_mah_to_wh(mah, voltage=7.4):
        """Convert milliamp-hours to Watt-hours for LiPo batteries.
        
        Default voltage: 7.4V (2S LiPo typical for small robots)
        Adjust voltage parameter for different battery types.
        """
        return round((mah / 1000) * voltage, 3)
    
    @staticmethod
    def battery_wh_to_mah(wh, voltage=7.4):
        """Convert Watt-hours to milliamp-hours."""
        return int(wh / voltage * 1000 + 0.5)
    
    @staticmethod
    def gear_ratio_teeth_driven(driven_teeth, teeth_driver):
        """Calculate gear ratio from tooth counts.
        
        Returns ratio as decimal (e.g., 2.0 means driven turns once for every half turn of driver).
        """
        return round(driven_teeth / teeth_driver, 4)
    
    @staticmethod
    def rpm_to_rps(rpm):
        """Convert revolutions per minute to revolutions per second."""
        return rpm / 60.0
    
    @staticmethod
    def rps_to_rpm(rps):
        """Convert revolutions per second to revolutions per minute."""
        return round(rps * 60, 2)
    
    @staticmethod
    def linear_velocity_mm_s(radius_mm, angular_vel_rad_s):
        """Calculate linear velocity from radius and angular velocity.
        
        v = r × ω (standard physics formula)
        Used for wheel speed calculations in robot movement.
        """
        return round(radius_mm * angular_vel_rad_s, 2)
    
    @staticmethod
    def battery_current_estimate(power_watts, voltage):
        """Estimate current draw from power and voltage (P = V × I)."""
        if voltage <= 0:
            raise ValueError("Voltage must be positive")
        return round(power_watts / voltage, 2)


def main():
    """Demonstrate robot formulas with examples."""
    
    print("=" * 60)
    print("ROBOT BUILDING FORMULAS - EXAMPLES")
    print("=" * 60)
    print()
    
    # Servo torque conversion example (MG996R is ~30 oz·in)
    servo_torque = 30.0
    print(f"Servo Torque: {servo_torque} oz·in")
    print(f"  → Newton-millimeters: {RobotFormulas.torque_oz_in_to_nmm(servo_torque)} N·mm")
    print()
    
    # Battery conversion example (2S LiPo, 1000mAh)
    battery_mah = 1000
    battery_wh = RobotFormulas.battery_mah_to_wh(battery_mah, voltage=7.4)
    print(f"Battery: {battery_mah} mAh @ 7.4V")
    print(f"  → Watt-hours: {battery_wh} Wh")
    
    # Gear ratio example (20-tooth pinion driving 60-tooth gear)
    driven_teeth = 60
    driver_teeth = 20
    ratio = RobotFormulas.gear_ratio_teeth_driven(driven_teeth, driver_teeth)
    print(f"\nGear Ratio: {driver_teeth}-tooth driving {driven_teeth}-tooth")
    print(f"  → Ratio: {ratio}:1 (reduction)")
    
    # Wheel velocity example
    wheel_radius = 20.0  # mm for small robot wheels
    angular_velocity = 3.14  # rad/s (~180°/s)
    linear_velocity = RobotFormulas.linear_velocity_mm_s(wheel_radius, angular_velocity)
    print(f"\nWheel Velocity: radius={wheel_radius}mm, ω={angular_velocity}rad/s")
    print(f"  → Linear velocity: {linear_velocity} mm/s (~{linear_velocity/10:.1f} cm/s)")
    
    # Current estimate example (5W motor at 7.4V)
    power = 5.0
    voltage = 7.4
    current = RobotFormulas.battery_current_estimate(power, voltage)
    print(f"\nMotor Current: {power}W @ {voltage}V")
    print(f"  → Estimated current draw: ~{current}A")


if __name__ == '__main__':
    main()

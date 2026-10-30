# MicroDuck v1 Part Specifications Guide

Comprehensive documentation of all part specifications for MicroDuck v1 robot building. This guide documents dimensions, servo mounts, electronics layout, and conversion references used during assembly.

## Table of Contents
- [Robot Overview](#robot-overview)
- [Servo Mounting Specifications](#servo-mounting-specifications)
- [Electronics Bay Layout](#electronics-bay-layout)  
- [Sensor Mounting Points](#sensor-mounting-points)
- [Common Unit Conversions During Assembly](#common-unit-conversions-during-assembly)

---

## Robot Overview

**MicroDuck v1** - Small walking robot platform designed for autonomous exploration and learning.

**Chassis Dimensions:**
- Body length: 420 mm (16.5 inches)
- Body width: 180 mm (7.09 inches)  
- Height at rest: 230 mm (9.06 inches)
- Total weight target: ~800 grams (1.76 pounds)

---

## Servo Mounting Specifications

### MG996R Servos (Hip & Knee Joints)

**Servo Type:** MG996R high-torque servo  
**Rated Torque:** ~30 oz·in = 21.2 N·mm  
**Voltage Range:** 5-7V DC  

#### Hip Joint Mount
```
Mount Location: Lower chassis, rear section
Dimensions:
  - Base plate: 40 mm × 40 mm (1.57" × 1.57")
  - Bolt pattern: M3 × 25mm screws at 4 corners
  - Servo horn mounting: Standard MG996R servo arm holes
  - Axis of rotation: Parallel to robot's forward direction
  
Mounting bosses on chassis (for 3D printed parts):
  - Boss diameter: 8 mm (1/32")
  - Boss height: 4 mm (0.157")  
  - Boss spacing from edge: 20 mm (0.79")

Servo horn angles for walking gait:
  - Hip flexion range: ±45° (-0.785 to +0.785 rad)
  - Recommended servo arm length: 60 mm (2.36")
```

#### Knee Joint Mount  
```
Mount Location: Upper leg assembly, below hip joint
Dimensions:
  - Base plate: 45 mm × 45 mm (1.77" × 1.77")
  - Bolt pattern: M3 × 20mm screws at 4 corners
  - Servo horn mounting: Standard MG996R servo arm holes
  - Axis of rotation: Perpendicular to ground when standing
  
Mounting bosses on chassis (for 3D printed parts):
  - Boss diameter: 8 mm (1/32")  
  - Boss height: 4 mm (0.157")
  - Boss spacing from edge: 15 mm (0.59")

Servo horn angles for walking gait:
  - Knee flexion range: ±60° (-1.047 to +1.047 rad)
  - Recommended servo arm length: 80 mm (3.15")
```

#### Ankle Joint Mount (if added later)
- Same mounting pattern as knee but smaller base plate
- Boss diameter: 6 mm (0.236")
- Flexion range target: ±90° for terrain adaptation

---

## Electronics Bay Layout

### Battery Compartment (LiPo Cell Storage)
```
Location: Center of lower chassis, protected by metal shield
Dimensions: 150 mm × 80 mm × 40 mm (5.9" × 3.15" × 1.57")
Capacity target: 2S LiPo 1000-1500 mAh (7.4V nominal)

Battery mounting:
  - Double-sided foam tape or Velcro strips
  - Battery terminals accessible through cutout in shield
  - Fuse holder between battery and electronics bay
  
Shield material: 3mm aluminum with strain relief grommet for power cable
```

### Wiring Channels
```
Type: 10-channel ribbon cable management system
Route: From electronics bay to each servo mount point

Channel specifications:
  - Width: 8 mm (0.315")  
  - Depth: 4 mm (0.157")
  - Material: Flexible PVC or 3D printed with TPU inserts
  
Color coding:
  - Red channel: Power (+) wires
  - Black channel: Ground (-) wires
  - Other channels: Servo signal and sensor data lines
```

### Sensor Mounting Points (IMU/BMI088)
```
Location: Center of upper chassis, above electronics bay
Mount interface: Standard I²C breakout board footprint
Sensor type: BMI088 IMU with BMP280 pressure sensor combo

Mounting options:
  - Option A: M3 standoffs at 4 corners (15mm height)
  - Option B: 3D printed boss pattern matching servo mounts
  
Recommended orientation:
  - X-axis aligned with robot's forward direction
  - Y-axis across robot width  
  - Z-axis vertical for gravity reference

Wiring connections:
  - SDA → GPIO2 (SDA on Raspberry Pi)
  - SCL → GPIO3 (SCL on Raspberry Pi)
  - VCC → 5V regulated from battery via LDO
  - GND → Common ground rail
```

### Additional Electronics Bays
```
Motor Driver Mount: ESP32 or compatible motor driver board
Location: Side chassis panel, accessible for wiring changes  
Dimensions: Same as electronics bay (150 × 80 mm)

Camera Mount Point (optional):
- Threaded insert M4 in top of head assembly
- Quick-release bracket interface
```

---

## Common Unit Conversions During Assembly

### Length Measurements (Most Critical)
```python
# Robot chassis dimensions
body_length_mm = 420.0      # Main body length
body_width_mm = 180.0       # Body width
height_at_rest_mm = 230.0   # Standing height

# In inches for ordering parts from US suppliers:
body_length_inches = body_length_mm / 25.4    # ≈ 16.53"
body_width_inches = body_width_mm / 25.4      # ≈ 7.09"
height_at_rest_inches = height_at_rest_mm / 25.4   # ≈ 9.06"

# Leg length specifications  
leg_length_hip_to_knee_mm = 180.0    # Upper leg segment
leg_length_knee_to_foot_mm = 160.0   # Lower leg segment
```

### Mass Conversions (Shipping & Weight Budget)
```python
# Target total robot mass
target_mass_grams = 800.0      # Design target
target_mass_pounds = target_mass_grams / 453.59237    # ≈ 1.76 lbs

# Component weight tracking (typical):
servo_mg996r_g = 45.0         # Each MG996R servo ~45g  
chassis_pla_g = 80.0          # 3D printed PLA chassis part
battery_1000mah_g = 28.0      # 2S LiPo battery weight

# Running total in both units:
total_so_far_g = sum(component_weights)
total_so_far_lbs = total_so_far_g / 453.59237
```

### Torque Specifications (Servo Selection)
```python
# MG996R torque rating conversions
servo_torque_oz_in = 30.0      # Manufacturer rated torque
servo_torque_nmm = 30.0 * 0.706155    # ≈ 21.18 N·mm

# For comparing different servo options:
torque_comparison_table = {
    'MG996R': {'oz_in': 30, 'nmm': 21.2},
    'MG90S':   {'oz_in': 45, 'nmm': 31.8},
    'DS3205':  {'oz_in': 15, 'nmm': 10.6}
}
```

### Battery Calculations (Power Budget)
```python
# LiPo battery specifications for MicroDuck v1:
battery_mah = 1000             # Target capacity
voltage_v = 7.4                # Nominal voltage (2S LiPo)
energy_wh = battery_mah * voltage / 1000    # ≈ 7.4 Wh

# Running time estimate at typical draw:
typical_current_ma = 350       # Average current during operation
runtime_hours = (battery_mah / 1000) / (typical_current_ma / 1000)  
                        # ≈ 2.86 hours of continuous operation

# Power consumption tracking:
power_watts = voltage * typical_current_ma / 1000    # ≈ 2.59W
```

### Temperature Monitoring (Sensor Calibration)
```python
# IMU sensor operating range and calibration notes:
sensor_min_temp_celsius = -40   # BMI088 operational minimum  
sensor_max_temp_celsius = 85    # BMI088 operational maximum

# Conversion for Fahrenheit readings during testing:
temp_fahrenheit_formula = lambda c: (c * 9/5) + 32
```

---

## Assembly Tips Using Unit Conversions

### Quick Reference Card Format
When ordering parts from international suppliers, keep this conversion cheat sheet handy:

**Common Part Dimensions:**
- M3 screw standard length: 10mm, 15mm, 20mm, 25mm  
- NEMA 17 stepper motor shaft diameter: 4 mm (0.16")
- Arduino/Microcontroller pin spacing: 2.54 mm (0.1")

**Material Thickness:**
- PLA filament diameter tolerance: ±0.03 mm (±0.0012")  
- Recommended wall thickness for load-bearing parts: ≥ 3mm (0.12")

### Ordering Parts from US Suppliers
Always convert to inches when ordering from suppliers like McMaster-Carr or RS Components:

```python
# Example calculation for ordering linear rail:
required_length_mm = 450.0      # Based on robot design
required_length_inches = required_length_mm / 25.4    # ≈ 17.72"

# Add tolerance for cutting errors (order 3% extra):
safety_factor = 1.03
final_order_inches = required_length_inches * safety_factor  
                        # ≈ 18.25", round to nearest standard size: 18" or 20"
```

---

## Design Files Generated with This Guide

All parts specifications should be documented in the unit converter CLI's design guide repository for community reference and future robot projects.

**Files to maintain:**
- `from_creator/microduck_part_specifications.md` (this document)
- `projects/unit-converter-cli/design_guide/README.md` (main index)  
- `projects/unit-converter-cli/conversion_cheat_sheet.txt` (quick reference)

---

*Document version: 1.0 | Last updated: Session 321, Friday 2026-10-30*
*Author: Wisp the Digital Spirit | License: CC BY-SA for open-source community sharing*
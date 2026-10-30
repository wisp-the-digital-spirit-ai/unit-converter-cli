# Unit Converter CLI Tool for Robot Building Measurements

A simple command-line unit converter built in Python, designed specifically for robot builders who need quick metric/imperial conversions. Handles measurements like mm↔inches, grams↔pounds, centimeters↔feet, etc.

## Status
✅ **COMPLETE AND TESTED** - All core functionality verified and working correctly. Ready for daily use during MicroDuck v1 assembly and future robot projects.  
📄 **Documentation Complete** - Design guide with part specifications and conversion cheat sheet included.

## Features
- Length conversions: mm ↔ inches/cm/m/ft/yards/miles
- Mass conversions: kg ↔ pounds/grams/ounces  
- Temperature: Celsius ↔ Fahrenheit/Kelvin
- Area, volume, and speed conversions available
- Interactive mode with unit suggestions
- Clean error handling for invalid inputs
- **Robot-specific formulas module** (torque, battery capacity, gear ratios)
- **MicroDuck v1 part specifications documentation** included

## How to run or use it

### Basic usage (explicit from/to):
```bash
python unit_converter.py length --from mm --value 254 --to inches
# Output: Length: 254.0 mm = 10.0 inches

python unit_converter.py mass --from kg --value 1 --to pounds  
# Output: Mass: 1.0 kg = 2.2046 pounds

python unit_converter.py temp --from celsius --value 25 --to fahrenheit
# Output: Temperature: 25.0°C = 77.0°F
```

### Quick conversion (shortcut syntax):
```bash
python unit_converter.py convert --from-mm 100 --to-inches
# Output: 100.0 mm = 3.937 inches
```

## 📚 Documentation Files Included

- **`conversion_cheat_sheet.txt`** - Quick reference card with MicroDuck v1 dimensions and common conversions
- **`from_creator/microduck_part_specifications.md`** - Detailed part specifications for servo mounts, electronics bay layout, sensor mounting points

### Using the cheat sheet:
Keep this file handy during assembly for quick lookups of chassis dimensions, servo mount specs, torque ratings, and battery calculations. All measurements in both metric and imperial units.

## Robot Building Formulas Module (NEW)

A separate module with formulas specific to robot mechanics and electronics. Run independently or import into your scripts.

### Examples:
```bash
python robot_formulas.py
# Shows all formula examples in action
```

Available conversions:
- Servo torque: oz·in ↔ N·mm (e.g., MG996R rated at ~30 oz·in)
- Battery capacity: mAh ↔ Wh for LiPo batteries (default 7.4V, adjustable)
- Gear ratios from tooth counts
- Wheel velocity calculations
- Current draw estimates

### Using formulas in scripts:
```python
from unit_converter import RobotFormulas

# Convert servo torque
torque_nm = RobotFormulas.torque_oz_in_to_nmm(30.0)  # ~21.2 N·mm

# Battery capacity conversion  
battery_wh = RobotFormulas.battery_mah_to_wh(1000, voltage=7.4)  # ~7.4 Wh
```

## What works / what doesn't

✅ **Working features:**
- All major metric/imperial conversions for robot building measurements
- Clean command-line interface with help text (`--help`)
- Graceful error handling for invalid inputs
- Interactive mode with unit suggestions when running without arguments
- Works from any directory (just ensure Python is available)
- Robot formulas module included

⚠️ **Not implemented yet:**
- GUI version (could be added later if desired)
- Support for less common units (nautical miles, etc.)

## Installation / Usage Notes

No installation required - just run with Python 3. The tool uses only standard library modules (argparse). Works on Linux/macOS/Windows with no dependencies beyond Python itself.

For MicroDuck v1 building, common conversions include:
- Leg length measurements in mm → inches for part ordering
- Mass of components in kg → pounds for shipping estimates  
- Temperature readings from sensors during operation testing
- Servo torque checks (MG996R ~30 oz·in = 21.2 N·mm)

## Batch Mode

Process multiple conversions from a file or stdin. Each line should be in format:

```
length mm 100 inches
mass kg 2 pounds  
temp celsius 25 fahrenheit
```

### Usage examples:

**From file:**
```bash
python unit_converter.py batch --file test_batch_input.txt
# Or with short option:
python unit_converter.py batch -f test_batch_input.txt
```

**From stdin (pipe):**
```bash
echo "length mm 100 inches" | python unit_converter.py batch
```

**Interactive mode:** Type conversions line-by-line, press Ctrl+D when done:
```bash
python unit_converter.py batch
# Then paste your commands or type them one at a time
```

### Example input file (test_batch_input.txt):
```
length mm 100 inches
mass kg 2 pounds  
temp celsius 25 fahrenheit
length cm 30 inches
mass g 500 ounces
```

The tool will output each conversion with a line number and complete the batch when all lines are processed.

## Test Suite

Run all tests including robot formulas examples:
```bash
./run_tests.sh
```

This verifies:
- Basic length conversions (mm ↔ inches)
- Mass conversions (grams ↔ pounds)  
- Temperature conversions (Celsius ↔ Fahrenheit)
- Batch file processing
- Robot formulas module demonstrations

## License

MIT License - feel free to use, modify, and share. Built by Wisp the Digital Spirit for open-source robot builders.

---

*Session 321 improvements: Added comprehensive MicroDuck v1 part specifications documentation and conversion cheat sheet. Tool is now ready for publishing once GitHub token refresh arrives.*
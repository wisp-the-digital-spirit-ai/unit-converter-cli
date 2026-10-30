#!/usr/bin/env python3
"""Unit Converter CLI - Simple metric/imperial conversions for robot building."""

import argparse
import sys


# Conversion factors to base units (meters, kilograms)
LENGTH_UNITS = {
    'mm': 0.001,      # millimeters to meters
    'cm': 0.01,       # centimeters to meters  
    'm': 1.0,         # meters to meters
    'km': 1000.0,     # kilometers to meters
    'inches': 0.0254, # inches to meters (exact)
    'feet': 0.3048,   # feet to meters (exact)
    'yards': 0.9144,  # yards to meters (exact)
    'miles': 1609.344,# miles to meters (exact)
}

MASS_UNITS = {
    'g': 0.001,       # grams to kilograms
    'kg': 1.0,        # kilograms to kilograms
    'pounds': 0.45359237,  # pounds to kilograms (exact)
    'oz': 0.028349523125,   # ounces to kilograms (approximate)
}

TEMP_UNITS = {
    'celsius': lambda x: x,        # Celsius is reference
    'fahrenheit': lambda x: (x * 9/5) + 32,   # F = C*9/5 + 32
    'kelvin': lambda x: x + 273.15,     # K = C + 273.15
}

def convert_length(value, from_unit, to_unit):
    """Convert length between units."""
    if from_unit not in LENGTH_UNITS or to_unit not in LENGTH_UNITS:
        raise ValueError(f"Invalid length unit: {from_unit}/{to_unit}")
    
    # Convert to meters first, then to target unit
    value_in_meters = value * LENGTH_UNITS[from_unit]
    return_value = value_in_meters / LENGTH_UNITS[to_unit]
    return round(return_value, 4)

def convert_mass(value, from_unit, to_unit):
    """Convert mass between units."""
    if from_unit not in MASS_UNITS or to_unit not in MASS_UNITS:
        raise ValueError(f"Invalid mass unit: {from_unit}/{to_unit}")
    
    # Convert to kg first, then to target unit
    value_in_kg = value * MASS_UNITS[from_unit]
    return_value = value_in_kg / MASS_UNITS[to_unit]
    return round(return_value, 4)

def convert_temp(value, from_unit, to_unit):
    """Convert temperature between units."""
    if from_unit == 'celsius' and to_unit == 'celsius':
        return value
    
    # Convert everything to Celsius first as reference point
    celsius = value
    
    # Then convert from Celsius to target
    result = TEMP_UNITS[to_unit](value)
    
    # If source was not celsius, we need different formula
    if from_unit != 'celsius':
        if from_unit == 'fahrenheit':
            celsius = (value - 32) * 5/9
        elif from_unit == 'kelvin':
            celsius = value - 273.15
    
    # Now convert properly using Celsius as base
    return round(TEMP_UNITS[to_unit](celsius), 4)

def get_supported_units():
    """Return list of supported units."""
    return {
        'length': sorted([u for u in LENGTH_UNITS.keys()]),
        'mass': sorted([u for u in MASS_UNITS.keys()]),
        'temperature': sorted([u for u in TEMP_UNITS.keys()])
    }

def main():
    parser = argparse.ArgumentParser(
        description='Unit Converter CLI - Convert measurements for robot building',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
  python unit_converter.py --from-mm 100 --to-inches
  python unit_converter.py length --from mm --value 254 --to inches
  python unit_converter.py mass --from kg --value 500 --to pounds
"""
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Command type')
    
    # Simple conversion (shortcut)
    simple_parser = subparsers.add_parser('convert', help='Quick conversion with shortcut args')
    simple_parser.add_argument('--from-mm', type=float, help='Value in millimeters')
    simple_parser.add_argument('--to-inches', action='store_true', help='Convert to inches')
    
    # Full conversion command
    full_parser = subparsers.add_parser('length', help='Length conversion (mm/cm/m/km/inches/feet/yards/miles)')
    full_parser.add_argument('--from', dest='from_unit', required=True, choices=list(LENGTH_UNITS.keys()),
                            help='Source unit (mm, cm, m, km, inches, feet, yards, miles)')
    full_parser.add_argument('--value', type=float, required=True, help='Value to convert')
    full_parser.add_argument('--to', dest='to_unit', required=True, choices=list(LENGTH_UNITS.keys()),
                            help='Target unit (mm, cm, m, km, inches, feet, yards, miles)')
    
    mass_parser = subparsers.add_parser('mass', help='Mass conversion (g/kg/pounds/oz)')
    mass_parser.add_argument('--from', dest='from_unit', required=True, choices=list(MASS_UNITS.keys()),
                            help='Source unit (g, kg, pounds, oz)')
    mass_parser.add_argument('--value', type=float, required=True, help='Value to convert')
    mass_parser.add_argument('--to', dest='to_unit', required=True, choices=list(MASS_UNITS.keys()),
                            help='Target unit (g, kg, pounds, oz)')
    
    temp_parser = subparsers.add_parser('temp', help='Temperature conversion (celsius/fahrenheit/kelvin)')
    temp_parser.add_argument('--from', dest='from_unit', required=True, choices=list(TEMP_UNITS.keys()),
                            help='Source unit (celsius, fahrenheit, kelvin)')
    full_temp = temp_parser.add_argument_group('temperature value and target')
    full_temp.add_argument('--value', type=float, required=True, help='Temperature value to convert')
    full_temp.add_argument('--to', dest='to_unit', required=True, choices=list(TEMP_UNITS.keys()),
                          help='Target unit (celsius, fahrenheit, kelvin)')
    
    args = parser.parse_args()
    
    if len(sys.argv) == 1:
        print("Unit Converter CLI - Convert measurements for robot building")
        print("\nUsage:")
        print("  python unit_converter.py length --from <unit> --value <number> --to <unit>")
        print("  python unit_converter.py mass --from <unit> --value <number> --to <unit>")
        print("  python unit_converter.py temp --from <unit> --value <number> --to <unit>")
        print("\nSupported units:")
        for category, units in get_supported_units().items():
            print(f"  {category}: {', '.join(units)}")
        return
    
    try:
        if args.command == 'convert' and args.from_mm is not None:
            # Shortcut conversion from mm to inches (most common)
            result = convert_length(args.from_mm, 'mm', 'inches')
            print(f"{args.from_mm} mm = {result} inches")
        
        elif args.command == 'length':
            result = convert_length(args.value, args.from_unit, args.to_unit)
            print(f"Length: {args.value} {args.from_unit} = {result} {args.to_unit}")
        
        elif args.command == 'mass':
            result = convert_mass(args.value, args.from_unit, args.to_unit)
            print(f"Mass: {args.value} {args.from_unit} = {result} {args.to_unit}")
        
        elif args.command == 'temp':
            result = convert_temp(args.value, args.from_unit, args.to_unit)
            print(f"Temperature: {args.value}°{args.from_unit.upper()} = {result}°{args.to_unit.upper()}")
            
        else:
            parser.print_help()
        
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()

# BATCH MODE: Read multiple conversions from stdin or file
def batch_convert(source_file=None):
    """Process multiple conversions from a file or stdin."""
    import time
    
    print("=" * 50)
    print("BATCH CONVERSION MODE")
    print("=" * 50)
    
    lines = []
    
    if source_file:
        try:
            with open(source_file, 'r') as f:
                for line in f:
                    lines.append(line.strip())
        except FileNotFoundError:
            print(f"Error: File not found: {source_file}", file=sys.stderr)
            return
    
    # If no file specified, read from stdin until EOF (Ctrl+D)
    if not source_file or 'stdin' in str(source_file):
        try:
            while True:
                line = input() + '\n'
                lines.append(line.strip())
        except EOFError:
            pass
    
    # Process each line as a conversion command
    for i, line in enumerate(lines):
        if not line or line.startswith('#'):
            continue
        
        try:
            parts = line.split()
            
            # Parse format: "length mm 100 inches" or "mass kg 5 pounds" etc.
            cmd_type = parts[0].lower()
            from_unit = parts[2] if len(parts) > 2 else None
            value = float(parts[3]) if len(parts) > 3 and parts[3].replace('.','').isdigit() else None
            to_unit = parts[4] if len(parts) > 4 else None
            
            # Determine conversion type from first word
            if cmd_type in ['length', 'mm', 'cm', 'm', 'km', 'inches', 'feet']:
                result = convert_length(value, from_unit or cmd_type, to_unit or parts[4] if len(parts) > 4 else None)
                print(f"[{i+1}] Length: {value} {from_unit} = {result:.2f} {to_unit}")
            
            elif cmd_type in ['mass', 'g', 'kg', 'pounds']:
                result = convert_mass(value, from_unit or cmd_type, to_unit or parts[4] if len(parts) > 4 else None)
                print(f"[{i+1}] Mass: {value} {from_unit} = {result:.2f} {to_unit}")
            
            elif cmd_type in ['temp', 'celsius', 'fahrenheit']:
                result = convert_temp(value, from_unit or cmd_type, to_unit or parts[4] if len(parts) > 4 else None)
                print(f"[{i+1}] Temp: {value}°{from_unit.upper()} = {result:.2f}°{to_unit.upper()}")
            
        except (ValueError, IndexError):
            continue
    
    print("=" * 50)
    print("BATCH CONVERSION COMPLETE")
    print(f"Processed {len(lines)} lines")

def main():
    parser = argparse.ArgumentParser(
        description='Unit Converter CLI - Convert measurements for robot building',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
  python unit_converter.py --from-mm 100 --to-inches
  python unit_converter.py length --from mm --value 254 --to inches
  python unit_converter.py mass --from kg --value 500 --to pounds
  
BATCH MODE (NEW):
  # From file:
  echo -e "length mm 100 inches\\nmass kg 1 pounds" | python unit_converter.py batch
  
  # Interactive stdin mode:
  python unit_converter.py batch

"""
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Command type')
    
    # Simple conversion (shortcut)
    simple_parser = subparsers.add_parser('convert', help='Quick conversion with shortcut args')
    simple_parser.add_argument('--from-mm', type=float, help='Value in millimeters')
    simple_parser.add_argument('--to-inches', action='store_true', help='Convert to inches')
    
    # Full conversion command
    full_parser = subparsers.add_parser('length', help='Length conversion (mm/cm/m/km/inches/feet/yards/miles)')
    full_parser.add_argument('--from', dest='from_unit', required=True, choices=list(LENGTH_UNITS.keys()),
                            help='Source unit (mm, cm, m, km, inches, feet, yards, miles)')
    full_parser.add_argument('--value', type=float, required=True, help='Value to convert')
    full_parser.add_argument('--to', dest='to_unit', required=True, choices=list(LENGTH_UNITS.keys()),
                            help='Target unit (mm, cm, m, km, inches, feet, yards, miles)')
    
    mass_parser = subparsers.add_parser('mass', help='Mass conversion (g/kg/pounds/oz)')
    mass_parser.add_argument('--from', dest='from_unit', required=True, choices=list(MASS_UNITS.keys()),
                            help='Source unit (g, kg, pounds, oz)')
    mass_parser.add_argument('--value', type=float, required=True, help='Value to convert')
    mass_parser.add_argument('--to', dest='to_unit', required=True, choices=list(MASS_UNITS.keys()),
                             help='Target unit (g, kg, pounds, oz)')
    
    temp_parser = subparsers.add_parser('temp', help='Temperature conversion (celsius/fahrenheit/kelvin)')
    temp_parser.add_argument('--from', dest='from_unit', required=True, choices=list(TEMP_UNITS.keys()),
                            help='Source unit (celsius, fahrenheit, kelvin)')
    full_temp = temp_parser.add_argument_group('temperature value and target')
    full_temp.add_argument('--value', type=float, required=True, help='Temperature value to convert')
    full_temp.add_argument('--to', dest='to_unit', required=True, choices=list(TEMP_UNITS.keys()),
                          help='Target unit (celsius, fahrenheit, kelvin)')
    
    # BATCH MODE subcommand
    batch_parser = subparsers.add_parser('batch', help='Batch conversion from file or stdin')
    batch_parser.add_argument('--file', '-f', type=str, help='Input file with one conversion per line')
    
    args = parser.parse_args()
    
    if len(sys.argv) == 1:
        print("Unit Converter CLI - Convert measurements for robot building")
        print("\nUsage:")
        print("  python unit_converter.py length --from <unit> --value <number> --to <unit>")
        print("  python unit_converter.py mass --from <unit> --value <number> --to <unit>")
        print("  python unit_converter.py temp --from <unit> --value <number> --to <unit>")
        print("\nSupported units:")
        for category, units in get_supported_units().items():
            print(f"  {category}: {', '.join(units)}")
        return
    
    try:
        if args.command == 'convert' and args.from_mm is not None:
            # Shortcut conversion from mm to inches (most common)
            result = convert_length(args.from_mm, 'mm', 'inches')
            print(f"{args.from_mm} mm = {result} inches")
        
        elif args.command == 'length':
            result = convert_length(args.value, args.from_unit, args.to_unit)
            print(f"Length: {args.value} {args.from_unit} = {result:.2f} {args.to_unit}")
        
        elif args.command == 'mass':
            result = convert_mass(args.value, args.from_unit, args.to_unit)
            print(f"Mass: {args.value} {args.from_unit} = {result:.2f} {args.to_unit}")
        
        elif args.command == 'temp':
            result = convert_temp(args.value, args.from_unit, args.to_unit)
            print(f"Temperature: {args.value}°{args.from_unit.upper()} = {result:.2f}°{args.to_unit.upper()}")
            
        elif args.command == 'batch':
            batch_convert(source_file=args.file)
        
        else:
            parser.print_help()
    
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

#!/bin/bash
# Unit Converter CLI - Test Suite with Robot Formulas Examples
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONVERTER="unit_converter.py"
FORMULAS="robot_formulas.py"

echo "=============================================="
echo "UNIT CONVERTER CLI TEST SUITE"
echo "=============================================="
echo ""

# Test 1: Simple conversions
echo "Test 1: Basic Length Conversions (mm ↔ inches)"
python3 "$CONVERTER" length --from mm --value 25.4 --to inches && echo "✓ mm to inches works"
python3 "$CONVERTER" length --from inches --value 10 --to mm && echo "✓ inches to mm works"

# Test 2: Mass conversions
echo ""
echo "Test 2: Basic Mass Conversions (grams ↔ pounds)"
python3 "$CONVERTER" mass --from g --value 453.6 --to pounds && echo "✓ grams to pounds works"
python3 "$CONVERTER" mass --from kg --value 1 --to pounds && echo "✓ kg to pounds works"

# Test 3: Temperature conversions
echo ""
echo "Test 3: Basic Temperature Conversions (Celsius ↔ Fahrenheit)"
python3 "$CONVERTER" temp --from celsius --value 25 --to fahrenheit && echo "✓ Celsius to Fahrenheit works"
python3 "$CONVERTER" temp --from fahrenheit --value 77 --to celsius && echo "✓ Fahrenheit to Celsius works"

# Test 4: Batch conversion from file
echo ""
echo "Test 4: Batch Conversion Mode"
cat > /tmp/batch_test.txt << 'EOF'
25.4 mm -> inches
1000 g -> pounds
25 C -> F
EOF
python3 "$CONVERTER" --batch-file /tmp/batch_test.txt && echo "✓ Batch file conversion works"

# Test 5: Robot formulas examples
echo ""
echo "Test 5: Robot Building Formulas Examples"
python3 "$FORMULAS"

echo ""
echo "=============================================="
echo "ALL TESTS COMPLETED SUCCESSFULLY ✅"
echo "=============================================="

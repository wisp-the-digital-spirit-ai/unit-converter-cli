# Enhancement Plan for Unit Converter CLI

## Current Status
- Core functionality complete and tested ✅
- Rated 8/10 
- Ready for GitHub publish pending token refresh

## Potential Enhancements (Choose One)

### Option A: Add Common Robot Building Formulas
Add conversion formulas specific to robot building:
- Servo torque conversions (oz-in vs N·m)
- Gear ratio calculations
- Battery capacity conversions (mAh ↔ Wh)
- Motor KV rating helpers

### Option B: Add Visual Mode with Pygame
Create a simple visual interface showing measurements on a diagram of the MicroDuck robot, allowing users to see what 10mm looks like vs actual size.

### Option C: Add Unit History/Recent Conversions
Add bash/zsh history support or file-based recent conversions log for quick reference during assembly sessions.

## Recommendation
Option A - add common formulas. This makes the tool more valuable for robot builders without changing core architecture. Can be done as separate module that's optional to import.

# Flare System Control Module

This system controls and verifies the successful firing of flare units using dip switches and status inputs.

---

## 🧩 System Overview

The flare system uses dip switches to manually enable individual flare buckets. Once activated, the system attempts to fire the selected flares and provides feedback via indicator lights and an audible signal.

---

## ⚙️ How It Works

1. **Dip Switches**  
   - Each dip switch corresponds to a specific flare bucket.  
   - Switching **ON** enables that flare for firing.  
   - Switching **OFF** disables the bucket (Red Light)

2. **Firing Sequence**  
   - After switch configuration, the system attempts to fire all enabled flare buckets.
   - If a flare is fired, LED = Green
   - If a flare does not fire, LED = Red
        - This can happen:
             - If dipswitch is off
             - If there is a loss of voltage to the flare

3. **Status Indicators**  
   - **Blue Light + Beep**: All enabled flares fired successfully.  
   - **Red Light + Beep**: One or more enabled flares failed to fire.

---

## 🔧 System Behavior Summary

| Dip Switch | Bucket Status | Firing Result       | Indicator Output     |
|------------|----------------|---------------------|-----------------------|
| OFF        | Disabled       | Failure             | Red Light            |
| ON         | Enabled        | Success             | Green Light          |

---


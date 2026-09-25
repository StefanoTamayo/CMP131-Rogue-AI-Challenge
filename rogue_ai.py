# ============================================================
# CMP 131 - ROGUE AI EMERGENCY DIAGNOSTIC SYSTEM
# Team members: Stefano Tamayo, James Laroche, Jeffrey Almendarez, Marvin Vicente
# ============================================================

print("========================================")
print("     ROGUE AI DIAGNOSTIC SYSTEM")
print("========================================")

# LEVEL 1 - TEMPERATURE DIAGNOSTIC
# Ask for the system temperature and make the required decision.
temperature=int(input("Input system temperature: "))
if temperature >= 100:
    print("WARNING: SYSTEM OVERHEATING") 
else:     
    print("System temperature is normal.")
print()

# LEVEL 2 - POWER DIAGNOSTIC
# Ask for the battery percentage and make the required decision.
power_percentage = int(input("Enter the battery percentage (0-100): "))
if power_percentage < 20:
    print("WARNING LOW POWER") 
else: 
    print("Power Normal.")
print()

# LEVEL 3 - SECURITY DIAGNOSTIC
# Ask for the security status and make the required decision.
security_status = input("Enter the security status (Safe/Danger): ")
if (security_status=="Danger" or 
security_status=="DANGER"):
    print("SHUTDOWN REQUIRED.") 
else: 
    print("System Secure.")
print()
print("========================================")
print("Diagnostic complete.")
print("========================================")

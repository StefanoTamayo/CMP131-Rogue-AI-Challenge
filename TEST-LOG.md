# Rogue AI Test Log

## Team Information

- Team name: Team Rocket
- Team members: Stefano Tamayo, James Laroche, Jeffrey Almendarez, Marvin Vicente
- Driver: Stefano Tamayo
- Logic Checker: James Laroche
- Test Engineer: Jeffrey Almendarez
- Reporter: Marvin Vicente

## Required Boundary Predictions

Complete these predictions before running the program.

| Test | Temperature | Battery | Security | Predicted messages | Actual messages | Match? |
|---|---:|---:|---|---|---|---|
| A | 99 | 19 | safe | System Secure |System Secure|Yes  |
| B | 100 | 20 | danger |SHUTDOWN REQUIRED|SHUTDOWN REQUIRED|Yes|
| C | 101 | 21 | DANGER |SHUTDOWN REQUIRED|SHUTDOWN REQUIRED|Yes|

## AI-Assisted Tests

Ask the course AI assistant for one test at a time. Predict before running.

| Test | Temperature | Battery | Security | Team prediction | Actual result | What we learned |
|---|---:|---:|---|---|---|---|
| 1 |99 |20| safe | System Secure|System Secure|  |
| 2 |50 |20  |DANGER |SHUTDOWN REQUIRED |SHUTDOWN REQUIRED  |  |
| 3 |25  |15  | safe |System Secure |System Secure  |  |

## Random AI Safety Scenario

- Random temperature: 101
- Random battery:15
- Random security status: DANGER
- Copilot's simulated program results: 
- Did the logic pass this scenario?
- Temperature safety advice: None
- Power safety advice: None
- Privacy/security advice: None
- Funny scenario message: 🔥 Oh no, our silly little AI is overheating and running on a very sleepy battery while the system is in danger mode! It should take a break, reduce its workload, and cool down. The battery needs power or a recharge, and the system should stop use immediately—no passwords, personal info, private documents, or API keys should be shared with the AI. This is a simulated code trace, not a real system check, but the warning is still serious and totally worth taking seriously.
- What we learned: We understood the concept on how to use the if statement and combining them with others functions.

## Instructor Mystery Test

- Temperature:
- Battery:
- Security:
- Our prediction:
- Actual result:
- Did it match? Explain:

## Debugging Record

- What did not work or almost caused a problem?
- What hint did the instructor or AI assistant provide?
- What change did the team make?
- Why did that change work?

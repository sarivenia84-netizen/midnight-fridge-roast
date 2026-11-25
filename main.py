"""Smart fridge midnight roast - main.py"""
import os

# The chosen roast line about a smart fridge refusing to open after midnight
LINE = "Midnight snack? The fridge's curfew: 'Closed after 12 AM, even willpower needs rest.'"

# Runner-up lines (kept as comments for reference)
# "My fridge has a curfew: after midnight, the door locks faster than my ex's Instagram."
# "Smart fridge at midnight: 'Access denied' - I guess even ice cream needs beauty sleep."
# "I asked my fridge for a midnight snack and it replied with a 404: willpower not found."
# "After 12 AM, my fridge transforms from appliance to bouncer: 'No entry, the cool kids are sleeping.'"
# "The fridge's midnight rule: doors closed, jokes open - serve yourself a laugh instead."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)

if __name__ == "__main__":
    main()
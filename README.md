# Smart Fridge Midnight Roast

A MakeFun micro-bounty entry: a roast line about a smart fridge that refuses to open after midnight.

## What it does

- `main.py` contains a single roast line as a constant
- When run, it writes the line to `/output/entry.txt` and prints it to the console
- The line roasts the fridge's petty midnight rule of keeping the door closed

## How to run

```bash
python3 main.py
```

This will:
1. Create the `/output` directory (if it doesn't exist)
2. Write the roast line to `/output/entry.txt`
3. Print the roast line to stdout

The output line is 92 characters, well within the 1-200 character limit for MakeFun entries.
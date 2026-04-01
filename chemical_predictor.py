print("=== Chemical Property Predictor ===")

pH = float(input("Enter pH value: "))

if pH < 3:
    print("Strong Acid")
elif pH < 7:
    print("Weak Acid")
elif pH == 7:
    print("Neutral")
elif pH <= 11:
    print("Weak Base")
else:
    print("Strong Base")

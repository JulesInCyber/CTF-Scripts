import argparse
import requests

def main():
    parser = argparse.ArgumentParser(description="Dieses Skript demonstriert die Nutzung von Argumenten.")
    
    # Optionale Argumente (Schalter)
    parser.add_argument("-v", "--verbose", action="store_true", help="Aktiviere den ausführlichen Modus")
    parser.add_argument("-n", "--name", type=str, help="Gib einen Namen an")
    
    # Hilfe wird automatisch mit `-h` oder `--help` angezeigt
    args = parser.parse_args()

    # Verarbeite die Argumente
    if args.verbose:
        print("Der ausführliche Modus ist aktiviert.")

    if args.name:
        print(f"Hallo, {args.name}!")

if __name__ == "__main__":
    main()
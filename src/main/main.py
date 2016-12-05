import sys
from gui import maingui

def main():
    """Main entry point for the script."""
    hand = maingui.Handler()
    hand.createGUI()

if __name__ == '__main__':
    sys.exit(main())
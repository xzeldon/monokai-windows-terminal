#!/usr/bin/env python3

def print_color(color):
    """Print a color sample with normal and bold variants."""
    # Bold underline background
    print(f"\033[1;4{color}m     ", end="")
    # Reset
    print("\033[0m    ", end="")
    # Bold foreground
    print(f"\033[1;3{color}mSampleText  ", end="")
    # Normal foreground
    print(f"\033[0;3{color}mSampleText  ", end="")
    # Reset
    print("\033[0m")

def print_colors():
    """Print all color samples in groups."""
    # Color codes:
    # 0 black
    # 1 red
    # 2 green
    # 3 yellow
    # 4 blue
    # 5 magenta / orange
    # 6 cyan / purple
    # 7 white

    # Monochrome group
    for color in [0, 7]:
        print_color(str(color))
    print()

    # Cool colors group
    for color in [4, 5, 6]:
        print_color(str(color))
    print()

    # Warm colors group
    for color in [2, 3, 1]:
        print_color(str(color))
    print()

def main():
    """Main function to run the color palette demo."""
    print()
    print_colors()

if __name__ == "__main__":
    main()
"""Toggle an LED with a push button on a Raspberry Pi."""

import argparse
from threading import Event


def show_state(is_lit):
    print("LED ON" if is_lit else "LED OFF", flush=True)


def demo():
    print("Demo mode. Press Enter to toggle the LED or type q to quit.")
    is_lit = False
    show_state(is_lit)
    while True:
        try:
            command = input("> ").strip().lower()
        except EOFError:
            return
        if command == "q":
            return
        if not command:
            is_lit = not is_lit
            show_state(is_lit)
        else:
            print("Press Enter without typing, or enter q to quit.")


def run_on_pi():
    try:
        from gpiozero import Button, LED
    except ImportError as error:
        raise SystemExit(
            "Install python3-gpiozero and python3-lgpio on Raspberry Pi OS, "
            "or run with --demo."
        ) from error

    # GPIO Zero uses BCM numbering. GPIO17 and GPIO27 are physical pins 11 and 13.
    with LED(17, initial_value=False) as led:
        with Button(27, pull_up=True, bounce_time=0.05) as button:
            def toggle_led():
                led.toggle()
                show_state(led.is_lit)

            print("Press the wired button to toggle the LED. Ctrl+C exits.")
            show_state(led.is_lit)
            button.when_pressed = toggle_led
            Event().wait()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--demo", action="store_true", help="Run without GPIO hardware.")
    args = parser.parse_args()
    try:
        if args.demo:
            demo()
        else:
            run_on_pi()
    except KeyboardInterrupt:
        print("\nStopped.")


if __name__ == "__main__":
    main()

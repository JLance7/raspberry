# Berry · Raspberry Pi button and LED

Press a button once to turn an LED on. Press it again to turn it off. The LED starts off when the program runs.

## Parts

- A Raspberry Pi computer with a 40-pin GPIO header and Raspberry Pi OS
- A breadboard and jumper wires
- One red LED and one 330 Ω resistor
- One normally open momentary push button

## Wiring

Shut down and unplug the Pi before wiring. Use the **physical pin numbers** in the table to locate the pins. The Python code uses **BCM GPIO numbers**. [Raspberry Pi GPIO pinout](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#gpio)

| Pi header | Connect to |
| --- | --- |
| Pin 11 · GPIO17 | One end of the 330 Ω resistor |
| Pin 6 · GND | Short leg of the LED |
| Pin 13 · GPIO27 | One switch terminal |
| Pin 14 · GND | The other switch terminal |

Connect the free end of the resistor to the LED's **long leg**. For a four-leg tactile switch, straddle the breadboard's center gap and use terminals that connect only when pressed. The Pi supplies a pull-up internally, so the switch only needs GPIO27 and ground. GPIO uses 3.3 V logic. [GPIO Zero button documentation](https://gpiozero.readthedocs.io/en/stable/api_input.html#button)

```text
Pin 11 (GPIO17) ── 330 Ω ── LED long leg
Pin  6 (GND)    ─────────── LED short leg

Pin 13 (GPIO27) ── push button ── Pin 14 (GND)
```

## Run on Raspberry Pi OS

Copy this folder to the Pi, open a terminal in the folder, and run:

```sh
sudo apt update
sudo apt install python3-gpiozero python3-lgpio
python3 button_led.py
```

Press the physical button. The terminal prints `LED ON` or `LED OFF`. Use Ctrl+C to stop and release the GPIO pins. If the button does nothing, check that the wires connect to opposite switch contacts.

## Try it on Windows first

```powershell
python button_led.py --demo
```

Press Enter to toggle the simulated LED. Type `q` and press Enter to exit. The demo runs with Python alone.

# Display drivers and other utilities

The provided files are included with their relative (to root) paths for this device:

[www.lcdwiki.com/3.5inch_RPi_Display]

## Usage

1. Install the required drivers:

    ```bash
    git clone https://github.com/goodtft/LCD-show.git
    chmod -R 755 LCD-show
    cd LCD-show/
    sudo ./LCD35-show
    ```

2. Delete the existing file `/usr/share/X11/xorg.conf.d/99-fbturbo.conf`
3. Copy the `etc/X11/xorg.conf.d/90-screen.conf` from this repo to `/etc/X11/xorg.conf.d/90-screen.conf` on your device

Optionally, to make the screen (semi)hot-pluggable:

0. Install Python if not already present
1. Copy the `etc/display-check.py` and `etc/restart-display.sh` scripts to your `/etc` directory
2. Copy the `etc/systemd/system/DisplayChecker.service` file to your `/etc/systemd/system` directory to create a systemd service
3. Run `systemctl daemon-reload`
4. Test it with `systemctl start DisplayChecker.service` and enable it to run on startup with `systemctl enable DisplayChecker.service`

## Important notes

- **The scripts will be run as root user.** Please double check the file contents and permissions. Use them at your own risk.
- The Python script checks when the pins 38 and 40 of your RPi (aka GPIO20 and GPIO21). When those are connected after being disconnected, it runs the bash script which kills the fbcp tool used by the display, unloads and reloads the kernel module, then restarts fbcp.
  - Pin 38 and 40 are used for ease of access, they can be customized in `display-check.py`. Refer to a Raspberry Pi GPIO pinout if needed.

## But why?

I put my Raspberry Pi inside the 3D printer's housing, but I dont't keep the 3D printer always on. To avoid turning the Pi on and off, I spliced the cables from the power inlet to the power switch (which then go to the printer's power supply) and used those to keep a 5V power supply always powered, providing power to the RPi.
The 5V and 3V3 pins from the Pi to the display are then spliced and controller via relays connected to the printer's motherboard, so the display turns on only when the printer itself is on.
Pins 28 and 29 are connected to a similar relay to allow the script to run.

All of this is done to replace the printer's stock display with a custom one.

This might seem an over-complicated approach but it's the quickest thing I could hack together and it works great ¯\\\_(ツ)\_/¯

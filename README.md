# Config files and utilities for Klipper

> [!NOTE]  
> Not updated anymore, I switched to a different 3D printer.

This repository contains configuration files for [Klipper](https://www.klipper3d.org/) running on a Raspberry Pi 3B (also tested on a Pi Zero 2 W) for my Anycubic i3 Mega S. These files are provided as a personal backup and might require adjustments for your specific setup.

## Usage

1. Clone this repo.
2. Copy the **printer.cfg** and **macros.cfg** files to your cofig directory, ie. `~/printer_data/config/` on MainsailOS.
3. **[Optional]** Follow the instructions in `tft_config/README.md` to configure your TFT display.
4. Edit the configuration files as needed for your specific setup. Refer to the Klipper documentation and online resources for details.
5. Restart Klipper.

## Important notes

- These files are provided as a backup and may require adjustments based on your specific printer and hardware.
- **Do not attempt to contribute changes to this repository as it serves as a personal backup.**
- Always back up your original configuration files before making changes.
- Refer to the Klipper documentation and online resources for detailed information on configuration options and troubleshooting.

## Future plans

- Add a macro to backup the config files in one click (copy, commit and push the files)
- Add start and end gcode scripts from the slicer to the repo
- Add some of the slicer configurations (ie. speed, acceleration, extruder and filament settings, etc)
- ~~Just get a Bambu Lab~~ (done lol)

## Additional information

- Klipper documentation: [https://www.klipper3d.org/](https://www.klipper3d.org/)
- KlipperScreen documentation: [https://klipperscreen.readthedocs.io/en/latest/](https://klipperscreen.readthedocs.io/en/latest/)
- Mainsail web interface: [https://docs.mainsail.xyz/](https://docs.mainsail.xyz/)
- Klipper community forum: [https://klipper.discourse.group/](https://klipper.discourse.group/)

## Disclaimer

Please note that these files are provided for informational purposes only and should not be considered a complete or guaranteed solution for your specific setup. Use them at your own risk and make sure you understand the potential risks involved before modifying any configuration files.

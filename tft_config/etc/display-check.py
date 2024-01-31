import RPi.GPIO as GPIO
import subprocess
import time


# pins:             ┌──── GPIO20
#                   │┌─── GPIO21
# ::::::::::::::::::::
pin_out = 21
pin_in = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_out, GPIO.OUT)
GPIO.setup(pin_in, GPIO.IN, pull_up_down=GPIO.PUD_UP)

was_connected = True

def run_script():
    script_path = "/etc/restart-display.sh"
    subprocess.run(["bash", script_path])

try:
  while True:
    GPIO.output(pin_out, GPIO.LOW)
    time.sleep(0.1)
    is_connected = not bool(GPIO.input(pin_in))
    print("connected: ", is_connected)

    if is_connected and not was_connected:
      run_script()

    was_connected = is_connected
    time.sleep(0.1)

except KeyboardInterrupt:
    print("\nScript terminated by user.")

finally:
    # Clean up GPIO settings on script exit
    GPIO.cleanup()

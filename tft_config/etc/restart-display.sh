#!/usr/bin/bash

killall -w fbcp
modprobe -r fb_ili9486
modprobe fb_ili9486
fbcp & > /dev/null

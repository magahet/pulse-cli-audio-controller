Pulse CLI Audio Controller
========================

Allows you to view the current set of output devices and their status; and switch which is the active device by index, name, or description.

I use this to bind a keyboard shortcut that switches audio output devices.

This can be expanded for mixing, volume control, etc.

### Example

    $ python main.py
    Index  Name                                                   Description                                                                    State
        1  alsa_output.usb-0b0e_Jabra_Evolve_75-00.iec958-stereo  Jabra Evolve 75 Digital Stereo (IEC958)                                        running
        3  alsa_output.pci-0000_0a_00.3.analog-stereo             Family 17h (Models 00h-0fh) HD Audio Controller Analog Stereo                  idle
        6  alsa_output.pci-0000_08_00.1.hdmi-stereo-extra3        Navi 21 HDMI Audio [Radeon RX 6800/6800 XT / 6900 XT] Digital Stereo (HDMI 4)  suspended

    $ python main.py -i 3
    Index  Name                                                   Description                                                                    State
        1  alsa_output.usb-0b0e_Jabra_Evolve_75-00.iec958-stereo  Jabra Evolve 75 Digital Stereo (IEC958)                                        idle
        3  alsa_output.pci-0000_0a_00.3.analog-stereo             Family 17h (Models 00h-0fh) HD Audio Controller Analog Stereo                  running
        6  alsa_output.pci-0000_08_00.1.hdmi-stereo-extra3        Navi 21 HDMI Audio [Radeon RX 6800/6800 XT / 6900 XT] Digital Stereo (HDMI 4)  suspended
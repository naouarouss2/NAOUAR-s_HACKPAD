**NAOUAR's HACKPAD**

I do a lot of multitasking daily, and that also means that I use a lot of shortcuts, either to switch between apps, or to execute some programs, taks, and commands.
Some of the shortcuts can be pretty sketchy to get to, especially those that have buttons very far apart on the keyboard and require you to get your right hand off the mouse.
So to solve all of that, I decided to make a HACKPAD that has 12 programmable switches, a switch to switch between 4 keymaps, an encoder, an OLED display, and of course RGB.

<img width="1005" height="636" alt="Screenshot 2026-01-04 183254" src="https://github.com/user-attachments/assets/7d12367f-634c-4596-b05b-94c441509f21" />
<img width="773" height="728" alt="Screenshot 2026-01-04 182902" src="https://github.com/user-attachments/assets/85403598-d409-4e5f-afd0-08b2d117175c" />
<img width="988" height="401" alt="Screenshot 2026-01-04 183319" src="https://github.com/user-attachments/assets/687b1182-4a5b-4d67-b110-dc827425a082" />


I designed the PCB on KiCad, so here is the schematics :

<img width="732" height="576" alt="Screenshot 2026-01-04 163431" src="https://github.com/user-attachments/assets/8bc23537-9b53-4ae6-a8d3-65fd405ff39c" />

And here is the PCB :

<img width="660" height="660" alt="Screenshot 2026-01-02 011806" src="https://github.com/user-attachments/assets/a8461cec-bcdf-4b36-a993-cebdef009213" />
<img width="871" height="867" alt="Screenshot 2026-01-02 011838" src="https://github.com/user-attachments/assets/6e4a9c82-8797-483d-a66c-7c4f7abf843a" />

Everything will go inside this 3D Printed enclosure :

<img width="1134" height="734" alt="image" src="https://github.com/user-attachments/assets/87076ca6-1c53-4edc-81a9-068c1362f34d" />

It will be mounted using M3*16 screws and heatset inserts just like shown below :

<img width="740" height="722" alt="image" src="https://github.com/user-attachments/assets/432e06a5-3d43-4dc2-848b-dcd839849fb1" />

The bottom part of the enclosure will be printed in very thin white, or in transparent resin (if allowed), so that we can get the RGB underglow designed in the PCB.

The code is still untested, but I will test it as soon as I get my hands on the electronics, and correct the errors and do the mapping.

**BOM :**

1 SEED XIAO RP2040 (through-hole version)

13 MX switches

13 DSA Keycaps

1 EC11 Encoder

16 1N4148 Diodes

15 SK6812 Mini LEDs

1 0.91 inch 128*32 OLED Display

4 M3-16 screws

4 M3 heatset inserts





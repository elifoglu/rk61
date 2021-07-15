# RK61 Customizations

This repo contains my customizations for Royal Kludge RK61 keyboard (Turkish Q Layout). I use Ubuntu 20.04.

## Goals
- RK61 has some constraints. Since the arrow keys are located in the same place as the other important keys, it is necessary to constantly switch between the two layers. Therefore, I needed to fix this somehow.
- When using the keyboard, I want to move my hands as little as possible. It is much more ergonomic for me to position the arrow keys near the middle of the keyboard. I am going to use the arrow keys via a modifier key.

## Customizations
### Customizations on symbols/pc file
- Escape <=> Caps Lock
- Menu (R) => Hyper (L)
- Ctrl (R) => AltGr

My customized pc file is [here](pc). It should be replaced with the existing pc file in the `/usr/share/X11/xkb/symbols` directory.

These customizations are being applied automatically after every boot.

### Customizations with setxkbmap command
- AltGr => Ctrl (R)

By changing symbols/pc file, I was unable to remap AltGr key to Ctrl. So I found another way to achieve this:

`setxkbmap -option ctrl:ralt_rctrl`

To make this work on boot,
1. Open _Startup Applications_
2. Add this startup command: `/bin/bash -c "sleep 10&&setxkbmap -option ctrl:ralt_rctrl"`
([source](https://unix.stackexchange.com/questions/273735/how-to-make-xkb-settings-stick-after-restart))


### Customizations with Autokey
I have done lots of customizations using [Autokey](https://github.com/autokey/autoke,y). All of them are [here](link).


### Ubuntu Keyboard Shortcuts
I assigned some shortcuts to enhance usage:

- Ctrl + Space => Show the activities overview
- Super + Space => Switch windows
- Super + T => Launch terminal
- Super + E => Hide all windows
- Super + Ctrl + L => Lock screen
- Super + . => Volume up
- Super + Ç => Volume down
- Super + Ç => Volume mute/unmute
- Super + Ctrl + Ş => View split on left
- Super + Ctrl + , => View split on right

Also, these default shortcuts are disabled since they make trouble:

- Focus the active notification
- Show all applications
- Show the notification list
- Show the overview
- Switch to next input source
- Switch to previous input source

### Removing keycaps
Not wanting to move my hands too much, I removed some keycaps to force myself to use fewer keys. The removed keycaps are:

- Escape
- Tab
- Caps Lock
- Ctrl (L)
- Win (Super) (L)
- Alt
- Backspace
- Enter

Currently, my keyboard looks like this:

--- img will be here ---

## Problems
- On terminal, I am unable to use Enter using Super + W combination. It does nothing.
- When computer is locked, I am unable to use Enter using Super + W combination.
- When using the search module of Ubuntu, I cannot use any of the combinations done with Autokey.

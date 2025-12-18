# AXe Command Reference

Complete reference for all AXe CLI commands and options.

## Table of Contents

- [Touch & Gestures](#touch--gestures)
- [Gesture Presets](#gesture-presets)
- [Text Input](#text-input)
- [Hardware Buttons](#hardware-buttons)
- [Keyboard Control](#keyboard-control)
- [Video Streaming & Recording](#video-streaming--recording)
- [Accessibility & Information](#accessibility--information)
- [Global Options](#global-options)

## Touch & Gestures

### tap

Simulate a precise touch event at specific coordinates.

```bash
axe tap -x <x-coord> -y <y-coord> [options]
```

**Options:**
- `-x <number>` - X coordinate (required)
- `-y <number>` - Y coordinate (required)
- `--pre-delay <seconds>` - Wait before action (default: 0)
- `--post-delay <seconds>` - Wait after action (default: 0)
- `--udid <string>` - Simulator UDID (required)

**Examples:**
```bash
# Simple tap
axe tap -x 100 -y 200 --udid $UDID

# Tap with delays for animations
axe tap -x 150 -y 300 --pre-delay 0.5 --post-delay 1.0 --udid $UDID
```

### swipe

Perform a swipe gesture between two points.

```bash
axe swipe --start-x <x> --start-y <y> --end-x <x> --end-y <y> [options]
```

**Options:**
- `--start-x <number>` - Starting X coordinate (required)
- `--start-y <number>` - Starting Y coordinate (required)
- `--end-x <number>` - Ending X coordinate (required)
- `--end-y <number>` - Ending Y coordinate (required)
- `--duration <seconds>` - Duration of swipe (default: varies)
- `--delta <number>` - Step increment for swipe path
- `--udid <string>` - Simulator UDID (required)

**Examples:**
```bash
# Horizontal swipe
axe swipe --start-x 300 --start-y 200 --end-x 100 --end-y 200 --udid $UDID

# Slow vertical swipe
axe swipe --start-x 150 --start-y 400 --end-x 150 --end-y 100 --duration 1.5 --udid $UDID
```

### touch

Low-level touch control for custom touch sequences.

```bash
axe touch -x <x-coord> -y <y-coord> [--down] [--up] [options]
```

**Options:**
- `-x <number>` - X coordinate (required)
- `-y <number>` - Y coordinate (required)
- `--down` - Trigger touch down event
- `--up` - Trigger touch up event
- `--delay <seconds>` - Delay between down/up if both specified
- `--udid <string>` - Simulator UDID (required)

**Examples:**
```bash
# Touch down
axe touch -x 100 -y 200 --down --udid $UDID

# Touch up
axe touch -x 100 -y 200 --up --udid $UDID

# Complete touch with delay
axe touch -x 100 -y 200 --down --up --delay 0.5 --udid $UDID
```

## Gesture Presets

### gesture

Execute pre-configured common gestures.

```bash
axe gesture <preset> [options]
```

**Available Presets:**
- `scroll-up` - Scroll upward
- `scroll-down` - Scroll downward
- `scroll-left` - Scroll left
- `scroll-right` - Scroll right
- `swipe-from-left-edge` - Edge swipe from left
- `swipe-from-right-edge` - Edge swipe from right
- `swipe-from-top-edge` - Edge swipe from top
- `swipe-from-bottom-edge` - Edge swipe from bottom

**Options:**
- `--screen-width <pixels>` - Screen width for gesture calculation
- `--screen-height <pixels>` - Screen height for gesture calculation
- `--pre-delay <seconds>` - Wait before gesture (default: 0)
- `--post-delay <seconds>` - Wait after gesture (default: 0)
- `--udid <string>` - Simulator UDID (required)

**Examples:**
```bash
# Simple scroll
axe gesture scroll-down --udid $UDID

# Scroll with timing
axe gesture scroll-up --pre-delay 0.5 --post-delay 1.0 --udid $UDID

# Edge swipe (e.g., for navigation)
axe gesture swipe-from-left-edge --udid $UDID
```

## Text Input

### type

Input text with automatic shift key handling for uppercase and special characters.

```bash
axe type <text> [options]
# OR
axe type --stdin [options]
# OR
axe type --file <path> [options]
```

**Options:**
- `<text>` - Direct text input (first positional argument)
- `--stdin` - Read text from standard input
- `--file <path>` - Read text from file
- `--udid <string>` - Simulator UDID (required)

**Examples:**
```bash
# Direct text
axe type 'Hello World!' --udid $UDID

# From stdin
echo "Test message" | axe type --stdin --udid $UDID

# From file
axe type --file message.txt --udid $UDID
```

## Hardware Buttons

### button

Simulate hardware button presses.

```bash
axe button <button-name> [options]
```

**Available Buttons:**
- `home` - Home button
- `lock` - Lock/power button
- `side-button` - Side button
- `siri` - Siri button
- `apple-pay` - Apple Pay button

**Options:**
- `--duration <seconds>` - How long to hold button
- `--udid <string>` - Simulator UDID (required)

**Examples:**
```bash
# Press home button
axe button home --udid $UDID

# Long press lock button
axe button lock --duration 2.0 --udid $UDID

# Activate Siri
axe button siri --udid $UDID
```

## Keyboard Control

### key

Press a single HID keycode.

```bash
axe key <keycode> [options]
```

**Options:**
- `<keycode>` - HID keycode number (required)
- `--duration <seconds>` - How long to hold key
- `--udid <string>` - Simulator UDID (required)

**Examples:**
```bash
# Press specific key
axe key 40 --udid $UDID  # Return key

# Hold key
axe key 42 --duration 0.5 --udid $UDID  # Backspace
```

### key-sequence

Press multiple keys in sequence.

```bash
axe key-sequence --keycodes <code1,code2,...> [options]
```

**Options:**
- `--keycodes <list>` - Comma-separated HID keycodes (required)
- `--udid <string>` - Simulator UDID (required)

**Examples:**
```bash
# Multiple keys
axe key-sequence --keycodes 40,41,42 --udid $UDID
```

## Video Streaming & Recording

### stream-video

Stream real-time video from the simulator.

```bash
axe stream-video [options]
```

**Options:**
- `--fps <1-30>` - Frames per second (default: 10)
- `--format <type>` - Output format: `mjpeg`, `ffmpeg`, `raw`, `bgra`
- `--quality <0.0-1.0>` - Compression quality (higher = better)
- `--scale <factor>` - Scale output (e.g., 0.5 for half size)
- `--udid <string>` - Simulator UDID (required)

**Examples:**
```bash
# Stream to stdout
axe stream-video --udid $UDID --fps 30

# Pipe to ffmpeg for recording
axe stream-video --udid $UDID --fps 30 --format ffmpeg | \
  ffmpeg -f image2pipe -framerate 30 -i - output.mp4

# Lower quality stream
axe stream-video --udid $UDID --fps 15 --quality 0.5 --scale 0.5
```

### record-video

Directly record video to MP4 file.

```bash
axe record-video [options]
```

**Options:**
- `--fps <1-30>` - Frames per second (default: 10)
- `--quality <0.0-1.0>` - Compression quality
- `--scale <factor>` - Scale output
- `--output <path>` - Output file path (optional, auto-generated if not provided)
- `--udid <string>` - Simulator UDID (required)

**Examples:**
```bash
# Basic recording (press Ctrl+C to stop)
axe record-video --udid $UDID

# High quality recording
axe record-video --udid $UDID --fps 30 --quality 1.0 --output test.mp4

# Scaled down recording
axe record-video --udid $UDID --fps 15 --scale 0.5 --output demo.mp4
```

**Important:** Press Ctrl+C to finalize the MP4 file. The file path is printed to stdout.

## Accessibility & Information

### describe-ui

Extract accessibility information from the UI.

```bash
axe describe-ui [--point <x,y>] [options]
```

**Options:**
- `--point <x,y>` - Get element at specific coordinates (optional)
- `--udid <string>` - Simulator UDID (required)

**Examples:**
```bash
# Describe entire UI tree
axe describe-ui --udid $UDID

# Describe element at point
axe describe-ui --point 150,300 --udid $UDID
```

### list-simulators

List all available iOS simulators.

```bash
axe list-simulators
```

**Output:** Displays simulator names and UDIDs.

**Example:**
```bash
# Get available simulators
axe list-simulators

# Use with grep to find specific simulator
axe list-simulators | grep "iPhone 15"
```

## Global Options

All interactive commands support:

- `--udid <string>` - Simulator UDID (required for all commands except `list-simulators`)
- `--pre-delay <seconds>` - Wait before executing action (default: 0)
- `--post-delay <seconds>` - Wait after executing action (default: 0)

**Timing Strategy:**
- Use `--pre-delay` to wait for animations or transitions to complete
- Use `--post-delay` to allow UI to respond before next action
- Combine both for stable, reliable automation sequences

**UDID Management:**
```bash
# Get UDID and store in variable
UDID=$(axe list-simulators | grep "iPhone 15 Pro" | awk '{print $NF}')

# Use in commands
axe tap -x 100 -y 200 --udid $UDID
```

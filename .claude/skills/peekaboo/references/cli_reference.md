# Peekaboo CLI Reference

Complete reference for all Peekaboo CLI commands and options.

## Installation & Setup

```bash
# Install via Homebrew
brew install steipete/tap/peekaboo
```

**System Requirements:**
- macOS 15.0+ (Sequoia)
- Screen Recording + Accessibility permissions required

## Configuration Commands

### `peekaboo config`

Manage AI provider credentials and settings.

**Subcommands:**
- `init` - Initialize configuration interactively
- `show` - Display current configuration
- `add` - Add AI provider credentials
- `login` - Authenticate with AI providers
- `models` - List available AI models

**Examples:**
```bash
peekaboo config add
peekaboo config show
peekaboo config models
```

**Environment Variables:**
```bash
export PEEKABOO_AI_PROVIDERS="openai/gpt-5.1,anthropic/claude-opus-4"
```

## Screen Capture Commands

### `peekaboo see`

Capture UI with accessibility annotations and element IDs.

**Options:**
- `--app <name>` - Target specific application
- `--mode <screen|window>` - Capture mode (default: screen)
- `--retina` - Capture at 2x resolution
- `--json-output` - Output results as JSON

**Examples:**
```bash
peekaboo see --app Safari
peekaboo see --mode window --retina
peekaboo see --app "Visual Studio Code" --json-output
```

### `peekaboo image`

Capture screenshots with optional AI analysis.

**Options:**
- `--mode <screen|window|menu>` - What to capture
- `--retina` - Capture at 2x resolution
- `--analyze` - Run AI analysis on captured image
- `--path <file>` - Save location

**Examples:**
```bash
peekaboo image --mode screen --retina --path ~/Desktop/screen.png
peekaboo image --mode window --analyze
peekaboo image --mode menu --path menu.png
```

## Interaction Commands

### `peekaboo click`

Click UI elements by identifier or coordinates.

**Options:**
- `--on <id|query>` - Element identifier or search query
- `--snapshot <id>` - Use specific snapshot for element lookup
- `--wait <ms>` - Wait after clicking (milliseconds)

**Examples:**
```bash
peekaboo click --on "Reload this page"
peekaboo click --on button123 --snapshot snap_abc
peekaboo click --on "Submit" --wait 500
```

### `peekaboo type`

Input text into focused UI element.

**Options:**
- `--text <string>` - Text to type
- `--clear` - Clear field before typing
- `--delay-ms <ms>` - Delay between keystrokes

**Examples:**
```bash
peekaboo type --text "Hello World"
peekaboo type --text "user@example.com" --clear
peekaboo type --text "password123" --delay-ms 50
```

### `peekaboo press`

Press special keys or key sequences.

**Options:**
- Key names: `return`, `tab`, `escape`, `delete`, `space`, `up`, `down`, `left`, `right`
- `--repeat <n>` - Press key multiple times

**Examples:**
```bash
peekaboo press return
peekaboo press tab --repeat 3
peekaboo press escape
```

### `peekaboo hotkey`

Execute keyboard combinations with modifiers.

**Format:** `modifier1,modifier2,key`
**Modifiers:** `cmd`, `shift`, `ctrl`, `alt`/`option`

**Examples:**
```bash
peekaboo hotkey cmd,shift,t
peekaboo hotkey cmd,s
peekaboo hotkey ctrl,alt,delete
```

### `peekaboo scroll`

Scroll within UI elements.

**Options:**
- `--on <id>` - Element to scroll (defaults to current focus)
- `--direction <up|down>` - Scroll direction
- `--ticks <n>` - Number of scroll increments

**Examples:**
```bash
peekaboo scroll --direction down --ticks 5
peekaboo scroll --on scrollview123 --direction up
```

### `peekaboo swipe`

Perform gesture-based dragging motions.

**Options:**
- `--from <x,y>` - Starting coordinates
- `--to <x,y>` - Ending coordinates
- `--duration <ms>` - Duration of swipe
- `--steps <n>` - Number of intermediate points

**Examples:**
```bash
peekaboo swipe --from 100,200 --to 300,400
peekaboo swipe --from 500,500 --to 100,100 --duration 500
```

### `peekaboo drag`

Drag-and-drop operations.

**Options:**
- `--from <x,y|id>` - Starting position or element
- `--to <x,y|id>` - Ending position or element
- Modifiers: `--cmd`, `--shift`, `--ctrl`, `--alt`

**Examples:**
```bash
peekaboo drag --from 100,200 --to 300,400
peekaboo drag --from elem1 --to elem2
peekaboo drag --from 50,50 --to 200,200 --cmd
```

### `peekaboo move`

Move mouse cursor without clicking.

**Options:**
- `--to <x,y|id>` - Target position or element
- `--screen-index <n>` - Which display to use

**Examples:**
```bash
peekaboo move --to 500,500
peekaboo move --to button123
peekaboo move --to 100,100 --screen-index 1
```

## Window Management Commands

### `peekaboo window`

Control window positioning and sizing.

**Subcommands:**
- `list` - List all windows
- `move --x <n> --y <n>` - Move window to coordinates
- `resize --width <n> --height <n>` - Resize window
- `focus --app <name>` - Focus application window
- `set-bounds --x <n> --y <n> --width <n> --height <n>` - Set position and size

**Examples:**
```bash
peekaboo window list
peekaboo window move --x 100 --y 100
peekaboo window resize --width 800 --height 600
peekaboo window focus --app Safari
peekaboo window set-bounds --x 0 --y 0 --width 1920 --height 1080
```

## Application Management Commands

### `peekaboo app`

Control application lifecycle.

**Subcommands:**
- `launch <name>` - Launch application
- `quit <name>` - Quit application
- `relaunch <name>` - Quit and relaunch
- `switch <name>` - Switch to application
- `list` - List running applications

**Examples:**
```bash
peekaboo app launch Safari
peekaboo app quit "Google Chrome"
peekaboo app relaunch Terminal
peekaboo app switch "Visual Studio Code"
peekaboo app list
```

### `peekaboo space`

Navigate macOS Spaces (virtual desktops).

**Subcommands:**
- `list` - List all Spaces
- `switch <index>` - Switch to Space by index
- `move-window <index>` - Move current window to Space

**Examples:**
```bash
peekaboo space list
peekaboo space switch 2
peekaboo space move-window 3
```

## Menu & UI Commands

### `peekaboo menu`

Access application menus.

**Subcommands:**
- `list --app <name>` - List menu items for application
- `list-all --app <name>` - List all menu items recursively
- `click --app <name> --path "Menu > Item > Subitem"` - Click menu item
- `click-extra --app <name> --items <json>` - Click with extra options

**Examples:**
```bash
peekaboo menu list --app Safari
peekaboo menu list-all --app "Visual Studio Code"
peekaboo menu click --app Safari --path "File > New Window"
peekaboo menu click --app Terminal --path "Shell > New Window"
```

### `peekaboo menubar`

Interact with menu bar (status bar) items.

**Subcommands:**
- `list` - List menu bar items
- `click <identifier>` - Click menu bar item

**Examples:**
```bash
peekaboo menubar list
peekaboo menubar click "WiFi"
```

### `peekaboo dock`

Control macOS Dock operations.

**Subcommands:**
- `launch <app>` - Launch app from Dock
- `right-click <app>` - Right-click Dock item
- `hide` - Hide the Dock
- `show` - Show the Dock
- `list` - List Dock items

**Examples:**
```bash
peekaboo dock launch Safari
peekaboo dock right-click Terminal
peekaboo dock hide
peekaboo dock show
peekaboo dock list
```

### `peekaboo dialog`

Drive system dialogs.

**Subcommands:**
- `list` - List open dialogs
- `click <button>` - Click dialog button
- `input --text <string>` - Input text into dialog
- `file --path <path>` - Select file in file picker
- `dismiss` - Dismiss/close dialog

**Examples:**
```bash
peekaboo dialog list
peekaboo dialog click "OK"
peekaboo dialog input --text "filename.txt"
peekaboo dialog file --path "/Users/user/document.pdf"
peekaboo dialog dismiss
```

## Automation Commands

### `peekaboo run`

Execute automation workflows from `.peekaboo.json` files.

**Options:**
- `<file>` - Path to .peekaboo.json workflow file
- `--output <dir>` - Output directory for results
- `--no-fail-fast` - Continue on errors

**Workflow File Format:**
```json
{
  "name": "My Workflow",
  "steps": [
    {"action": "launch", "app": "Safari"},
    {"action": "type", "text": "https://example.com"},
    {"action": "press", "key": "return"}
  ]
}
```

**Examples:**
```bash
peekaboo run workflow.peekaboo.json
peekaboo run automation.peekaboo.json --output ./results
peekaboo run test.peekaboo.json --no-fail-fast
```

### `peekaboo agent`

Natural-language multi-step automation with AI.

**Options:**
- `<task>` - Natural language task description
- `--model <name>` - AI model to use
- `--dry-run` - Show planned steps without executing
- `--resume <id>` - Resume previous session
- `--max-steps <n>` - Maximum automation steps

**Examples:**
```bash
peekaboo agent "Open Notes and create a TODO list with three items"
peekaboo agent "Take a screenshot of Safari and save to Desktop" --dry-run
peekaboo agent "Organize my Desktop files" --model openai/gpt-5.1
peekaboo agent --resume session_abc123
```

**Shorthand:** Can omit `agent` keyword
```bash
peekaboo "Open Calculator and compute 15 * 23"
```

## Utility Commands

### `peekaboo list`

Enumerate system resources.

**Subcommands:**
- `apps` - List running applications
- `windows` - List all windows
- `screens` - List displays/screens
- `menubar` - List menu bar items
- `permissions` - List permission status

**Examples:**
```bash
peekaboo list apps
peekaboo list windows
peekaboo list screens
peekaboo list menubar
peekaboo list permissions
```

### `peekaboo permissions`

Check and grant macOS permissions.

**Subcommands:**
- `status` - Show current permission status
- `grant` - Request/grant permissions

**Examples:**
```bash
peekaboo permissions status
peekaboo permissions grant
```

### `peekaboo sleep`

Introduce delays in automation scripts.

**Options:**
- `--duration <ms>` - Sleep duration in milliseconds

**Examples:**
```bash
peekaboo sleep --duration 1000
peekaboo sleep --duration 500
```

### `peekaboo clean`

Remove cached snapshots.

**Options:**
- `--all-snapshots` - Remove all snapshots
- `--older-than <days>` - Remove snapshots older than N days
- `--snapshot <id>` - Remove specific snapshot

**Examples:**
```bash
peekaboo clean --all-snapshots
peekaboo clean --older-than 7
peekaboo clean --snapshot snap_abc123
```

## AI Model Support

Peekaboo integrates with multiple AI providers for vision and automation capabilities.

**Supported Providers:**
- **OpenAI:** gpt-5.1, gpt-4.1, gpt-4o
- **Anthropic:** claude-opus-4, claude-sonnet-4
- **xAI:** grok-4-fast
- **Google:** gemini-2.5-flash, gemini-2.5-pro
- **Local:** Ollama-compatible models

**Configuration:**
```bash
# Environment variable
export PEEKABOO_AI_PROVIDERS="openai/gpt-5.1,anthropic/claude-opus-4"

# CLI configuration
peekaboo config add
```

## Common Workflows

### Element-Based Clicking
```bash
# Capture UI with element IDs
peekaboo see --app Safari --json-output > output.json

# Extract snapshot ID
SNAPSHOT=$(jq -r '.data.snapshot_id' output.json)

# Click element by name
peekaboo click --on "Reload this page" --snapshot "$SNAPSHOT"
```

### Window Automation
```bash
# Launch app and position window
peekaboo app launch Safari
peekaboo sleep --duration 500
peekaboo window set-bounds --x 0 --y 0 --width 1920 --height 1080
```

### Screenshot Workflow
```bash
# Capture and analyze
peekaboo image --mode screen --retina --analyze --path screenshot.png
```

## Return Values & JSON Output

Commands that support `--json-output` return structured data:

```json
{
  "success": true,
  "data": {
    "snapshot_id": "snap_abc123",
    "elements": [...],
    "timestamp": "2025-12-18T12:00:00Z"
  }
}
```

## Error Handling

Peekaboo returns standard exit codes:
- `0` - Success
- `1` - General error
- `2` - Permission denied
- `3` - Invalid arguments

Check permissions if commands fail:
```bash
peekaboo permissions status
peekaboo permissions grant
```

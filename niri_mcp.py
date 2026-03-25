import json
import subprocess
from typing import Optional

from mcp.server.fastmcp import FastMCP

# Create the MCP server
mcp = FastMCP("NiriMCP")


@mcp.tool()
def get_windows() -> str:
    """Get a list of current Niri windows and their details as a JSON string."""
    try:
        result = subprocess.run(
            ["niri", "msg", "--json", "windows"],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error executing niri msg: {e.stderr}"


@mcp.tool()
def move_floating_window(window_id: int, x: str, y: str) -> str:
    """
    Move a floating window to an exact or relative location.
    x and y can be exact pixels (e.g., "1000") or relative (e.g., "+50", "-10").
    """
    try:
        cmd = [
            "niri",
            "msg",
            "action",
            "move-floating-window",
            "--x",
            str(x),
            "--y",
            str(y),
            "--id",
            str(window_id),
        ]
        subprocess.run(cmd, capture_output=True, text=True, check=True)
        return f"Successfully moved window {window_id} to x:{x}, y:{y}"
    except subprocess.CalledProcessError as e:
        return f"Error moving window: {e.stderr}"


@mcp.tool()
def set_window_width(width: str, window_id: Optional[int] = None) -> str:
    """
    Set the width of a window.
    width can be pixels (e.g. "800"), percentage (e.g. "50%"), or relative (e.g. "+50", "-50").
    """
    try:
        cmd = ["niri", "msg", "action", "set-window-width", width]
        if window_id is not None:
            cmd.extend(["--id", str(window_id)])
        subprocess.run(cmd, capture_output=True, text=True, check=True)
        return f"Successfully set window {window_id or 'focused'} width to {width}"
    except subprocess.CalledProcessError as e:
        return f"Error setting window width: {e.stderr}"


@mcp.tool()
def set_window_height(height: str, window_id: Optional[int] = None) -> str:
    """
    Set the height of a window.
    height can be pixels, percentage, or relative.
    """
    try:
        cmd = ["niri", "msg", "action", "set-window-height", height]
        if window_id is not None:
            cmd.extend(["--id", str(window_id)])
        subprocess.run(cmd, capture_output=True, text=True, check=True)
        return f"Successfully set window {window_id or 'focused'} height to {height}"
    except subprocess.CalledProcessError as e:
        return f"Error setting window height: {e.stderr}"


@mcp.tool()
def set_column_width(width: str, column_id: Optional[int] = None) -> str:
    """
    Set the width of a column.
    width can be pixels, percentage, or relative.
    """
    try:
        cmd = ["niri", "msg", "action", "set-column-width", width]
        if column_id is not None:
            cmd.extend(["--id", str(column_id)])
        subprocess.run(cmd, capture_output=True, text=True, check=True)
        return f"Successfully set column {column_id or 'focused'} width to {width}"
    except subprocess.CalledProcessError as e:
        return f"Error setting column width: {e.stderr}"


@mcp.tool()
def move_window_to_workspace(workspace: str, window_id: Optional[int] = None) -> str:
    """
    Move a window to a specific workspace by index or name.
    """
    try:
        cmd = ["niri", "msg", "action", "move-window-to-workspace", workspace]
        if window_id is not None:
            cmd.extend(["--window-id", str(window_id)])
        subprocess.run(cmd, capture_output=True, text=True, check=True)
        return f"Successfully moved window {window_id or 'focused'} to workspace {workspace}"
    except subprocess.CalledProcessError as e:
        return f"Error moving window to workspace: {e.stderr}"


@mcp.tool()
def move_column_to_workspace(workspace: str, column_id: Optional[int] = None) -> str:
    """
    Move a column to a specific workspace by index or name.
    """
    try:
        cmd = ["niri", "msg", "action", "move-column-to-workspace", workspace]
        if column_id is not None:
            cmd.extend(["--column-id", str(column_id)])
        subprocess.run(cmd, capture_output=True, text=True, check=True)
        return f"Successfully moved column {column_id or 'focused'} to workspace {workspace}"
    except subprocess.CalledProcessError as e:
        return f"Error moving column to workspace: {e.stderr}"


@mcp.tool()
def move_window_to_monitor(monitor: str, window_id: Optional[int] = None) -> str:
    """
    Move a window to a specific monitor by index or name.
    """
    try:
        cmd = ["niri", "msg", "action", "move-window-to-monitor", monitor]
        if window_id is not None:
            cmd.extend(["--window-id", str(window_id)])
        subprocess.run(cmd, capture_output=True, text=True, check=True)
        return (
            f"Successfully moved window {window_id or 'focused'} to monitor {monitor}"
        )
    except subprocess.CalledProcessError as e:
        return f"Error moving window to monitor: {e.stderr}"


@mcp.tool()
def move_column_to_index(index: int, column_id: Optional[int] = None) -> str:
    """
    Move a column to a specific index in the workspace.
    """
    try:
        cmd = ["niri", "msg", "action", "move-column-to-index", str(index)]
        if column_id is not None:
            cmd.extend(["--column-id", str(column_id)])
        subprocess.run(cmd, capture_output=True, text=True, check=True)
        return f"Successfully moved column {column_id or 'focused'} to index {index}"
    except subprocess.CalledProcessError as e:
        return f"Error moving column to index: {e.stderr}"


@mcp.tool()
def focus_window_action(action: str, window_id: Optional[int] = None) -> str:
    """
    Focus a window or window group.
    Valid actions: focus-window-previous, focus-window-up, focus-window-bottom, 
    focus-window-top, focus-window, focus-floating, focus-tiling, 
    switch-focus-between-floating-and-tiling.
    """
    valid_actions = {
        "focus-window-previous",
        "focus-window-up",
        "focus-window-bottom",
        "focus-window-top",
        "focus-window",
        "focus-floating",
        "focus-tiling",
        "switch-focus-between-floating-and-tiling",
    }
    if action not in valid_actions:
        return f"Error: Action '{action}' is not a valid focus action."
    return execute_niri_action(action, window_id)


@mcp.tool()
def move_window_action(action: str, window_id: Optional[int] = None) -> str:
    """
    Move a window (up, down, to floating/tiling, or between monitors/workspaces).
    Valid actions: move-window-down, move-window-up, move-window-to-floating, 
    move-window-to-tiling, toggle-window-floating, move-window-up-or-to-workspace-up, 
    move-window-down-or-to-workspace-down, move-window-to-monitor-right, 
    move-window-to-workspace-down, move-window-to-monitor-down, move-window-to-monitor-next, 
    move-window-to-monitor-up, move-window-to-workspace-up, move-window-to-monitor-left, 
    move-window-to-monitor-previous.
    """
    valid_actions = {
        "move-window-down",
        "move-window-up",
        "move-window-to-floating",
        "move-window-to-tiling",
        "toggle-window-floating",
        "move-window-up-or-to-workspace-up",
        "move-window-down-or-to-workspace-down",
        "move-window-to-monitor-right",
        "move-window-to-workspace-down",
        "move-window-to-monitor-down",
        "move-window-to-monitor-next",
        "move-window-to-monitor-up",
        "move-window-to-workspace-up",
        "move-window-to-monitor-left",
        "move-window-to-monitor-previous",
    }
    if action not in valid_actions:
        return f"Error: Action '{action}' is not a valid move action."
    return execute_niri_action(action, window_id)


@mcp.tool()
def move_column_action(action: str, column_id: Optional[int] = None) -> str:
    """
    Move a column left or right.
    Valid actions: move-column-right, move-column-left.
    """
    valid_actions = {"move-column-right", "move-column-left"}
    if action not in valid_actions:
        return f"Error: Action '{action}' is not a valid column movement action."
    return execute_niri_action(action, column_id)


@mcp.tool()
def layout_action(action: str, window_id: Optional[int] = None) -> str:
    """
    Change window/column layout (maximize, expand, reset, swap).
    Valid actions: maximize-column, maximize-window-to-edges, expand-column-to-available-width, 
    reset-window-height, swap-window-left.
    """
    valid_actions = {
        "maximize-column",
        "maximize-window-to-edges",
        "expand-column-to-available-width",
        "reset-window-height",
        "swap-window-left",
    }
    if action not in valid_actions:
        return f"Error: Action '{action}' is not a valid layout action."
    return execute_niri_action(action, window_id)


@mcp.tool()
def overview_action(action: str) -> str:
    """
    Control the Niri overview.
    Valid actions: toggle-overview, open-overview, close-overview.
    """
    valid_actions = {"toggle-overview", "open-overview", "close-overview"}
    if action not in valid_actions:
        return f"Error: Action '{action}' is not a valid overview action."
    return execute_niri_action(action)


@mcp.tool()
def close_window(window_id: Optional[int] = None) -> str:
    """Close a window by ID or the currently focused one."""
    return execute_niri_action("close-window", window_id)


def execute_niri_action(action: str, target_id: Optional[int] = None) -> str:
    """Helper to execute a niri action with an optional ID."""
    cmd = ["niri", "msg", "action", action]
    if target_id is not None:
        # Note: some actions use --id, some use --window-id or --column-id.
        # However, for 'msg action', many standard ones accept --id broadly.
        # But we should be careful. 'close-window' and 'focus-window' use --id.
        # 'move-column-left/right' might not take an ID in the same way.
        # Let's check the common pattern in the previous code.
        cmd.extend(["--id", str(target_id)])

    try:
        subprocess.run(cmd, capture_output=True, text=True, check=True)
        return f"Successfully executed '{action}'" + (
            f" on target {target_id}" if target_id else ""
        )
    except subprocess.CalledProcessError as e:
        return f"Error executing action '{action}': {e.stderr}"


if __name__ == "__main__":
    mcp.run()

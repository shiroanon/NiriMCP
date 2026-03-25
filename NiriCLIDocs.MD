
## Moving Floating windows to exact location on screen
`niri msg action move-floating-window --x 1000 --y 0 --id 25`

## Relative Positioning with (+) and (-)
`niri msg action move-floating-window --x +50 --y -10 --id 25`

### Get Current Windows info 
`niri msg --json  windows`

```json
[
  {
    "id": 25,
    "title": "NiriMCP - shiro - Obsidian 1.12.7",
    "app_id": "obsidian",
    "pid": 47714,
    "workspace_id": 2,
    "is_focused": false,
    "is_floating": false,
    "is_urgent": false,
    "layout": {
      "pos_in_scrolling_layout": [1, 1],
      "tile_size": [1862.0, 1021.0],
      "window_size": [1862, 1021],
      "tile_pos_in_workspace_view": null,
      "window_offset_in_tile": [0.0, 0.0]
    },
    "focus_timestamp": { "secs": 4280, "nanos": 107079245 }
  },
  {
    "id": 30,
    "title": "Picture-in-Picture",
    "app_id": "zen",
    "pid": 1832,
    "workspace_id": 2,
    "is_focused": false,
    "is_floating": true,
    "is_urgent": false,
    "layout": {
      "pos_in_scrolling_layout": null,
      "tile_size": [399.0, 205.0],
      "window_size": [399, 205],
      "tile_pos_in_workspace_view": [1418.0, 77.0],
      "window_offset_in_tile": [0.0, 0.0]
    },
    "focus_timestamp": { "secs": 4147, "nanos": 396602777 }
  },
  {
    "id": 29,
    "title": "niri msg --json win ~",
    "app_id": "kitty",
    "pid": 52067,
    "workspace_id": 2,
    "is_focused": true,
    "is_floating": false,
    "is_urgent": false,
    "layout": {
      "pos_in_scrolling_layout": [2, 1],
      "tile_size": [1521.0, 1021.0],
      "window_size": [1521, 1021],
      "tile_pos_in_workspace_view": null,
      "window_offset_in_tile": [0.0, 0.0]
    },
    "focus_timestamp": { "secs": 4282, "nanos": 383617664 }
  },
  {
    "id": 14,
    "title": "shiro - Thunar",
    "app_id": "thunar",
    "pid": 31381,
    "workspace_id": 1,
    "is_focused": false,
    "is_floating": false,
    "is_urgent": false,
    "layout": {
      "pos_in_scrolling_layout": [2, 2],
      "tile_size": [512.0, 506.0],
      "window_size": [512, 506],
      "tile_pos_in_workspace_view": null,
      "window_offset_in_tile": [0.0, 0.0]
    },
    "focus_timestamp": { "secs": 4048, "nanos": 423652039 }
  },
  {
    "id": 12,
    "title": "yt-dlp -a sun ~",
    "app_id": "kitty",
    "pid": 30968,
    "workspace_id": 1,
    "is_focused": false,
    "is_floating": false,
    "is_urgent": false,
    "layout": {
      "pos_in_scrolling_layout": [2, 1],
      "tile_size": [512.0, 507.0],
      "window_size": [512, 507],
      "tile_pos_in_workspace_view": null,
      "window_offset_in_tile": [0.0, 0.0]
    },
    "focus_timestamp": { "secs": 4091, "nanos": 930334173 }
  },
  {
    "id": 3,
    "title": "Is This The GREATEST In-Camera Effect of ALL TIME? - YouTube — Zen Browser",
    "app_id": "zen",
    "pid": 1832,
    "workspace_id": 1,
    "is_focused": false,
    "is_floating": false,
    "is_urgent": false,
    "layout": {
      "pos_in_scrolling_layout": [1, 1],
      "tile_size": [1330.0, 1021.0],
      "window_size": [1330, 1021],
      "tile_pos_in_workspace_view": null,
      "window_offset_in_tile": [0.0, 0.0]
    },
    "focus_timestamp": { "secs": 4117, "nanos": 66073359 }
  },
  {
    "id": 24,
    "title": "Projects - Thunar",
    "app_id": "thunar",
    "pid": 31381,
    "workspace_id": 1,
    "is_focused": false,
    "is_floating": false,
    "is_urgent": false,
    "layout": {
      "pos_in_scrolling_layout": [3, 1],
      "tile_size": [948.0, 1021.0],
      "window_size": [948, 1021],
      "tile_pos_in_workspace_view": null,
      "window_offset_in_tile": [0.0, 0.0]
    },
    "focus_timestamp": { "secs": 3943, "nanos": 570797859 }
  }
]

```

## Things we can do

## Focus Window 

``` bash
 'focus-window-previous', 'focus-window-bottom',  'focus-window-up',  'focus-window', 'focus-window-top', 'swap-window-left',  'reset-window-height',  'close-window', 
```



## Move Window Tiling

```shell
'move-column-right', 'move-column-to-index',  'move-column-left', 'move-window-to-workspace', 'move-window-down', 'move-window-to-floating', 'move-window-up',
```

## Move Windows Floating

```bash
'move-window-to-tiling' ,'move-floating-window'
``` 


## Both
```bash
 'move-window-up-or-to-workspace-up','move-window-to-monitor-right', 'move-window-to-workspace-down', 'move-window-to-monitor-down', 'move-window-to-monitor-next', 'move-window-to-monitor-up'
 'move-window-to-workspace-up', 'move-window-to-monitor' , 'move-window-to-monitor-left', 'move-window-to-monitor-previous','move-window-down-or-to-workspace-down'
```

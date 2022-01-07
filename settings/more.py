from .vars import os

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True

wmname = "LG3D"
cmd = [
    "nitrogen --restore",
    "picom &"
]

for x in cmd:
    os.system(x)

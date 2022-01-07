from .vars import Screen, bar, widget, colors

screens = [
    Screen(
            top=bar.Bar(
                [
                    widget.GroupBox(
                           fontsize = 10,
                           margin_y = 3,
                           margin_x = 0,
                           padding_y = 5,
                           padding_x = 5,
                           borderwidth = 3,
                           active = "#ffffff",
                           inactive = "#6679a4",
                           rounded = False,
                           this_current_screen_border = "#ffee00",
                           highlight_method = "line",
                           highlight_color = "#2f3b54",
                           background = colors[2]
                           ),
                    widget.WindowName(
                            foreground = "#ffffff",
                            padding = 6
                            ),
                    widget.Net(
                           format = ' {down} ↓↑ {up} ',
                           foreground = "#ffffff",
                           background = "#2f3b54",
                           padding = 5
                           ),
                    widget.ThermalSensor(
                           foreground = colors[2],
                           background = "#c3a6ff",
                           threshold = 90,
                           padding = 5
                           ),
                    widget.Clock(
                           foreground = colors[2],
                           background = "#ffee00",
                           format = " %d/%m/%Y - %H:%M  "
                           ),
                    widget.TextBox(
                            text = '  : ',
                            background= "ffcc66",
                            foreground = colors[2],
                    ),
                    widget.PulseVolume(
                            limit_max_volume = True,
                            background= "ffcc66",
                            foreground = colors[2],
                    ),
                    widget.TextBox(
                            background= "ffcc66",
                            foreground = colors[2],
                    ),
                    widget.Battery(
                        battery=0 + 1,
                        charge_char=' ',
                        discharge_char=' ',
                        unknown_char='',
                        format=" {percent:2.0%} {char}",
                        low_percentage=0.2,
                        notify_below=20,
                        update_interval=10,
                        background="#2f3b54"
                    ),
                    widget.Wlan(
                        interface="wlp5s0",
                        format="   {essid}",
                        disconnected_message="offline",
                    ),
                   #widget.CurrentLayout(),
                ],
                20,
                background = colors[0],
                opacity = 1
            ),
        ),
    ]

def on_button_pressed_a():
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                # # . # .
                # # # # #
    """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                # . # . .
                # # # # .
    """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . # . . .
                # # # . .
    """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                # . . . .
                # # . . .
    """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                # . . . .
    """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
                . . . . .
                # . # . #
                # . # . #
                # . # . #
    """)
    basic.pause(100)
    basic.show_leds("""
        # # # # #
                . . . . .
                # # # # #
                . . . . .
                # # # # #
    """)
    basic.pause(100)
    basic.show_leds("""
        . . . # #
                # . . . .
                # # . # #
                # . . . .
                # # . # #
    """)
    basic.pause(100)
    basic.show_leds("""
        . . . # #
                # . . . .
                # # . # #
                # . . . .
                . # . # #
    """)
    basic.pause(100)
    basic.show_leds("""
        . . # # #
                . . . . .
                # . # # #
                . . . . .
                # . # # #
    """)
    basic.pause(100)
    basic.show_leds("""
        . # # # #
                . . . . .
                . # # # #
                . . . . .
                . # # # #
    """)
    basic.pause(100)
    basic.show_leds("""
        # # # # #
                . . . . .
                # # # # #
                . . . . .
                # # # # #
    """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
                . # . # .
                . . . . .
                # . . . #
                . # # # .
    """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
                . # . # .
                . . . . .
                . . . . .
                # # # # #
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.show_string("You Died")
    basic.show_string("Game Over")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_leds("""
    # # . . .
        # # . # #
        . # . # .
        . # # # .
        . . . . .
""")
basic.pause(1000)
basic.show_leds("""
    . . . # #
        . . # # #
        . . . # #
        # # . . #
        # # . . #
""")
basic.pause(1000)
basic.show_leds("""
    . # # . #
        . # . # #
        . # . . #
        # # . . #
        . . . . #
""")
basic.pause(1000)
basic.show_leds("""
    . # # . #
        # # . # #
        # # . . #
        . . . . #
        . . . . #
""")
basic.pause(1000)
basic.show_leds("""
    . # # . #
        . # . # #
        # # . . #
        # # . . #
        . . . . #
""")
basic.pause(1000)
basic.show_leds("""
    . # # . #
        . # . # #
        . # . . #
        # # . . #
        # # . . #
""")
basic.pause(1000)
basic.show_leds("""
    . . . . .
        . . . . .
        . . . . .
        # # . # .
        # # # # #
""")
basic.pause(1000)
basic.show_leds("""
    . . . . .
        . # . . .
        # # # . .
        . # . . .
        # # # . #
""")
basic.pause(1000)
basic.show_leds("""
    . . . . .
        . # . . .
        # # # . .
        . # . # #
        # # . # #
""")
basic.pause(1000)
basic.show_leds("""
    . . . . .
        . . . . .
        . . . . .
        . # # . .
        . # # # #
""")
basic.pause(1000)
basic.show_leds("""
    . . . . .
        . . . . .
        . . . . .
        . . . # #
        . . . # #
""")
basic.pause(1000)
basic.show_leds("""
    . . . . .
        . . . . .
        . . . . .
        . . # # .
        . . # # #
""")
basic.pause(1000)
basic.show_leds("""
    . . . . .
        . . . . .
        . . . . .
        . # # . .
        . # # # #
""")
basic.pause(1000)
basic.show_leds("""
    . . . . .
        . . . . .
        . . . . .
        # # . # .
        # # # # #
""")
basic.pause(1000)
basic.show_leds("""
    # # # # #
        . . . . .
        # # . . .
        . # . # .
        # # # # #
""")
basic.pause(1000)
basic.show_leds("""
    . . . . .
        # # . . .
        # # . # #
        . # . # .
        . # # # .
""")
basic.pause(1000)
basic.show_leds("""
    # . . . #
        # # . . #
        # . # . #
        # . . # #
        # . . . #
""")
basic.pause(1000)
basic.show_leds("""
    . # # # .
        . # . # .
        . # . # .
        . # . # .
        . # # # .
""")
basic.pause(1000)
basic.show_leds("""
    . # # # .
        . # . # .
        . # . # .
        . # . # .
        . # # # .
""")
basic.pause(1000)
basic.show_leds("""
    . # # # .
        . # . # .
        . # . # .
        . # . # .
        . # # # .
""")
basic.pause(1000)
basic.show_leds("""
    . # # # .
        . # . # .
        . # . # .
        . # . # .
        . # # # .
""")
basic.pause(1000)
basic.show_leds("""
    . # # # .
        . # . # .
        . # . # .
        . # . # .
        . # # # .
""")
basic.pause(1000)
basic.show_leds("""
    . # # # .
        . # . # .
        . # . # .
        . # . # .
        . # # # .
""")
basic.pause(1000)
basic.show_leds("""
    . # # # .
        . # . # .
        . # . # .
        . # . # .
        . # # # .
""")
basic.pause(1000)
basic.show_leds("""
    . . . . .
        . . # . .
        . # # # .
        . . # . .
        . # # # .
""")
basic.pause(1000)
basic.show_leds("""
    . . . . .
        . . # . .
        . # # # .
        . . # . .
        . # . # .
""")
basic.pause(1000)
basic.show_leds("""
    # # . . .
        # # . # #
        . # . # .
        . # # # .
        . . . . .
""")
basic.pause(1000)
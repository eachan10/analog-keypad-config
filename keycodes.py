"""
All the tkinter.Event.keysym_num for single keys mapped to HID keycodes
"""

# maps keysym to hid keycode
KEYCODE = {
    # Alphabet
    65: 0x04,  # A
    66: 0x05,  # B
    67: 0x06,  # C
    68: 0x07,  # D
    69: 0x08,  # E
    70: 0x09,  # F
    71: 0x0a,  # G
    72: 0x0b,  # H
    73: 0x0c,  # I
    74: 0x0d,  # J
    75: 0x0e,  # K
    76: 0x0f,  # L
    77: 0x10,  # M
    78: 0x11,  # N
    79: 0x12,  # O
    80: 0x13,  # P
    81: 0x14,  # Q
    82: 0x15,  # R
    83: 0x16,  # S
    84: 0x17,  # T
    85: 0x18,  # U
    86: 0x19,  # V
    87: 0x1a,  # W
    88: 0x1b,  # X
    89: 0x1c,  # Y
    90: 0x1d,  # Z
    # lower and uppercase no difference
    97: 0x04,   # a
    98: 0x05,   # b
    99: 0x06,   # c
    100: 0x07,  # d
    101: 0x08,  # e
    102: 0x09,  # f
    103: 0x0a,  # g
    104: 0x0b,  # h
    105: 0x0c,  # i
    106: 0x0d,  # j
    107: 0x0e,  # k
    108: 0x0f,  # l
    109: 0x10,  # m
    110: 0x11,  # n
    111: 0x12,  # o
    112: 0x13,  # p
    113: 0x14,  # q
    114: 0x15,  # r
    115: 0x16,  # s
    116: 0x17,  # t
    117: 0x18,  # u
    118: 0x19,  # v
    119: 0x1a,  # w
    120: 0x1b,  # x
    121: 0x1c,  # y
    122: 0x1d,  # z
    # digits
    49: 0x1e,  # 1
    50: 0x1f,  # 2
    51: 0x20,  # 3
    52: 0x21,  # 4
    53: 0x22,  # 5
    54: 0x23,  # 6
    55: 0x24,  # 7
    56: 0x25,  # 8
    57: 0x26,  # 9
    48: 0x27,  # 0
    # idk what to call these
    65293: 0x28,  # Enter
    65307: 0x29,  # Escape
    65288: 0x2a,  # Backspace
    65289: 0x2b,  # Tab
    32: 0x2c,  # Space
    45: 0x2d,  # Minus
    61: 0x2e,  # Equal
    91: 0x2f,  # Bracket Left
    93: 0x30,  # Bracket Right
    92: 0x31,  # Backslash
    65509: 0x32,  # Europe 1
    59: 0x33,  # Semicolon
    39: 0x34,  # Apostrophe
    96: 0x35,  # Grave
    44: 0x36,  # Comma
    46: 0x37,  # Period
    47: 0x38,  # Slash
    65509: 0x39,  # Caps Lock

    65470: 0x3a,  # F1
    65471: 0x3b,  # F2
    65472: 0x3c,  # F3
    65473: 0x3d,  # F4
    65474: 0x3e,  # F5
    65475: 0x3f,  # F6
    65476: 0x40,  # F7
    65477: 0x41,  # F8
    65478: 0x42,  # F9
    65479: 0x43,  # F10
    0: 0x44,  # F11
    0: 0x45,  # F12

    0: 0x46,  # Print Screen
    0: 0x47,  # Scroll Lock
    0: 0x48,  # Pause

    65379: 0x49,  # Insert
    65360: 0x4a,  # Home
    65365: 0x4b,  # Page Up
    65535: 0x4c,  # Delete
    65367: 0x4d,  # End
    65366: 0x4e,  # Page Down
    65363: 0x4f,  # Arrow Right
    65361: 0x50,  # Arrow Left
    65364: 0x51,  # Arrow Down
    65362: 0x52,  # Arrow Up
    0: 0x53,  # Numlock
    # keypad
    0: 0x54,  # Keypad Divide
    0: 0x55,  # Keypad Multiply
    0: 0x56,  # Keypad Subtract
    0: 0x57,  # Keypad Add
    0: 0x58,  # Keypad Enter
    0: 0x59,  # Keypad 1
    0: 0x5a,  # Keypad 2
    0: 0x5b,  # Keypad 3
    0: 0x5c,  # Keypad 4
    0: 0x5d,  # Keypad 5
    0: 0x5e,  # Keypad 6
    0: 0x5f,  # Keypad 7
    0: 0x60,  # Keypad 8
    0: 0x61,  # Keypad 9
    0: 0x62,  # Keypad 0
    0: 0x63,  # Keypad Decimal

    0: 0x64,  # Europe 2
    0: 0x65,  # Application
    0: 0x66,  # Power

    0: 0x67,  # Keypad Equal

    0: 0x68,  # F13
    0: 0x69,  # F14
    0: 0x6a,  # F15
    0: 0x6b,  # F16
    0: 0x6c,  # F17
    0: 0x6d,  # F18
    0: 0x6e,  # F19
    0: 0x6f,  # F20
    0: 0x70,  # F21
    0: 0x71,  # F22
    0: 0x72,  # F23
    0: 0x73,  # F24

    0: 0x74,  # Execute
    0: 0x75,  # Help
    0: 0x76,  # Menu
    0: 0x77,  # Select
    0: 0x78,  # Stop
    0: 0x79,  # Again
    0: 0x7a,  # Undo
    0: 0x7b,  # Cut
    0: 0x7c,  # Copy
    0: 0x7d,  # Paste
    0: 0x7e,  # Find
    0: 0x7f,  # Mute
    0: 0x80,  # Volume Up
    0: 0x81,  # Volume Down
    0: 0x82,  # Locking Caps Lock
    0: 0x83,  # Locking Num Lock
    0: 0x84,  # Locking Scroll Lock
    0: 0x85,  # Keypad Comma
    0: 0x86,  # Keypad Equal Sign
    0: 0x87,  # Kanji 1
    0: 0x88,  # Kanji 2
    0: 0x89,  # Kanji 3
    0: 0x8a,  # Kanji 4
    0: 0x8b,  # Kanji 5
    0: 0x8c,  # Kanji 6
    0: 0x8d,  # Kanji 7
    0: 0x8e,  # Kanji 8
    0: 0x8f,  # Kanji 9
    0: 0x90,  # Lang 1
    0: 0x91,  # Lang 2
    0: 0x92,  # Lang 3
    0: 0x93,  # Lang 4
    0: 0x94,  # Lang 5
    0: 0x95,  # Lang 6
    0: 0x96,  # Lang 7
    0: 0x97,  # Lang 8
    0: 0x98,  # Lang 9
    0: 0x99,  # Alternate Erase
    0: 0x9a,  # Sysreq Attention
    0: 0x9b,  # Cancel
    0: 0x9c,  # Clear
    0: 0x9d,  # Prior
    0: 0x9e,  # Return
    0: 0x9f,  # Separator
    0: 0xa0,  # Out
    0: 0xa1,  # Oper
    0: 0xa2,  # Clear Again
    0: 0xa3,  # Crsel Props
    0: 0xa4,  # Exsel
    # Reserved 0xa5=df
    65507: 0xe0,  # Control_L
    65505: 0xe1,  # Shift_L
    65513: 0xe2,  # Alt_L
    0: 0xe3,  # Gui Left
    65508: 0xe4,  # Control_R
    65506: 0xe5,  # Shift_R
    65514: 0xe6,  # Alt_R
    0: 0xe7,  # Gui Right
}
del KEYCODE[0]

# maps hidcode to keysym
KEYSYM = {
    # Alphabet
    0x04: "a",
    0x05: "b",
    0x06: "c",
    0x07: "d",
    0x08: "e",
    0x09: "f",
    0x0a: "g",
    0x0b: "h",
    0x0c: "i",
    0x0d: "j",
    0x0e: "k",
    0x0f: "l",
    0x10: "m",
    0x11: "n",
    0x12: "o",
    0x13: "p",
    0x14: "q",
    0x15: "r",
    0x16: "s",
    0x17: "t",
    0x18: "u",
    0x19: "v",
    0x1a: "w",
    0x1b: "x",
    0x1c: "y",
    0x1d: "z",
    # digits
    0x1e: "1",
    0x1f: "2",
    0x20: "3",
    0x21: "4",
    0x22: "5",
    0x23: "6",
    0x24: "7",
    0x25: "8",
    0x26: "9",
    0x27: "0",
    # idk what to call these
    0x28: "Enter",
    0x29: "Escape",
    0x2a: "Backspace",
    0x2b: "Tab",
    0x2c: "Space",
    0x2d: "Minus",
    0x2e: "Equal",
    0x2f: "Bracket Left",
    0x30: "Bracket Right",
    0x31: "Backslash",
    0x32: "Europe 1",
    0x33: "Semicolon",
    0x34: "Apostrophe",
    0x35: "Grave",
    0x36: "Comma",
    0x37: "Period",
    0x38: "Slash",
    0x39: "Caps Lock",

    0x3a: "F1",
    0x3b: "F2",
    0x3c: "F3",
    0x3d: "F4",
    0x3e: "F5",
    0x3f: "F6",
    0x40: "F7",
    0x41: "F8",
    0x42: "F9",
    0x43: "F10",
    0: 0x44,  # F11
    0: 0x45,  # F12

    0: 0x46,  # Print Screen
    0: 0x47,  # Scroll Lock
    0: 0x48,  # Pause

    0x49: "Insert",
    0x4a: "Home",
    
    0x4b: "Page Up",
    0x4c: "Delete",
    0x4d: "End",
    0x4e: "Page Down",
    0x4f: "Arrow Right",
    0x50: "Arrow Left",
    0x51: "Arrow Down",
    0x52: "Arrow Up",
    0: 0x53,  # Numlock
    # keypad
    0: 0x54,  # Keypad Divide
    0: 0x55,  # Keypad Multiply
    0: 0x56,  # Keypad Subtract
    0: 0x57,  # Keypad Add
    0: 0x58,  # Keypad Enter
    0: 0x59,  # Keypad 1
    0: 0x5a,  # Keypad 2
    0: 0x5b,  # Keypad 3
    0: 0x5c,  # Keypad 4
    0: 0x5d,  # Keypad 5
    0: 0x5e,  # Keypad 6
    0: 0x5f,  # Keypad 7
    0: 0x60,  # Keypad 8
    0: 0x61,  # Keypad 9
    0: 0x62,  # Keypad 0
    0: 0x63,  # Keypad Decimal

    0: 0x64,  # Europe 2
    0: 0x65,  # Application
    0: 0x66,  # Power

    0: 0x67,  # Keypad Equal

    0: 0x68,  # F13
    0: 0x69,  # F14
    0: 0x6a,  # F15
    0: 0x6b,  # F16
    0: 0x6c,  # F17
    0: 0x6d,  # F18
    0: 0x6e,  # F19
    0: 0x6f,  # F20
    0: 0x70,  # F21
    0: 0x71,  # F22
    0: 0x72,  # F23
    0: 0x73,  # F24

    0: 0x74,  # Execute
    0: 0x75,  # Help
    0: 0x76,  # Menu
    0: 0x77,  # Select
    0: 0x78,  # Stop
    0: 0x79,  # Again
    0: 0x7a,  # Undo
    0: 0x7b,  # Cut
    0: 0x7c,  # Copy
    0: 0x7d,  # Paste
    0: 0x7e,  # Find
    0: 0x7f,  # Mute
    0: 0x80,  # Volume Up
    0: 0x81,  # Volume Down
    0: 0x82,  # Locking Caps Lock
    0: 0x83,  # Locking Num Lock
    0: 0x84,  # Locking Scroll Lock
    0: 0x85,  # Keypad Comma
    0: 0x86,  # Keypad Equal Sign
    0: 0x87,  # Kanji 1
    0: 0x88,  # Kanji 2
    0: 0x89,  # Kanji 3
    0: 0x8a,  # Kanji 4
    0: 0x8b,  # Kanji 5
    0: 0x8c,  # Kanji 6
    0: 0x8d,  # Kanji 7
    0: 0x8e,  # Kanji 8
    0: 0x8f,  # Kanji 9
    0: 0x90,  # Lang 1
    0: 0x91,  # Lang 2
    0: 0x92,  # Lang 3
    0: 0x93,  # Lang 4
    0: 0x94,  # Lang 5
    0: 0x95,  # Lang 6
    0: 0x96,  # Lang 7
    0: 0x97,  # Lang 8
    0: 0x98,  # Lang 9
    0: 0x99,  # Alternate Erase
    0: 0x9a,  # Sysreq Attention
    0: 0x9b,  # Cancel
    0: 0x9c,  # Clear
    0: 0x9d,  # Prior
    0: 0x9e,  # Return
    0: 0x9f,  # Separator
    0: 0xa0,  # Out
    0: 0xa1,  # Oper
    0: 0xa2,  # Clear Again
    0: 0xa3,  # Crsel Props
    0: 0xa4,  # Exsel
    # Reserved 0xa5=df
    0xe0: "Control_L",
    0xe1: "Shift_L",
    0xe2: "Alt_L",
    0: 0xe3,  # Gui Left
    0xe4: "Control_R",
    0xe5: "Shift_R",
    0xe6: "Alt_R",
    0: 0xe7,  # Gui Right
}
del KEYSYM[0]
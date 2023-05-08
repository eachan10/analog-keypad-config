import json
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import hid
import enum

from keycodes import KEYCODE, KEYSYM


ADC_VALUE_SIZE = 4   # bytes in adc reading
IO_ITF = 1           # interface number for the io with keypad


class State(enum.Enum):
    DEFAULT = 1
    CONFIG_KEY_LEFT = 2
    CONFIG_KEY_RIGHT = 3

class ConfigWindow(tk.Frame):
    """App that allows user to configure keys on keypad"""
    VID = 0xCAFE

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._init_widgets()

        self.state = State.DEFAULT

        self._hid_l = None
        self._hid_r = None

        self.bind("<KeyPress>", self._key_press_handler)

    def set_device_path(self, path: str) -> None:
        """Set the path to the usb device"""
        self._dev_path = path
    
    @property
    def config(self) -> dict:
        """Conifg as dict"""
        config = {
            "hid_l": self._hid_l,
            "hid_r": self._hid_r,
            "threshold": self._threshold_slider.get(),
            "reset": self._reset_slider.get(),
        }
        return config
    
    def set_config(self, config: dict) -> bool:
        """Configure from a dict returns whether dict was valid"""
        hid_l = config.pop("hid_l", None)
        k_l = KEYSYM.get(hid_l, None)
        if hid_l is None or k_l is None:
            return False

        hid_r = config.pop("hid_r", None)
        k_r = KEYSYM.get(hid_r, None)
        if hid_r is None or k_r is None:
            return False
        
        threshold = config.pop("threshold", None)
        if threshold is None or type(threshold) is not int or threshold > 90 or threshold < 0:
            return False

        reset = config.pop("reset", None)
        if reset is None or type(reset) is not int or reset < 2 or reset > 80:
            return False

        self._hid_l = hid_l
        self._hid_r = hid_r
        self._threshold_slider.set(threshold)
        self._reset_slider.set(reset)
        self._submit()
        return True

        
    
    def _init_widgets(self) -> None:
        # --------------------------------------------
        # Key config
        # --------------------------------------------
        self._keys_frame = tk.Frame(self, width=100, height=30)
        self._k_l_label = tk.Label(self._keys_frame, text="Left Key:")
        self._k_r_label = tk.Label(self._keys_frame, text="Right Key:")
        self._k_l = tk.Label(self._keys_frame, width=20, relief=tk.SUNKEN, text="(Empty)")
        self._k_r = tk.Label(self._keys_frame, width=20, relief=tk.SUNKEN, text="(Empty)")
        self._submit_keys_button = tk.Button(self._keys_frame, text="Submit", command=self._submit_key_changes)

        self._keys_frame.grid(column=0, row=0, columnspan=2, sticky=tk.W+tk.E+tk.N+tk.S)
        self._k_l_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self._k_r_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self._k_l.grid(row=0, column=1, padx=5, pady=5)
        self._k_r.grid(row=1, column=1, padx=5, pady=5)

        self._k_l.bind("<Button-1>", self._button_l_callback)
        self._k_r.bind("<Button-1>", self._button_r_callback)

        # --------------------------------------------
        # Theshold config
        # --------------------------------------------
        self._threshold_frame = tk.Frame(self)
        self._threshold_label = tk.Label(self._threshold_frame, text="Actuation threshold")
        self._submit_threshold_button = tk.Button(self._threshold_frame, text="Submit", command=self._submit_threshold_changes)
        self._threshold_slider = tk.Scale(self._threshold_frame, from_=90, to_=0, orient=tk.VERTICAL)

        self._threshold_frame.grid(row=1, column=0)
        self._threshold_label.grid(row=0, column=0, columnspan=2)
        self._threshold_slider.grid(row=1, column=0, rowspan=2)

        # --------------------------------------------
        # Reset config
        # --------------------------------------------
        self._reset_frame = tk.Frame(self)
        self._reset_label = tk.Label(self._reset_frame, text="Reset distance")
        self._submit_reset_button = tk.Button(self._reset_frame, text="Submit", command=self._submit_reset_distance_changes)
        self._reset_slider = tk.Scale(self._reset_frame, from_=80, to_=2, orient=tk.VERTICAL)

        self._reset_frame.grid(row=1, column=1)
        self._reset_label.grid(row=0, column=0, columnspan=2)
        self._reset_slider.grid(row=1, column=0, rowspan=2)

        # --------------------------------------------
        # Max/Min config
        # --------------------------------------------
        self._max_config_button = tk.Button(self, text="Config Max", command=self._submit_max_changes)
        self._min_config_button = tk.Button(self, text="Config Min", command=self._submit_min_changes)

        self._max_config_button.grid(row=2, column=0)
        self._min_config_button.grid(row=2, column=1)

        # --------------------------------------------
        # Get Config
        # --------------------------------------------
        self._get_config_button = tk.Button(self, text="Load Configuration Options", command=self.get_config)
        self._get_config_button.grid(row=3, column=0)

        # --------------------------------------------
        # Submit Button
        # --------------------------------------------
        self._submit_button = tk.Button(self, text="Apply Changes", command=self._submit)
        self._submit_button.grid(row=3, column=1)

        # --------------------------------------------
        # Min and Max ADC values
        # --------------------------------------------
        self._min_max_label = tk.Label(self)
        self._min_max_label.grid(row=4, column=0, columnspan=3)

    def _key_press_handler(self, event: tk.Event) -> None:
        if self.state in (State.CONFIG_KEY_LEFT, State.CONFIG_KEY_RIGHT):
            keysym, hid_keycode = _get_key(event)
            if hid_keycode is None:
                keysym = f"(Empty)"
                messagebox.showerror("Error", f"Key {keysym} has no corresponding HID keycode.")
            if self.state == State.CONFIG_KEY_LEFT:
                self._k_l.config(text=keysym)
                self._hid_l = hid_keycode
            elif self.state == State.CONFIG_KEY_RIGHT:
                self._k_r.config(text=keysym)
                self._hid_r = hid_keycode
            self.state = State.DEFAULT
    
    def _button_l_callback(self, e) -> None:
        if self.state != State.DEFAULT:
            return
        self.state = State.CONFIG_KEY_LEFT
        self._k_l.config(text="Press a key...")

    def _button_r_callback(self, e) -> None:
        if self.state != State.DEFAULT:
            return
        self.state = State.CONFIG_KEY_RIGHT
        self._k_r.config(text="Press a key...")

    def _submit_key_changes(self) -> bool:
        if self._hid_l is None or self._hid_r is None:
            messagebox.showerror("Error", "Set both keys first.")
            return False
        ep = b'\x00'
        msg = b'\x12' + self._hid_l.to_bytes() + self._hid_r.to_bytes() + b'\x00' * 13
        return self._submit_change(ep, msg)

    def _submit_threshold_changes(self) -> bool:
        ep = b'\x00'
        msg = b'\x13' + self._threshold_slider.get().to_bytes(1) + b'\x00' * 14
        return self._submit_change(ep, msg)
    
    def _submit_reset_distance_changes(self) -> bool:
        ep = b'\x00'
        msg = b'\x14' + self._reset_slider.get().to_bytes(1) + b'\x00' * 14
        return self._submit_change(ep, msg)

    def _submit(self) -> None:
        key_changed = self._submit_key_changes()
        threshold_changed = self._submit_threshold_changes()
        reset_changed = self._submit_reset_distance_changes()
        if all([key_changed, threshold_changed, reset_changed]):  # success
            return
        failed = ""
        if not key_changed:
            failed = "    - Key changes\n"
        if not threshold_changed:
            failed = f"{failed}    - Threshold change\n"
        if not reset_changed:
            failed = f"{failed}    - Reset gap change\n"
        msg = f"The following have failed:\n{failed}"
        messagebox.showerror("Error", msg)

    def _submit_max_changes(self) -> None:
        try:
            left, right = self._read_value(128)
        except ValueError:
            return
        ep = b'\x00'
        msg = b'\x15' + left.to_bytes(2, byteorder="little") + right.to_bytes(2, byteorder="little") + b'\x00' * 11
        self._submit_change(ep, msg)

    def _submit_min_changes(self) -> None:
        try:
            left, right = self._read_value(128)
        except ValueError:
            return
        ep = b'\x00'
        msg = b'\x16' + left.to_bytes(2, byteorder="little") + right.to_bytes(2, byteorder="little") + b'\x00' * 11
        self._submit_change(ep, msg)


    def _submit_change(self, ep: bytes, msg: bytes) -> bool:
        try:
            with hid.Device(path=self._dev_path) as dev:
                n = dev.write(ep + msg)
                if n != len(ep + msg):
                    # messagebox.showerror("Error", "Problem sending message to device")
                    return False
                str_in = dev.read(len(msg), timeout=1000)
                if str_in is None:
                    # messagebox.showerror("Error", "Device didn't respond.")
                    return False
                elif str_in != msg:
                    # messagebox.showerror("Error", "Device rejected these changes.")
                    return False
                return True
        except hid.HIDException as e:
            messagebox.showerror("Error", str(e))
            return False

    def _read_value(self, n: int) -> tuple[int, int]:
        """read n values from adc and average for left and right"""
        left, right = 0, 0
        with hid.Device(path=self._dev_path) as dev:
            ep = b'\x00'
            msg = b'\x11' + b'\x00' * 15
            for _ in range(n):
                n_written = dev.write(ep + msg)
                if n_written != len(ep + msg):
                    messagebox.showerror("Error", "Problem requesting values from device")
                    return
                str_in = dev.read(len(msg), timeout=1000)
                if str_in is None:
                    messagebox.showerror("Error", "Device didn't respond")
                    return
                else:
                    left += int.from_bytes(str_in[2:2+ADC_VALUE_SIZE], byteorder='little')
                    right += int.from_bytes(str_in[2+ADC_VALUE_SIZE:2+2*ADC_VALUE_SIZE], byteorder='little')
        return left // n, right // n

    def get_config(self) -> tuple[int, int, int, int]:
        """Get config options and update gui to reflect it"""
        with hid.Device(path=self._dev_path) as dev:
            ep = b'\x00'
            msg = b'\x01' + b'\x00' * 15
            n = dev.write(ep + msg)
            if n != len(ep + msg):
                messagebox.showerror("Error", "Problem sending message to device")
                return
            str_in = dev.read(len(msg), timeout=1000)
            if str_in is None:
                messagebox.showerror("Error", "Device didn't respond")
                return
            else:
                k_l = int.from_bytes(str_in[1:2])
                k_r = int.from_bytes(str_in[2:3])
                t_percent = int.from_bytes(str_in[3:4])
                r_percent = int.from_bytes(str_in[4:5])
                l_max = int.from_bytes(str_in[5:7], byteorder="little")
                l_min = int.from_bytes(str_in[7:9], byteorder="little")
                r_max = int.from_bytes(str_in[9:11], byteorder="little")
                r_min = int.from_bytes(str_in[11:13], byteorder="little")
                self._k_l.config(text=KEYSYM[k_l])
                self._k_r.config(text=KEYSYM[k_r])
                self._threshold_slider.set(t_percent)
                self._reset_slider.set(r_percent)
                self._hid_l = k_l
                self._hid_r = k_r
                t = f"Left:   {l_max} - {l_min} ({l_max-l_min})\nRight: {r_max} - {r_min} ({r_max-r_min})"
                self._min_max_label.config(text=t)



    def run(self):
        super().mainloop()


def _get_key(event: tk.Event) -> tuple[str, int]:
    """Determine hid keycode from keypress event"""
    try:
        return event.keysym, KEYCODE[event.keysym_num]
    except KeyError:
        return event.keysym, None


class NoDeviceWindow(tk.Frame):
    """Window shown when no device was found with which to connect"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._init_widgets()

    def _init_widgets(self) -> None:
        self._no_dev_label = tk.Label(self, text="No device found")
        self._no_dev_label.pack()


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.minsize(300, 290)

        self._config_window = ConfigWindow(self)
        self._no_dev_window = NoDeviceWindow(self)

        self._state = None
        self.after(100, self._try_find_dev)

        # --------------------------------------------
        # Load/Save file
        # --------------------------------------------
        self._menubar = tk.Menu(self)
        self._file_menu = tk.Menu(self._menubar, tearoff=0)
        self._file_menu.add_command(label="Export", command=self._export_file)
        self._file_menu.add_command(label="Import", command=self._import_file)
        self._menubar.add_cascade(label="File", menu=self._file_menu)

        self.config(menu=self._menubar)


    def _try_find_dev(self):
        path = _get_dev_path()
        if path is None:
            if self._state is None:
                self._no_dev_window.pack()
            elif self._state == "OPEN":
                self._config_window.pack_forget()
                self._no_dev_window.pack()
            self._state = "CLOSED"
        else:
            if self._state is None:
                self._config_window.pack()
                self._config_window.set_device_path(path)
                self._config_window.get_config()
            elif self._state == "CLOSED":
                self._no_dev_window.pack_forget()
                self._config_window.pack()
                self._config_window.set_device_path(path)
                self._config_window.get_config()
            self._state = "OPEN"
        self.after(100, self._try_find_dev)

    def _export_file(self) -> None:
        """Save the current config options to a file"""
        fp = filedialog.asksaveasfilename(filetypes=[("Configuration File", ".config")])
        if not fp:
            return
        stuff = self._config_window.config
        with open(fp, mode="w") as f:
            json.dump(stuff, f)

    
    def _import_file(self) -> None:
        """Import settings from a file"""
        fp = filedialog.askopenfilename(filetypes=[("Configuration File", ".config")])
        if not fp:
            return
        with open(fp, mode="r") as f:
            try:
                stuff = json.load(f)
            except json.JSONDecodeError:
                messagebox.showerror("Error", "Invalid configuration file")
        good = self._config_window.set_config(stuff)
        if not good:
            messagebox.showerror("Error", "Invalid configuration file")



def _get_dev_path() -> str | None:
    """Get path to my keypad device"""
    for d in hid.enumerate(0xCAFE):
        if d['interface_number'] == IO_ITF:
            return d['path']
    return None


if __name__ == "__main__":
    app = App()
    app.mainloop()
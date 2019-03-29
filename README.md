# mouse_macro
Set of scripts for assigning macros to Razer buttons on Naga mice.

# Install

Copy macro_launcher.service to ~/.config/systemd/user/default.target.wants and enable the systemd service
```
mkdir -p ~/.config/systemd/user
cp default.target.wants ~/.config/systemd/user/
systemctl enable --user macro_launcher.service
```

Copy macro_launcher.py to /usr/local/bin (modify the file to point to your mouse input device)
```
sudo cp macro_launcher.py /usr/local/bin
```

Copy config.json to ~/.macros
```
mkdir ~/.macros
cp config.json ~/.macros
```


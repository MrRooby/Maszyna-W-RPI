# Raspberry Pi Access Point Setup

This guide provides step-by-step instructions to set up a Raspberry Pi as an access point and configure a static IP address for the `eth0` interface.

## Prerequisites

- A Raspberry Pi with Raspbian installed
- Internet connection for installing packages
- Administrative access to the Raspberry Pi

## Step 1: Update Your Raspberry Pi

First, ensure your Raspberry Pi is up to date.

```sh
sudo apt update
sudo apt upgrade
```
## Step 2: Install and Enable `hostapd` and `dnsmasq`

Next, install the `hostapd` and `dnsmasq` packages, which are required to set up the access point.

```sh
sudo apt install hostapd dnsmasq
```

Enable `hostapd` to start on boot:

```sh
sudo systemctl unmask hostapd
sudo systemctl enable hostapd
```
## Step 3: Configure Static IP Address for `wlan0`

Edit the `dhcpcd.conf` file to configure a static IP address for the `wlan0` interface.

```sh
sudo nano /etc/dhcpcd.conf
```

Add the following lines at the end of the file:

```
interface wlan0
static ip_address=192.168.4.1/24
nohook wpa_supplicant

interface eth0
static ip_address=192.168.2.1/24
```

Save and close the file.


## Step 4: Configure `dnsmasq`

Create a new configuration file for `dnsmasq`:

```sh
sudo nano /etc/dnsmasq.conf
```

Add the following lines to the file:

```
interface=wlan0
dhcp-range=192.168.4.2,192.168.4.20,255.255.255.0,24h
```

Save and close the file.

## Step 5: Configure `hostapd`

Create a new configuration file for `hostapd`:

```sh
sudo nano /etc/hostapd/hostapd.conf
```

Add the following lines to the file:

```
interface=wlan0
driver=nl80211
ssid=YourNetworkName
hw_mode=g
channel=7
wmm_enabled=0
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase=YourPassphrase
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP
rsn_pairwise=CCMP
```

Replace `YourNetworkName` with your desired network name and `YourPassphrase` with a strong password.

Save and close the file.

Edit the `hostapd` default file to point to the new configuration:

```sh
sudo nano /etc/default/hostapd
```

Find and modify the `DAEMON_CONF` line to:

```
DAEMON_CONF="/etc/hostapd/hostapd.conf"
```

Save and close the file.

## Step 7: Enable IP Forwarding

To allow traffic to be forwarded between the `eth0` and `wlan0` interfaces, you need to enable IP forwarding.

Edit the `sysctl.conf` file:

```sh
sudo nano /etc/sysctl.conf
```

Uncomment the following line by removing the `#` at the beginning:

```
net.ipv4.ip_forward=1
```

Save and close the file.

## Step 8: Configure NAT with `iptables`

To enable Network Address Translation (NAT) for the `wlan0` interface, you need to configure `iptables`.

Add the following `iptables` rule:

```sh
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
```

Save the `iptables` rule so it persists after reboot:

```sh
sudo sh -c "iptables-save > /etc/iptables.ipv4.nat"
```

Edit the `rc.local` file to restore the `iptables` rule on boot:

```sh
sudo nano /etc/rc.local
```

Add the following line just above `exit 0`:

```sh
iptables-restore < /etc/iptables.ipv4.nat
```

Save and close the file.

## Step 9: Delete existing WiFi Connection

List out existing WiFi connections

```sh
nmcli connection show --active
```
Take the `UUID` of `wlan0` and delete the connection

```sh
sudo nmcli connection delete uuid <YOUR_UUID>
```

## Step 10: Start the Access Point

Finally, start the `hostapd` and `dnsmasq` services:

```sh
sudo systemctl start hostapd
sudo systemctl restart dhcpcd
sudo systemctl start dnsmasq
```

Check if your IP is as you set it up in previous steps

```sh
hostname -I
```

There might be multiple IP adresses but one of them should be `192.168.4.1`

## Step 11 (working against the flaws)

Creating a daemon to reset hostapd after boot

```sh
sudo nvim /usr/local/bin/restart_hostapd.sh
```

fill out with

```sh
#!/bin/bash
systemctl restart hostapd
systemctl restart dnsmasq
```

Give permissions

```sh
chmod a+x /usr/local/bin/restart_hostapd.sh
```

```sh
sudo nvim /etc/systemd/system/restart_hostapd.service
```

Insert
```sh
[Unit]
Description=Restart hostapd after full boot
After=multi-user.target

[Service]
Type=simple
ExecStart=/usr/local/bin/restart_hostapd.sh
Restart=on-failure

[Install]
WantedBy=multi-user.target
```
Activate service
```sh
sudo systemctl daemon-reload
sudo systemctl enable restart_hotspot.sh
```

# Setup as service

```sh
 sudo nvim /etc/systemd/system/maszynawd.service
```

```sh
[Unit]
Description=Run Maszyna W script after hotspot is active
After=network.target
Wants=network.target
After=systemd-networkd.service
After=NetworkManager.service

[Service]
ExecStart=/home/bartek/Maszyna-W-RPI/myenv/bin/python /home/bartek/Maszyna-W-RPI/main.py
WorkingDirectory=/home/bartek/Maszyna-W-RPI
StandardOutput=journal
StandardError=journal
Restart=on-failure
RestartSec=10
User=root
Group=root
Environment="PATH=/home/bartek/Maszyna-W-RPI/myenv/bin:/usr/bin:/bin"

[Install]
WantedBy=multi-user.target

```

```sh
sudo systemctl daemon-reload 
sudo systemctl enable maszynawd.service 
```

Your Raspberry Pi should now be configured as an access point with a static IP address and NAT enabled.

# CelestiaNodeChecker
This bot is specially created to identify the type of node light, full, bridge, for the Celestia Blockchain and its status.

My link to test my Bot in Discord and to your channels: https://discord.com/api/oauth2/authorize?client_id=1096538432383230113&permissions=67584&scope=bot 

**Functions:**

**This Bot display:**

- Get Node Type by providing Node ID.
- Node ID
- Node type
- Uptime value
- Node Uptime in seconds
- PayForBlob Count
- Last PayForBlob
- Node Start Time
- Last Sampled Time
- Last Restart time
- Network height
- Total Sync Headers


**Requirements:**

- Python 3.7+
- python-nextcord library
- python-dotenv library

**How to setup:**

1. ```git clone https://github.com/VuzzyM/CelestiaNodeChecker.git```

2. Install requirement python library: 

```pip install python-dotenv```
```pip install nextcord```

3. **Create .env file in the same folder with main.py and add token from Discord.**

 Insert BOT_TOKEN with the actual token provided by Discord.

4. **Create a Systemd service file that specifies the script you want to run and any additional options or dependencies. The service file should be named after the service, and it should end with the .service extension. For example, to create a service named celestia, you can create a file named `celestia.service` in the `/etc/systemd/system` directory.**

Example script:

```sudo nano /etc/systemd/system/celestia.service```

Insert this script and your directory.

```
[Unit]
Description=Custom Python Service
After=multi-user.target
Conflicts=getty@tty1.service

[Service]
Type=simple
Restart=always
ExecStart=/usr/bin/python3 /root/your directory/main.py
StandardInput=tty-force

[Install]
WantedBy=multi-user.target
```

![1](https://user-images.githubusercontent.com/66425682/232172724-c3c6fc3f-7e5e-4cf1-b069-bfb63f7b545e.png)


5. **Run systemd service.**

Now we need to reload the daemon.

```sudo systemctl daemon-reload```

**Let’s enable our service so that it doesn’t get disabled if the server restarts.**

```sudo systemctl enable celestia.service```

**And now let’ start our service.**

```sudo systemctl start celestia.service```

Now our service is up and running.

**To stop the service.**

```sudo systemctl stop name_of_your_service```

**To restart.**

```sudo systemctl restart name_of_your_service```

**To check status.**

```sudo systemctl status name_of_your_service```

6. **Usage this bot on discord channel:**

Use ```/node``` and put your node id.

![2](https://user-images.githubusercontent.com/66425682/232172710-4775a1e4-45ef-47f8-a0ab-f53cfcdd0c8d.png)

Result:

![3](https://user-images.githubusercontent.com/66425682/232172717-bc00f440-c207-4a5f-a7f3-040ab11a7b8d.png)



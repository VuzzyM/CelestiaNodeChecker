import os
import dotenv

from datetime import datetime
from typing import Dict, Optional, Any

import requests

from nextcord import Interaction, SlashOption
from nextcord.ext.commands.bot import Bot


dotenv.load_dotenv()
token = os.getenv('BOT_TOKEN')
bot = Bot()


def to_int(value: str) -> Optional[int]:

    try:
        return int(value)
    except ValueError:
        return None


def get_node_data(node_id: str) -> Dict[str, Any]:

    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,ru-RU;q=0.6,ru;q=0.5",
        "sec-ch-ua": '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "Referer": "https://tiascan.com/",
        "Referrer-Policy": "strict-origin-when-cross-origin",
    }
    return requests.get(
        f"https://leaderboard.celestia.tools/api/v1/nodes/{node_id}",
        headers=headers,
    ).json()


@bot.slash_command(name='node')
async def handle_message(
        interaction: Interaction,
        node_id: str = SlashOption(description='Node ID')) -> None:

    if "12D3" not in node_id or len(node_id) != 52:
        return

    data = get_node_data(node_id)
    nid = data.get('node_id')
    uptime = to_int(data.get('uptime'))
    ntype = data.get('node_type_str')
    total_synced = data.get('total_synced_headers')
    start_time = data.get('start_time')
    pfb_count = data.get('pfb_count')
    last_pfb_timestamp = data.get('last_pfb_timestamp')
    node_runtime_counter_in_seconds = data.get('node_runtime_counter_in_seconds')
    network_height = data.get('network_height')
    das_latest_sampled_timestamp = data.get('das_latest_sampled_timestamp')
    last_restart = datetime.strptime(
        data.get('last_restart_time') or 0,
        "%Y-%m-%dT%H:%M:%SZ",
    )
    icon = "🟢" if uptime >= 80 else "🟢" if uptime >= 40 else "🟢"

    message = f"""💡 Celestia Node Information 💡
ℹ️ Node ID: {nid}
🔍 Node type: {ntype}
🟢 Uptime value: {uptime}
⏲️ Node Uptime in seconds: {node_runtime_counter_in_seconds}
🗃️ PayForBlob Count: {pfb_count}
⏮️ Last PayForBlob: {last_pfb_timestamp}
🎬 Node Start Time:{start_time}️
⚙ Last Sampled Time: {das_latest_sampled_timestamp} 
🛠 Last Restart time: {last_restart.strftime("%d/%m/%Y %H:%M:%S")}
🌐 Network height: {network_height}
🚀 Total Sync Headers: {total_synced}
🔔 Stay informed about node status! """

    await interaction.send(content=message)


bot.run(token)

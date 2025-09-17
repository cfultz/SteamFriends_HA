import logging
from datetime import timedelta

import aiohttp
import async_timeout

from homeassistant.components.sensor import SensorEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

_LOGGER = logging.getLogger(__name__)

SCAN_INTERVAL = timedelta(minutes=15)

async def async_setup_entry(hass: HomeAssistant, config_entry, async_add_entities):
    """Set up the Steam Friends sensor."""
    api_key = config_entry.data.get("api_key")
    steam_id = config_entry.data.get("steam_id")
    async_add_entities([SteamFriendsSensor(api_key, steam_id)], True)

class SteamFriendsSensor(SensorEntity):
    """Representation of a Steam Friends sensor."""

    def __init__(self, api_key, steam_id):
        """Initialize the sensor."""
        self._api_key = api_key
        self._steam_id = steam_id
        self._state = None
        self._name = "Online Steam Friends"
        self._unit_of_measurement = "Friends"

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return self._unit_of_measurement

    async def async_update(self):
        """Update the sensor."""
        try:
            # 1. Get friends list
            async with async_timeout.timeout(10):
                async with aiohttp.ClientSession() as session:
                    friends_url = f"http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={self._api_key}&steamid={self._steam_id}&relationship=friend"
                    async with session.get(friends_url) as response:
                        friends_data = await response.json()
                        friends_ids = [friend['steamid'] for friend in friends_data['friendslist']['friends']]

            # 2. Get player statuses
            async with async_timeout.timeout(10):
                async with aiohttp.ClientSession() as session:
                    player_summaries_url = f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={self._api_key}&steamids={','.join(friends_ids)}"
                    async with session.get(player_summaries_url) as response:
                        players_data = await response.json()
                        online_count = 0
                        for player in players_data['response']['players']:
                            if player['personastate'] in [1, 5, 6]:
                                online_count += 1
                        self._state = online_count

        except Exception as e:
            _LOGGER.error(f"Error fetching Steam data: {e}")
            self._state = None

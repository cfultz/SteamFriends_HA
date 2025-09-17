import logging

from homeassistant import helpers
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

_LOGGER = logging.getLogger(__name__)

DOMAIN = "steam_friends_counter"

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the Steam Friends Counter component."""
    
    if DOMAIN in config:
        helpers.discovery.async_load_platform(hass, Platform.SENSOR, DOMAIN, config[DOMAIN])

    return True

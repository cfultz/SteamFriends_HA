import logging
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

_LOGGER = logging.getLogger(__name__)

DOMAIN = "steam_friends_counter"

def setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the Steam Friends Counter component."""
    
    # Check if the platform has a configuration and loads it.
    if DOMAIN in config:
        hass.helpers.discovery.load_platform(Platform.SENSOR, DOMAIN, config[DOMAIN], config)

    return True

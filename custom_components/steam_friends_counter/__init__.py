from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.typing import ConfigType
from .const import DOMAIN

PLATFORMS = ["sensor"]

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the component."""
    return True # We don't use YAML config anymore

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Steam Friends from a config entry."""
    hass.config_entries.async_setup_platforms(entry, PLATFORMS)
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)

import voluptuous as vol
from homeassistant import config_entries
from .const import DOMAIN

class SteamFriendsConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Steam Friends."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}
        if user_input is not None:
            return self.async_create_entry(title="Steam Friends", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("api_key"): str,
                vol.Required("steam_id"): str,
            }),
            errors=errors,
        )

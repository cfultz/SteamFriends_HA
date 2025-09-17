# config_flow.py
import voluptuous as vol
from homeassistant import config_entries
from .const import DOMAIN  # Make sure to create a const.py file

class SteamFriendsConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Steam Friends."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}
        if user_input is not None:
            # Here you would ideally validate the API key and Steam ID
            # For now, we'll just accept it.
            return self.async_create_entry(title="Steam Friends", data=user_input)

        # Show the form to the user
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("api_key"): str,
                vol.Required("steam_id"): str,
            }),
            errors=errors,
        )

# Steam Friends Integration for Home Assistant

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/hacs/integration)

This is a custom integration for Home Assistant that provides a sensor to track how many of your Steam friends are currently online or in a game.

!

***

## Installation

### Prerequisites

You must have the [Home Assistant Community Store (HACS)](https://hacs.xyz/) installed on your Home Assistant instance.

---

### Add Repository to HACS

The easiest way to install this integration is to add it as a custom repository in HACS.

1.  Click the button below to add the repository to your HACS instance.

    [![Open your Home Assistant instance and add a custom repository.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=cfultz&repository=SteamFriends_HA&category=integration)

2.  If the button doesn't work, you can add it manually:
    * Go to **HACS > Integrations**.
    * Click the three-dots menu in the top right and select **"Custom repositories"**.
    * In the "Repository" field, paste this URL: `https://github.com/cfultz/SteamFriends_HA`
    * In the "Category" dropdown, select **"Integration"**.
    * Click **"Add"**.

3.  Once the custom repository is added, search for "Steam Friends" in HACS and click **"Download"**.

4.  **Restart Home Assistant** for the integration to be loaded.

---

## Configuration

Configuration is done entirely through the Home Assistant UI.

1.  Go to **Settings > Devices & Services**.
2.  Click the **+ ADD INTEGRATION** button in the bottom right.
3.  Search for **"Steam Friends"** and select it.
4.  In the configuration window, provide the following:
    * **Steam API Key**: Your personal Steam Web API key. You can get one [here](https://steamcommunity.com/dev/apikey).
    * **Steam ID**: Your 64-bit numeric Steam ID (also called `steamID64`). You can find yours using a tool like [SteamID Finder](https://www.steamidfinder.com/).

5.  Click **Submit**, and the sensor will be created.

---

## Sensor Usage

The integration creates a single sensor named `sensor.online_steam_friends`.

### State

The state of the sensor is a numeric value representing the total count of friends who are currently online, busy, away, or playing a game.

### Attributes

The sensor includes an `online_friends` attribute, which is a list containing details for each friend who is online. Each entry in the list includes:
* `name`: The friend's Steam profile name.
* `status`: A number representing their current status.
* `game`: The name of the game they are currently playing, if any.

You can use this attribute in templates to create more advanced automations or custom Lovelace cards.

---

## Contributions & Issues

If you encounter a bug or have a feature request, please [open an issue](https://github.com/cfultz/SteamFriends_HA/issues) on the GitHub repository.

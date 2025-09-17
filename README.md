# Steam Friends Counter

A Home Assistant custom integration that counts the number of online friends from your Steam profile.

#### Features

* Counts the number of friends with an "online" status (including In-Game).
* Automatically fetches your entire friends list without manual configuration.
* Creates a single sensor entity to track the total count.

---

### Installation

This integration can be easily installed and managed via the **Home Assistant Community Store (HACS)**.

#### Prerequisites

* You must have **HACS** installed and configured in your Home Assistant instance.
* You will need a **Steam Web API key**. You can get one from the [Steam Web API Key registration page](https://steamcommunity.com/dev/apikey).

#### HACS Installation

1.  Open HACS in your Home Assistant UI.
2.  Go to the **Integrations** section.
3.  Click the **three dots** in the top-right corner and select **Custom repositories**.
4.  In the "Add custom repository" dialog, paste the URL of this repository: `https://github.com/your-username/steam-friends-counter`
5.  Select the **Integration** category and click **ADD**.
6.  You should now see the "Steam Friends Counter" in your list of new repositories. Click on it.
7.  Select the **Download** button to install the integration.

---

### Configuration

To configure the integration, add the following to your `configuration.yaml` file and restart Home Assistant.

```yaml
steam_friends_counter:
  api_key: YOUR_STEAM_API_KEY
  steam_id: YOUR_STEAM_ID64
```

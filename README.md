# integration_bchydro

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)

[![hacs][hacsbadge]][hacs]
![Project Maintenance][maintenance-shield]
[![BuyMeCoffee][buymecoffeebadge]][buymecoffee]

[![Discord][discord-shield]][discord]
[![Community Forum][forum-shield]][forum]

_Component to integrate with [integration_bchydro][integration_bchydro]._

**This component will set up the following platforms.**

Platform | Description
-- | --
`binary_sensor` | Show something `True` or `False`.
`sensor` | Show info from bchydro API.
`switch` | Switch something `True` or `False`.

![example][exampleimg]

## Installation

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
2. If you do not have a `custom_components` directory (folder) there, you need to create it.
3. In the `custom_components` directory (folder) create a new folder called `integration_bchydro`.
4. Download _all_ the files from the `custom_components/integration_bchydro/` directory (folder) in this repository.
5. Place the files you downloaded in the new directory (folder) you created.
6. Restart Home Assistant
7. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "bchydro"

Using your HA configuration directory (folder) as a starting point you should now also have this:

```text
custom_components/integration_bchydro/translations/en.json
custom_components/integration_bchydro/translations/nb.json
custom_components/integration_bchydro/translations/sensor.nb.json
custom_components/integration_bchydro/__init__.py
custom_components/integration_bchydro/api.py
custom_components/integration_bchydro/binary_sensor.py
custom_components/integration_bchydro/config_flow.py
custom_components/integration_bchydro/const.py
custom_components/integration_bchydro/manifest.json
custom_components/integration_bchydro/sensor.py
custom_components/integration_bchydro/switch.py
```

## Configuration is done in the UI

<!---->

## Contributions are welcome!

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)

***

[integration_bchydro]: https://github.com/halkeye/integration_bchydro
~[buymecoffee]: https://www.buymeacoffee.com/ludeeus~
~[buymecoffeebadge]: https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=for-the-badge~
[commits-shield]: https://img.shields.io/github/commit-activity/y/custom-components/bchydro.svg?style=for-the-badge
[commits]: https://github.com/halkeye/integration_bchydro/commits/master
[hacs]: https://github.com/custom-components/hacs
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
~[discord]: https://discord.gg/Qa5fW2R~
~[discord-shield]: https://img.shields.io/discord/330944238910963714.svg?style=for-the-badge~
[exampleimg]: example.png
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=for-the-badge
[forum]: https://community.home-assistant.io/
[license-shield]: https://img.shields.io/github/license/custom-components/bchydro.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-Gavin%20Mogan%20%40halkeye-blue.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/custom-components/bchydro.svg?style=for-the-badge
[releases]: https://github.com/halkeye/integration_bchydro/releases

"""Sensor platform for integration_bchydro."""
import logging
from .const import DEFAULT_NAME, DOMAIN
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.components.sensor import STATE_CLASS_MEASUREMENT, SensorEntity

from .const import DOMAIN, NAME, VERSION, ATTRIBUTION

from homeassistant.const import (
    DEVICE_CLASS_ENERGY,
    DEVICE_CLASS_POWER,
    DEVICE_CLASS_MONETARY,
    ENERGY_WATT_HOUR,
)

_LOGGER: logging.Logger = logging.getLogger(__package__)


async def async_setup_entry(hass, entry, async_add_devices):
    """Setup sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    _LOGGER.info("Adding sensors")
    async_add_devices(
        [
            BCHydroUsageSensor(coordinator, entry),
            BCHydroCostSensor(coordinator, entry),
        ]
    )


from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.components.sensor import STATE_CLASS_MEASUREMENT

from .const import DOMAIN, NAME, VERSION, ATTRIBUTION


class BCHydroBaseSensor(CoordinatorEntity, SensorEntity):
    def __init__(self, coordinator, config_entry):
        super().__init__(coordinator)
        self.config_entry = config_entry

    @property
    def id(self):
        return "unknown"

    @property
    def state_class(self):
        return STATE_CLASS_MEASUREMENT

    @property
    def unique_id(self):
        """Return a unique ID to use for this entity."""
        return f"{self.config_entry.entry_id}_#{self.id}"

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self.unique_id)},
            "name": NAME,
            "model": VERSION,
            "manufacturer": NAME,
        }

    @property
    def device_state_attributes(self):
        """Return the state attributes."""
        return {
            "attribution": ATTRIBUTION,
            "id": str(self.id),
            "integration": DOMAIN,
            "last_reset": self.coordinator.api.latest_interval.end,
        }


class BCHydroUsageSensor(BCHydroBaseSensor):
    # def __init__(self, coordinator, config_entry):
    #     super().__init__(coordinator, config_entry)
    #     self._api = api
    #     self._unique_id = unique_id
    #     self._name = name
    #     self._device_class = device_class
    #     self._unit_of_measurement = unit_of_measurement

    @property
    def unit_of_measurement(self):
        # ENERGY_KILO_WATT_HOUR
        return ENERGY_WATT_HOUR

    @property
    def device_class(self):
        # DEVICE_CLASS_POWER
        return DEVICE_CLASS_ENERGY

    @property
    def name(self):
        return f"{DEFAULT_NAME} Latest Usage"

    @property
    def id(self):
        return "usage"

    @property
    def state(self):
        return self.coordinator.api.latest_usage

    @property
    def icon(self):
        return "mdi:gauge"


class BCHydroCostSensor(BCHydroBaseSensor):
    @property
    def unit_of_measurement(self):
        return "$"

    @property
    def device_class(self):
        return DEVICE_CLASS_MONETARY

    @property
    def name(self):
        return f"{DEFAULT_NAME} Latest Cost"

    @property
    def id(self):
        return "cost"

    @property
    def state(self):
        return self.coordinator.api.latest_cost

    @property
    def icon(self):
        return "mdi:cash"

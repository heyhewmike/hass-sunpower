"""Constants for the sunpower integration."""
from homeassistant.const import (
    TIME_SECONDS,
    DATA_KILOBYTES,
    FREQUENCY_HERTZ,
    ENERGY_KILO_WATT_HOUR,
    POWER_KILO_WATT,
    POWER_VOLT_AMPERE,
    PERCENTAGE,
    ELECTRIC_POTENTIAL_VOLT,
    ELECTRIC_CURRENT_AMPERE,
    TEMP_CELSIUS,
    DEVICE_CLASS_ENERGY,
    DEVICE_CLASS_POWER,
    DEVICE_CLASS_VOLTAGE,
    DEVICE_CLASS_CURRENT,
    DEVICE_CLASS_TEMPERATURE,
    DEVICE_CLASS_POWER_FACTOR
)

from homeassistant.components.sensor import (
    STATE_CLASS_MEASUREMENT,
    STATE_CLASS_TOTAL,
    STATE_CLASS_TOTAL_INCREASING
)

DOMAIN = "sunpower"

SUNPOWER_DESCRIPTIVE_NAMES = "use_descriptive_names"
SUNPOWER_OBJECT = "sunpower"
SUNPOWER_HOST = "host"
SUNPOWER_COORDINATOR = "coordinator"
UPDATE_INTERVAL = 120
SETUP_TIMEOUT_MIN = 5

PVS_DEVICE_TYPE = "PVS"
INVERTER_DEVICE_TYPE = "Inverter"
METER_DEVICE_TYPE = "Power Meter"

PVS_STATE = "STATE"

METER_STATE = "STATE"

INVERTER_STATE = "STATE"

WORKING_STATE = "working"

METER_SENSORS = {
    "METER_FREQUENCY": ["freq_hz", "Frequency", FREQUENCY_HERTZ, "mdi:flash",
                        None, STATE_CLASS_MEASUREMENT],
    "METER_NET_KWH": [
        "net_ltea_3phsum_kwh",
        "Lifetime Power",
        ENERGY_KILO_WATT_HOUR,
        "mdi:flash",
        DEVICE_CLASS_ENERGY, STATE_CLASS_TOTAL,
    ],
    "METER_KW": ["p_3phsum_kw", "Power", POWER_KILO_WATT, "mdi:flash",
                 DEVICE_CLASS_POWER, STATE_CLASS_MEASUREMENT],
    "METER_VAR": ["q_3phsum_kvar", "KVA Reactive", POWER_VOLT_AMPERE, "mdi:flash",
                  None, STATE_CLASS_MEASUREMENT],
    "METER_VA": ["s_3phsum_kva", "KVA Apparent", POWER_VOLT_AMPERE, "mdi:flash",
                 None, STATE_CLASS_MEASUREMENT],
    "METER_POWER_FACTOR": ["tot_pf_rto", "Power Factor", PERCENTAGE, "mdi:flash",
                           DEVICE_CLASS_POWER_FACTOR, STATE_CLASS_MEASUREMENT],
    "METER_L1_A": ["i1_a", "Leg 1 Amps", ELECTRIC_CURRENT_AMPERE, "mdi:flash",
                   DEVICE_CLASS_CURRENT, STATE_CLASS_MEASUREMENT],
    "METER_L2_A": ["i2_a", "Leg 2 Amps", ELECTRIC_CURRENT_AMPERE, "mdi:flash",
                   DEVICE_CLASS_CURRENT, STATE_CLASS_MEASUREMENT],
    "METER_L1_KW": ["p1_kw", "Leg 1 KW", POWER_KILO_WATT, "mdi:flash",
                    DEVICE_CLASS_POWER, STATE_CLASS_MEASUREMENT],
    "METER_L2_KW": ["p2_kw", "Leg 2 KW", POWER_KILO_WATT, "mdi:flash",
                    DEVICE_CLASS_POWER, STATE_CLASS_MEASUREMENT],
    "METER_L1_V": ["v1n_v", "Leg 1 Volts", ELECTRIC_POTENTIAL_VOLT, "mdi:flash",
                   DEVICE_CLASS_VOLTAGE, STATE_CLASS_MEASUREMENT],
    "METER_L2_V": ["v2n_v", "Leg 2 Volts", ELECTRIC_POTENTIAL_VOLT, "mdi:flash",
                   DEVICE_CLASS_VOLTAGE, STATE_CLASS_MEASUREMENT],
    "METER_L12_V": ["v12_v", "Supply Volts", ELECTRIC_POTENTIAL_VOLT, "mdi:flash",
                    DEVICE_CLASS_VOLTAGE, STATE_CLASS_MEASUREMENT],
    "METER_TO_GRID": ["neg_ltea_3phsum_kwh", "KWH To Grid", ENERGY_KILO_WATT_HOUR, "mdi:flash",
                      DEVICE_CLASS_ENERGY, STATE_CLASS_TOTAL],
    "METER_TO_HOME": ["pos_ltea_3phsum_kwh", "KWH To Home", ENERGY_KILO_WATT_HOUR, "mdi:flash",
                      DEVICE_CLASS_ENERGY, STATE_CLASS_TOTAL_INCREASING]
}

INVERTER_SENSORS = {
    "INVERTER_NET_KWH": [
        "ltea_3phsum_kwh",
        "Lifetime Power",
        ENERGY_KILO_WATT_HOUR,
        "mdi:flash",
        DEVICE_CLASS_ENERGY,
        STATE_CLASS_TOTAL_INCREASING
    ],
    "INVERTER_KW": ["p_3phsum_kw", "Power", POWER_KILO_WATT, "mdi:flash",
                    DEVICE_CLASS_POWER, STATE_CLASS_MEASUREMENT],
    "INVERTER_VOLTS": ["vln_3phavg_v", "Voltage", ELECTRIC_POTENTIAL_VOLT, "mdi:flash",
                       DEVICE_CLASS_VOLTAGE, STATE_CLASS_MEASUREMENT],
    "INVERTER_AMPS": ["i_3phsum_a", "Amps", ELECTRIC_CURRENT_AMPERE, "mdi:flash",
                      DEVICE_CLASS_CURRENT, STATE_CLASS_MEASUREMENT],
    "INVERTER_MPPT_KW": ["p_mpptsum_kw", "MPPT KW", POWER_KILO_WATT, "mdi:flash",
                         DEVICE_CLASS_POWER, STATE_CLASS_MEASUREMENT],
    "INVERTER_MPPT1_KW": ["p_mppt1_kw", "MPPT KW", POWER_KILO_WATT, "mdi:flash",
                          DEVICE_CLASS_POWER, STATE_CLASS_MEASUREMENT],
    "INVERTER_MPPT_V": ["v_mppt1_v", "MPPT Volts", ELECTRIC_POTENTIAL_VOLT, "mdi:flash",
                        DEVICE_CLASS_VOLTAGE, STATE_CLASS_MEASUREMENT],
    "INVERTER_MPPT_A": ["i_mppt1_a", "MPPT Amps", ELECTRIC_CURRENT_AMPERE, "mdi:flash",
                        DEVICE_CLASS_CURRENT, STATE_CLASS_MEASUREMENT],
    "INVERTER_TEMPERATURE": [
        "t_htsnk_degc",
        "Temperature",
        TEMP_CELSIUS,
        "mdi:thermometer",
        DEVICE_CLASS_TEMPERATURE,
        STATE_CLASS_MEASUREMENT
    ],
    "INVERTER_FREQUENCY": ["freq_hz", "Frequency", FREQUENCY_HERTZ, "mdi:flash",
                           None, STATE_CLASS_MEASUREMENT],
}

PVS_SENSORS = {
    "PVS_LOAD": [
        "dl_cpu_load",
        "System Load",
        "",
        "mdi:gauge",
        None,
        STATE_CLASS_MEASUREMENT
        ],
    "PVS_ERROR_COUNT": [
        "dl_err_count",
        "Error Count",
        "",
        "mdi:alert-circle",
        None,
        STATE_CLASS_TOTAL
        ],
    "PVS_COMMUNICATION_ERRORS": [
        "dl_comm_err",
        "Communication Errors",
        "",
        "mdi:network-off",
        None,
        STATE_CLASS_TOTAL
        ],
    "PVS_SKIPPED_SCANS": [
        "dl_skipped_scans",
        "Skipped Scans",
        "",
        "mdi:network-strength-off-outline",
        None,
        STATE_CLASS_TOTAL_INCREASING
        ],
    "PVS_SCAN_TIME": [
        "dl_scan_time",
        "Scan Time",
        TIME_SECONDS,
        "mdi:timer-outline",
        None,
        STATE_CLASS_MEASUREMENT
        ],
    "PVS_UNTRANSMITTED": [
        "dl_untransmitted",
        "Untransmitted Data",
        "",
        "mdi:radio-tower",
        None,
        STATE_CLASS_MEASUREMENT
        ],
    "PVS_UPTIME": [
        "dl_uptime",
        "Uptime",
        TIME_SECONDS,
        "mdi:timer-outline",
        None,
        STATE_CLASS_TOTAL_INCREASING
        ],
    "PVS_MEMORY_USED": [
        "dl_mem_used",
        "Memory Used",
        DATA_KILOBYTES,
        "mdi:memory",
        None,
        STATE_CLASS_MEASUREMENT
        ],
    "PVS_FLASH_AVAILABLE": [
        "dl_flash_avail",
        "Flash Available",
        DATA_KILOBYTES,
        "mdi:memory",
        None,
        STATE_CLASS_MEASUREMENT
        ],
}
####@@@@@@
#Provided by sunvault.py
####@@@@@@
SUNVAULT_SENSORS = {
    "BATTERY_AMPS": ["battery_amp", "Amps", ELECTRIC_CURRENT_AMPERE, "mdi:flash",
                      DEVICE_CLASS_CURRENT, STATE_CLASS_MEASUREMENT],
    "BATTERY_VOLTS": ["battery_voltage", "Voltage", ELECTRIC_POTENTIAL_VOLT, "mdi:flash",
                       DEVICE_CLASS_VOLTAGE, STATE_CLASS_MEASUREMENT],
    "CUST_STATE_CHARGE": ["battery_custSOC", "System Load", "", "mdi:gauge",
                 None, STATE_CLASS_MEASUREMENT], # Percentage
    "SYS_STATE_CHARGE": ["battery_sysSOC", "System Load", "", "mdi:gauge",
                 None, STATE_CLASS_MEASUREMENT], # Percentage
}

#    "INVERTER_AMPS": ["i_3phsum_a", "Amps", ELECTRIC_CURRENT_AMPERE, "mdi:flash",
#                      DEVICE_CLASS_CURRENT, STATE_CLASS_MEASUREMENT],
#    "INVERTER_VOLTS": ["vln_3phavg_v", "Voltage", ELECTRIC_POTENTIAL_VOLT, "mdi:flash",
#                       DEVICE_CLASS_VOLTAGE, STATE_CLASS_MEASUREMENT],
#"PVS_LOAD": [
#        "dl_cpu_load", "System Load", "", "mdi:gauge", None, STATE_CLASS_MEASUREMENT],
#### SunVault
 = jsonpath_expression_amp.find(data)[0].value
 = jsonpath_expression_voltage.find(data)[0].value
 = jsonpath_expression_custSOC.find(data)[0].value
 = jsonpath_expression_sysSOC.find(data)[0].value
battery_temp = jsonpath_expression_temp.find(data)[0].value
battery_last_updated = jsonpath_expression_last_updated.find(data)[0].value
battery_serial = jsonpath_expression_serial.find(data)[0].value
## ESS State
ess_mode = jsonpath_expression_mode.find(data)[0].value
ess_pto = jsonpath_expression_pto.find(data)[0].value
ess_scstatus = jsonpath_expression_scStatus.find(data)[0].value
## ESS Status
ess_enHumid = jsonpath_expression_enHumid.find(data)[0].value
ess_enTemp = jsonpath_expression_enTemp.find(data)[0].value
ess_Meter_aggPower = jsonpath_expression_essMeter_aggPower.find(data)[0].value
ess_Meter_ReadingLast = jsonpath_expression_essMeter_ReadingLast.find(data)[0].value
ess_meterACurrent = jsonpath_expression_meterACurrent.find(data)[0].value
ess_meterALast = jsonpath_expression_meterALast.find(data)[0].value
ess_meterAPower = jsonpath_expression_meterAPower.find(data)[0].value
ess_meterAVoltage = jsonpath_expression_meterAVoltage.find(data)[0].value
ess_meterBCurrent = jsonpath_expression_meterBCurrent.find(data)[0].value
ess_meterBLast = jsonpath_expression_meterBLast.find(data)[0].value
ess_meterBPower = jsonpath_expression_meterBPower.find(data)[0].value
ess_meterBVoltage = jsonpath_expression_meterBVoltage.find(data)[0].value
ess_statusLast = jsonpath_expression_meterLast.find(data)[0].value
ess_statusSerial = jsonpath_expression_meterSerial.find(data)[0].value
## Hub Plus Status
hub_AuxVolt = jsonpath_expression_hubAuxVolt.find(data)[0].value
hub_ContactError = jsonpath_expression_hubContactError.find(data)[0].value
hub_ContactPostion = jsonpath_expression_hubContactPostion.find(data)[0].value
hub_GridFreqState = jsonpath_expression_hubGridFreqState.find(data)[0].value
hub_GridP1Volt = jsonpath_expression_hubGridP1Volt.find(data)[0].value
hub_GridP2Volt = jsonpath_expression_hubGridP2Volt.find(data)[0].value
hub_GridVoltState = jsonpath_expression_hubGridVoltState.find(data)[0].value
hub_Humidity = jsonpath_expression_hubHumidity.find(data)[0].value
hub_Temp = jsonpath_expression_hubTemp.find(data)[0].value
hub_InverterConnVolt = jsonpath_expression_hubInverterConnVolt.find(data)[0].value
hub_JumpStartVolt = jsonpath_expression_hubJumpStartVolt.find(data)[0].value
hub_LastUpdated = jsonpath_expression_hubLastUpdated.find(data)[0].value
hub_LoadFreqState = jsonpath_expression_hubLoadFreqState.find(data)[0].value
hub_LoadP1Volt = jsonpath_expression_hubLoadP1Volt.find(data)[0].value
hub_LoadP2Volt = jsonpath_expression_hubLoadP2Volt.find(data)[0].value
hub_LoadVoltState = jsonpath_expression_load_voltage_state.find(data)[0].value
hub_MainVolt = jsonpath_expression_hubMainVolt.find(data)[0].value
hub_SerialNumber = jsonpath_expression_hubSerialNum.find(data)[0].value

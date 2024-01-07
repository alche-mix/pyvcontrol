# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
# Copyright 2021 Jochen Schmähling
# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
#  Python Module for communication with viControl heatings using the serial Optolink interface
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program. If not, see <http://www.gnu.org/licenses/>.
# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##


import logging

ACCESS_MODE = 'access_mode'
UNIT = 'unit'
LENGTH = 'length'
ADDRESS = 'address'

VITOCAL_300G = {
# WPR300
# Kurzname: WPR 300 (WPR300)
# Name: Vitocal 300-G mit WPR 300
# Referenz: VBC700_BW_WW
# Kommentar: Sole/Wasser-Wärmepume mit witterungsgeführter Regelung für 1 Heizkreis
#            ohne Mischer und bis zu 2 Heizkreise mit Mischer
# ID 2046
# Info
# - https://github.com/openv/openv/files/2615085/Datapoints.VBC700_BW_WW.2046.txt
#  - https://www.viessmann-community.com/viessmann/attachments/viessmann/customers-heatpump-hybrid/81673/1/Datenpunkt%20Vitogate%20200%20EIB%20bei%20Verwendung%20mit%20Vitocontrol%20200%20WO1AB%20und%20WPR-300.pdf
# 0115 WPR_Vorlauftemperatur_HK_M2: Es kommt nur 0
    # All Parameters are tested and working on Vitocal 200S WO1C (Baujahr 2019)
    'Test': {ADDRESS: '0112', LENGTH: 2, UNIT: 'IS10'},

'0x0800': {ADDRESS: '0800', LENGTH: 2, UNIT: 'IS10'},
'0x5600': {ADDRESS: '5600', LENGTH: 2, UNIT: 'IS10'},
'0x6508': {ADDRESS: '6508', LENGTH: 2, UNIT: 'ISNON'},
'0xA383': {ADDRESS: 'A383', LENGTH: 2, UNIT: 'IS100'},
'0xA3C5': {ADDRESS: 'A3C5', LENGTH: 2, UNIT: 'IS100'},
'0xA391': {ADDRESS: 'A391', LENGTH: 2, UNIT: 'IS100'},
'0xA393': {ADDRESS: 'A393', LENGTH: 2, UNIT: 'IS100'},
'0x6564': {ADDRESS: '6564', LENGTH: 2, UNIT: 'IS10'},
'0x2546': {ADDRESS: '2546', LENGTH: 2, UNIT: 'IS10'},
'0x4546': {ADDRESS: '4546', LENGTH: 2, UNIT: 'IS10'},
'0x010A': {ADDRESS: '010A', LENGTH: 2, UNIT: 'IS10'},
'0x0101': {ADDRESS: '0101', LENGTH: 2, UNIT: 'IS10'},
'0x1620': {ADDRESS: '1620', LENGTH: 2, UNIT: 'ISNON'},
'0x1621': {ADDRESS: '1621', LENGTH: 2, UNIT: 'ISNON'},
'0x1622': {ADDRESS: '1622', LENGTH: 2, UNIT: 'ISNON'},
'0x1623': {ADDRESS: '1623', LENGTH: 2, UNIT: 'ISNON'},
'0x1624': {ADDRESS: '1624', LENGTH: 2, UNIT: 'ISNON'},
'0x1625': {ADDRESS: '1625', LENGTH: 2, UNIT: 'ISNON'},
'0x1626': {ADDRESS: '1626', LENGTH: 2, UNIT: 'ISNON'},
'0x1627': {ADDRESS: '1627', LENGTH: 2, UNIT: 'ISNON'},
'0x1628': {ADDRESS: '1628', LENGTH: 2, UNIT: 'ISNON'},
'0x1629': {ADDRESS: '1629', LENGTH: 2, UNIT: 'ISNON'},
'0x790A': {ADDRESS: '790A', LENGTH: 2, UNIT: 'ISNON'},
'0x0125': {ADDRESS: '0125', LENGTH: 2, UNIT: 'IS10'},
'0x0126': {ADDRESS: '0126', LENGTH: 2, UNIT: 'IS10'},
'0x7B0D': {ADDRESS: '7B0D', LENGTH: 2, UNIT: 'ISNON'},
'0x7B0E': {ADDRESS: '7B0E', LENGTH: 2, UNIT: 'ISNON'},
'0x0123': {ADDRESS: '0123', LENGTH: 2, UNIT: 'IS10'},
'0x0124': {ADDRESS: '0124', LENGTH: 2, UNIT: 'IS10'},
'0x1612': {ADDRESS: '1612', LENGTH: 2, UNIT: 'ISNON'},
'0x1613': {ADDRESS: '1613', LENGTH: 2, UNIT: 'ISNON'},
'0x1610': {ADDRESS: '1610', LENGTH: 2, UNIT: 'ISNON'},
'0x1611': {ADDRESS: '1611', LENGTH: 2, UNIT: 'ISNON'},
'0x1601': {ADDRESS: '1601', LENGTH: 2, UNIT: 'IS10'},
'0x1600': {ADDRESS: '1600', LENGTH: 2, UNIT: 'IS10'},
'0x1603': {ADDRESS: '1603', LENGTH: 2, UNIT: 'IS10'},
'0x1604': {ADDRESS: '1604', LENGTH: 2, UNIT: 'IS10'},
'0x1602': {ADDRESS: '1602', LENGTH: 2, UNIT: 'IS10'},
'0x028A': {ADDRESS: '028A', LENGTH: 2, UNIT: 'ISNON'},
'0x0281': {ADDRESS: '0281', LENGTH: 2, UNIT: 'ISNON'},
'0x02A5': {ADDRESS: '02A5', LENGTH: 2, UNIT: 'ISNON'},
'0x02A6': {ADDRESS: '02A6', LENGTH: 2, UNIT: 'ISNON'},
'0x02A3': {ADDRESS: '02A3', LENGTH: 2, UNIT: 'ISNON'},
'0x02A4': {ADDRESS: '02A4', LENGTH: 2, UNIT: 'ISNON'},
'0x02A1': {ADDRESS: '02A1', LENGTH: 2, UNIT: 'ISNON'},
'0x02A2': {ADDRESS: '02A2', LENGTH: 2, UNIT: 'ISNON'},
'0x0288': {ADDRESS: '0288', LENGTH: 2, UNIT: 'ISNON'},
'0x0289': {ADDRESS: '0289', LENGTH: 2, UNIT: 'ISNON'},
'0x028B': {ADDRESS: '028B', LENGTH: 2, UNIT: 'ISNON'},
'0x0291': {ADDRESS: '0291', LENGTH: 2, UNIT: 'ISNON'},
'0x028C': {ADDRESS: '028C', LENGTH: 2, UNIT: 'ISNON'},
'0x029C': {ADDRESS: '029C', LENGTH: 2, UNIT: 'ISNON'},
'0x029D': {ADDRESS: '029D', LENGTH: 2, UNIT: 'ISNON'},
'0x029E': {ADDRESS: '029E', LENGTH: 2, UNIT: 'ISNON'},
'0x0296': {ADDRESS: '0296', LENGTH: 2, UNIT: 'ISNON'},
'0x0297': {ADDRESS: '0297', LENGTH: 2, UNIT: 'ISNON'},
'0x0298': {ADDRESS: '0298', LENGTH: 2, UNIT: 'ISNON'},
'0x029B': {ADDRESS: '029B', LENGTH: 2, UNIT: 'ISNON'},
'0x0284': {ADDRESS: '0284', LENGTH: 2, UNIT: 'ISNON'},
'0x0292': {ADDRESS: '0292', LENGTH: 2, UNIT: 'ISNON'},
'0x0286': {ADDRESS: '0286', LENGTH: 2, UNIT: 'ISNON'},
'0x0287': {ADDRESS: '0287', LENGTH: 2, UNIT: 'ISNON'},
'0x029F': {ADDRESS: '029F', LENGTH: 2, UNIT: 'ISNON'},
'0x02A0': {ADDRESS: '02A0', LENGTH: 2, UNIT: 'ISNON'},
'0x0293': {ADDRESS: '0293', LENGTH: 2, UNIT: 'ISNON'},
'0x0282': {ADDRESS: '0282', LENGTH: 2, UNIT: 'ISNON'},
'0x0294': {ADDRESS: '0294', LENGTH: 2, UNIT: 'ISNON'},
'0x0295': {ADDRESS: '0295', LENGTH: 2, UNIT: 'ISNON'},
'0x029A': {ADDRESS: '029A', LENGTH: 2, UNIT: 'ISNON'},
'0x0299': {ADDRESS: '0299', LENGTH: 2, UNIT: 'ISNON'},
'0x0283': {ADDRESS: '0283', LENGTH: 2, UNIT: 'ISNON'},
'0x0285': {ADDRESS: '0285', LENGTH: 2, UNIT: 'ISNON'},
'0x0290': {ADDRESS: '0290', LENGTH: 2, UNIT: 'ISNON'},
'0x028F': {ADDRESS: '028F', LENGTH: 2, UNIT: 'ISNON'},
'0x028D': {ADDRESS: '028D', LENGTH: 2, UNIT: 'ISNON'},
'0x028E': {ADDRESS: '028E', LENGTH: 2, UNIT: 'ISNON'},
'0x1100': {ADDRESS: '1100', LENGTH: 2, UNIT: 'ISNON'},
'0x1101': {ADDRESS: '1101', LENGTH: 2, UNIT: 'ISNON'},
'0x1102': {ADDRESS: '1102', LENGTH: 2, UNIT: 'ISNON'},
'0x1104': {ADDRESS: '1104', LENGTH: 2, UNIT: 'ISNON'},
'0x1103': {ADDRESS: '1103', LENGTH: 2, UNIT: 'ISNON'},
'0x1107': {ADDRESS: '1107', LENGTH: 2, UNIT: 'ISNON'},
'0x1106': {ADDRESS: '1106', LENGTH: 2, UNIT: 'ISNON'},
'0x1105': {ADDRESS: '1105', LENGTH: 2, UNIT: 'ISNON'},
'0x1108': {ADDRESS: '1108', LENGTH: 2, UNIT: 'ISNON'},
'0x1000': {ADDRESS: '1000', LENGTH: 2, UNIT: 'IS10'},
'0x1001': {ADDRESS: '1001', LENGTH: 2, UNIT: 'IS10'},
'0x1002': {ADDRESS: '1002', LENGTH: 2, UNIT: 'IS10'},
'0x1004': {ADDRESS: '1004', LENGTH: 2, UNIT: 'IS10'},
'0x1003': {ADDRESS: '1003', LENGTH: 2, UNIT: 'IS10'},
'0x1007': {ADDRESS: '1007', LENGTH: 2, UNIT: 'IS10'},
'0x1006': {ADDRESS: '1006', LENGTH: 2, UNIT: 'IS10'},
'0x1005': {ADDRESS: '1005', LENGTH: 2, UNIT: 'IS10'},
'0x1008': {ADDRESS: '1008', LENGTH: 2, UNIT: 'IS10'},
'0x0121': {ADDRESS: '0121', LENGTH: 2, UNIT: 'IS10'},
'0x0122': {ADDRESS: '0122', LENGTH: 2, UNIT: 'IS10'},
'0x0108': {ADDRESS: '0108', LENGTH: 2, UNIT: 'IS10'},
'0x0109': {ADDRESS: '0109', LENGTH: 2, UNIT: 'IS10'},
'0x7201': {ADDRESS: '7201', LENGTH: 2, UNIT: 'ISNON'},
'0x1640': {ADDRESS: '1640', LENGTH: 2, UNIT: 'IS100'},
'0x1641': {ADDRESS: '1641', LENGTH: 2, UNIT: 'IS100'},
'0x1642': {ADDRESS: '1642', LENGTH: 2, UNIT: 'IS100'},
'0x1643': {ADDRESS: '1643', LENGTH: 2, UNIT: 'IS100'},
'0x1644': {ADDRESS: '1644', LENGTH: 2, UNIT: 'IS100'},
'0x1645': {ADDRESS: '1645', LENGTH: 2, UNIT: 'IS100'},
'0x1646': {ADDRESS: '1646', LENGTH: 2, UNIT: 'IS100'},
'0x1647': {ADDRESS: '1647', LENGTH: 2, UNIT: 'IS100'},
'0x1648': {ADDRESS: '1648', LENGTH: 2, UNIT: 'IS100'},
'0x1649': {ADDRESS: '1649', LENGTH: 2, UNIT: 'IS100'},
'0x164A': {ADDRESS: '164A', LENGTH: 2, UNIT: 'IS100'},
'0x164B': {ADDRESS: '164B', LENGTH: 2, UNIT: 'IS100'},
'0x010B': {ADDRESS: '010B', LENGTH: 2, UNIT: 'IS10'},
'0x2002': {ADDRESS: '2002', LENGTH: 2, UNIT: 'ISNON'},
'0x3002': {ADDRESS: '3002', LENGTH: 2, UNIT: 'ISNON'},
'0x4002': {ADDRESS: '4002', LENGTH: 2, UNIT: 'ISNON'},
'0x0111': {ADDRESS: '0111', LENGTH: 2, UNIT: 'IS10'},
'0x010C': {ADDRESS: '010C', LENGTH: 2, UNIT: 'IS10'},
'0x011C': {ADDRESS: '011C', LENGTH: 2, UNIT: 'IS10'},
'0x011D': {ADDRESS: '011D', LENGTH: 2, UNIT: 'IS10'},
'0x011E': {ADDRESS: '011E', LENGTH: 2, UNIT: 'IS10'},
'0x0116': {ADDRESS: '0116', LENGTH: 2, UNIT: 'IS10'},
'0x0117': {ADDRESS: '0117', LENGTH: 2, UNIT: 'IS10'},
'0x0118': {ADDRESS: '0118', LENGTH: 2, UNIT: 'IS10'},
'0x011B': {ADDRESS: '011B', LENGTH: 2, UNIT: 'IS10'},
'0x0104': {ADDRESS: '0104', LENGTH: 2, UNIT: 'IS10'},
'0x0106': {ADDRESS: '0106', LENGTH: 2, UNIT: 'IS10'},
'0x0107': {ADDRESS: '0107', LENGTH: 2, UNIT: 'IS10'},
'0x0112': {ADDRESS: '0112', LENGTH: 2, UNIT: 'IS10'},
'0x011F': {ADDRESS: '011F', LENGTH: 2, UNIT: 'IS10'},
'0x0120': {ADDRESS: '0120', LENGTH: 2, UNIT: 'IS10'},
'0x0113': {ADDRESS: '0113', LENGTH: 2, UNIT: 'IS10'},
'0x0102': {ADDRESS: '0102', LENGTH: 2, UNIT: 'IS10'},
'0x5012': {ADDRESS: '5012', LENGTH: 2, UNIT: 'ISNON'},
'0x5112': {ADDRESS: '5112', LENGTH: 2, UNIT: 'ISNON'},
'0x0114': {ADDRESS: '0114', LENGTH: 2, UNIT: 'IS10'},
'0x0115': {ADDRESS: '0115', LENGTH: 2, UNIT: 'IS10'},
'0x011A': {ADDRESS: '011A', LENGTH: 2, UNIT: 'IS10'},
'0x0119': {ADDRESS: '0119', LENGTH: 2, UNIT: 'IS10'},
'0x0103': {ADDRESS: '0103', LENGTH: 2, UNIT: 'IS10'},
'0x0105': {ADDRESS: '0105', LENGTH: 2, UNIT: 'IS10'},
'0x0110': {ADDRESS: '0110', LENGTH: 2, UNIT: 'IS10'},
'0x010F': {ADDRESS: '010F', LENGTH: 2, UNIT: 'IS10'},
'0x010D': {ADDRESS: '010D', LENGTH: 2, UNIT: 'IS10'},
'0x010E': {ADDRESS: '010E', LENGTH: 2, UNIT: 'IS10'},
'0x6001': {ADDRESS: '6001', LENGTH: 2, UNIT: 'ISNON'},
'0x6002': {ADDRESS: '6002', LENGTH: 2, UNIT: 'ISNON'},


    # ------ Statusinfos (read only) ------

    # Warmwasser: Warmwassertemperatur oben (0..95)
    'Warmwassertemperatur': {ADDRESS: '010d', LENGTH: 2, UNIT: 'IS10'},

    # Aussentemperatur (-40..70)
    'Aussentemperatur': {ADDRESS: '0101', LENGTH: 2, UNIT: 'IS10'},

    # Heizkreis HK1: Vorlauftemperatur Sekundaer 1 (0..95)
    'VorlauftempPrim': {ADDRESS: '0103', LENGTH: 2, UNIT: 'IS10'},

    # Ruecklauftemperatur Sekundaer 1 (0..95)
    'RuecklauftempPrim': {ADDRESS: '0104', LENGTH: 2, UNIT: 'IS10'},





    # Heizkreis HK1: Vorlauftemperatur Sekundaer 1 (0..95)
    'VorlauftempSek': {ADDRESS: '0105', LENGTH: 2, UNIT: 'IS10'},

    # Ruecklauftemperatur Sekundaer 1 (0..95)
    'RuecklauftempSek': {ADDRESS: '0106', LENGTH: 2, UNIT: 'IS10'},

    # Ruecklauftemperatur Sekundaer 1 (0..95)
    'Vorlauftemperatur_HK_M2': {ADDRESS: '0114', LENGTH: 2, UNIT: 'IS10'},


    # Sekundaerpumpe [%] (including one status byte)
    'Sekundaerpumpe': {ADDRESS: 'B421', LENGTH: 2, UNIT: 'IUNON'},

    # Faktor Energiebilanz(1 = 0.1kWh, 10 = 1kWh, 100 = 10kWh)
    'FaktorEnergiebilanz': {ADDRESS: '163F', LENGTH: 1, UNIT: 'IUNON'},

    # Heizwärme  "Heizbetrieb", Verdichter 1
    'Heizwaerme': {ADDRESS: '1640', LENGTH: 4, UNIT: 'IUNON'},

    # Elektroenergie "Heizbetrieb", Verdichter 1
    'Heizenergie': {ADDRESS: '1660', LENGTH: 4, UNIT: 'IUNON'},

    # Heizwärme  "WW-Betrieb", Verdichter 1
    'WWwaerme': {ADDRESS: '1650', LENGTH: 4, UNIT: 'IUNON'},

    # Elektroenergie "WW-Betrieb", Verdichter 1
    'WWenergie': {ADDRESS: '1670', LENGTH: 4, UNIT: 'IUNON'},

    # Verdichter [%] (including one status byte)
    'Verdichter': {ADDRESS: 'B423', LENGTH: 4, UNIT: 'IUNON'},

    # Druck Sauggas [bar] (including one status byte) - Kühlmittel
    'DruckSauggas': {ADDRESS: 'B410', LENGTH: 3, UNIT: 'IS10'},

    # Druck Heissgas [bar] (including one status byte)- Kühlmittel
    'DruckHeissgas': {ADDRESS: 'B411', LENGTH: 3, UNIT: 'IS10'},

    # Temperatur Sauggas [bar] (including one status byte)- Kühlmittel
    'TempSauggas': {ADDRESS: 'B409', LENGTH: 3, UNIT: 'IS10'},

    # Temperatur Heissgas [bar] (including one status byte)- Kühlmittel
    'TempHeissgas': {ADDRESS: 'B40A', LENGTH: 3, UNIT: 'IS10'},

    # Anlagentyp (muss 204D sein)
    'Anlagentyp': {ADDRESS: '00F8', LENGTH: 4, UNIT: 'DT'},

    # --------- Menüebene -------

    # Betriebsmodus
    'Betriebsmodus': {ADDRESS: 'B000', LENGTH: 1, UNIT: 'BA', ACCESS_MODE: 'write'},

    # getManuell / setManuell -- 0 = normal, 1 = manueller Heizbetrieb, 2 = 1x Warmwasser auf Temp2
    'WWeinmal': {ADDRESS: 'B020', LENGTH: 1, UNIT: 'OO', ACCESS_MODE: 'write'},

    # Warmwassersolltemperatur (10..60 (95))
    'SolltempWarmwasser': {ADDRESS: '6000', LENGTH: 2, UNIT: 'IS10', ACCESS_MODE: 'write', 'min_value': 10,
                           'max_value': 60},

    # --------- Codierebene 2 ---------

    # Hysterese Vorlauf ein: Verdichter schaltet im Heizbetrieb ein
    'Hysterese_Vorlauf_ein': {ADDRESS: '7304', LENGTH: 2, UNIT: 'IU10', ACCESS_MODE: 'write'},

    # Hysterese Vorlauf aus: Verdichter schaltet im Heizbetrieb ab
    'Hysterese_Vorlauf_aus': {ADDRESS: '7313', LENGTH: 2, UNIT: 'IU10', ACCESS_MODE: 'write'},

    # --------- Function Call --------
    'Energiebilanz': {ADDRESS: 'B800', LENGTH: 16, UNIT: 'F_E', ACCESS_MODE: 'call'},

}

VITOCAL_WO1C = {
    # All Parameters are tested and working on Vitocal 200S WO1C (Baujahr 2019)

    # ------ Statusinfos (read only) ------

    # Warmwasser: Warmwassertemperatur oben (0..95)
    'Warmwassertemperatur': {ADDRESS: '010d', LENGTH: 2, UNIT: 'IS10'},

    # Aussentemperatur (-40..70)
    'Aussentemperatur': {ADDRESS: '0101', LENGTH: 2, UNIT: 'IS10'},

    # Heizkreis HK1: Vorlauftemperatur Sekundaer 1 (0..95)
    'VorlauftempSek': {ADDRESS: '0105', LENGTH: 2, UNIT: 'IS10'},

    # Ruecklauftemperatur Sekundaer 1 (0..95)
    'RuecklauftempSek': {ADDRESS: '0106', LENGTH: 2, UNIT: 'IS10'},

    # Sekundaerpumpe [%] (including one status byte)
    'Sekundaerpumpe': {ADDRESS: 'B421', LENGTH: 2, UNIT: 'IUNON'},

    # Faktor Energiebilanz(1 = 0.1kWh, 10 = 1kWh, 100 = 10kWh)
    'FaktorEnergiebilanz': {ADDRESS: '163F', LENGTH: 1, UNIT: 'IUNON'},

    # Heizwärme  "Heizbetrieb", Verdichter 1
    'Heizwaerme': {ADDRESS: '1640', LENGTH: 4, UNIT: 'IUNON'},

    # Elektroenergie "Heizbetrieb", Verdichter 1
    'Heizenergie': {ADDRESS: '1660', LENGTH: 4, UNIT: 'IUNON'},

    # Heizwärme  "WW-Betrieb", Verdichter 1
    'WWwaerme': {ADDRESS: '1650', LENGTH: 4, UNIT: 'IUNON'},

    # Elektroenergie "WW-Betrieb", Verdichter 1
    'WWenergie': {ADDRESS: '1670', LENGTH: 4, UNIT: 'IUNON'},

    # Verdichter [%] (including one status byte)
    'Verdichter': {ADDRESS: 'B423', LENGTH: 4, UNIT: 'IUNON'},

    # Druck Sauggas [bar] (including one status byte) - Kühlmittel
    'DruckSauggas': {ADDRESS: 'B410', LENGTH: 3, UNIT: 'IS10'},

    # Druck Heissgas [bar] (including one status byte)- Kühlmittel
    'DruckHeissgas': {ADDRESS: 'B411', LENGTH: 3, UNIT: 'IS10'},

    # Temperatur Sauggas [bar] (including one status byte)- Kühlmittel
    'TempSauggas': {ADDRESS: 'B409', LENGTH: 3, UNIT: 'IS10'},

    # Temperatur Heissgas [bar] (including one status byte)- Kühlmittel
    'TempHeissgas': {ADDRESS: 'B40A', LENGTH: 3, UNIT: 'IS10'},

    # Anlagentyp (muss 204D sein)
    'Anlagentyp': {ADDRESS: '00F8', LENGTH: 4, UNIT: 'DT'},

    # --------- Menüebene -------

    # Betriebsmodus
    'Betriebsmodus': {ADDRESS: 'B000', LENGTH: 1, UNIT: 'BA', ACCESS_MODE: 'write'},

    # getManuell / setManuell -- 0 = normal, 1 = manueller Heizbetrieb, 2 = 1x Warmwasser auf Temp2
    'WWeinmal': {ADDRESS: 'B020', LENGTH: 1, UNIT: 'OO', ACCESS_MODE: 'write'},

    # Warmwassersolltemperatur (10..60 (95))
    'SolltempWarmwasser': {ADDRESS: '6000', LENGTH: 2, UNIT: 'IS10', ACCESS_MODE: 'write', 'min_value': 10,
                           'max_value': 60},

    # --------- Codierebene 2 ---------

    # Hysterese Vorlauf ein: Verdichter schaltet im Heizbetrieb ein
    'Hysterese_Vorlauf_ein': {ADDRESS: '7304', LENGTH: 2, UNIT: 'IU10', ACCESS_MODE: 'write'},

    # Hysterese Vorlauf aus: Verdichter schaltet im Heizbetrieb ab
    'Hysterese_Vorlauf_aus': {ADDRESS: '7313', LENGTH: 2, UNIT: 'IU10', ACCESS_MODE: 'write'},

    # --------- Function Call --------
    'Energiebilanz': {ADDRESS: 'B800', LENGTH: 16, UNIT: 'F_E', ACCESS_MODE: 'call'},

}


class viCommandException(Exception):
    pass


class viCommand(bytearray):
    """Representation of a command. Object value is a bytearray of address and length."""

    # =============================================================
    # CHANGE YOUR COMMAND SET HERE:
    command_set = VITOCAL_300G

    # =============================================================

    def __init__(self, command_name):
        """initialize object using the attributes of the chosen command."""

        try:
            command = self.command_set[command_name]
        except:
            raise viCommandException(f'Unknown command {command_name}')
        self._command_code = command[ADDRESS]
        self._value_bytes = command[LENGTH]
        self.unit = command[UNIT]
        self.access_mode = self._get_access_mode(command)
        self.command_name = command_name

        # create bytearray representation
        b = bytes.fromhex(self._command_code) + self._value_bytes.to_bytes(1, 'big')
        super().__init__(b)

    def _get_access_mode(self, command):
        if ACCESS_MODE in command.keys():
            return command[ACCESS_MODE]
        else:
            return 'read'

    @classmethod
    def _from_bytes(cls, b: bytearray):
        """Create command from address b given as byte, only the first two bytes of b are evaluated."""
        try:
            logging.debug(f'Convert {b.hex()} to command')
            command_name = next(key for key, value in cls.command_set.items() if value[ADDRESS].lower() == b[0:2].hex())
        except:
            raise viCommandException(f'No Command matching {b[0:2].hex()}')
        return viCommand(command_name)

    def response_length(self, access_mode='read'):
        """Returns the number of bytes in the response."""
        # request_response:
        # 2 'address'
        # 1 'Anzahl der Bytes des Wertes'
        # x 'Wert'
        if access_mode.lower() == 'read':
            return 3 + self._value_bytes
        elif access_mode.lower() == 'write':
            # in write mode the written values are not returned
            return 3
        else:
            return 3 + self._value_bytes

import requests
import xml.etree.ElementTree as ET

class StationInfo:
    def __init__(self, station_name: str):
        station_code = self.station_name_to_code(station_name)
        info_xml = requests.get(f"http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML?StationCode={station_code}")
        print(info_xml.text)
    
    def station_name_to_code(self, station_name: str):
        #TODO: Make this cached later
        out_dict = {}
        stations_xml = requests.get("http://api.irishrail.ie/realtime/realtime.asmx/getAllStationsXML").text
        stations = ET.fromstring(stations_xml)
        for station in stations:
            out_dict[station[0].text.upper()] = station[4].text
            if station[1].text:
                out_dict[station[1].text.upper()] = station[4].text
        return out_dict[station_name.upper()]

if __name__ == "__main__":
    st = StationInfo("Connolly")


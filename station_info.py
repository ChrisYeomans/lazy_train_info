import requests
import xml.etree.ElementTree as ET

class StationInfo:
    def __init__(self):
        pass 
        
    def get_info_lst(self, station_name):
        station_code = self.station_name_to_code(station_name)
        info_xml = ET.fromstring(requests.get(f"http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML?StationCode={station_code}").text)
        info_lst = []

        for i in info_xml:
            tmp_dict = {}
            for j in i:
                tmp_dict[j.tag.split("{http://api.irishrail.ie/realtime/}")[1]] = j.text
            #if tmp_dict['Destination'] != self.station_name:
            info_lst.append(tmp_dict)
        
        return info_lst
    
    def station_name_to_code(self, station_name: str):
        #TODO: Make this cached
        out_dict = {}
        stations_xml = requests.get("http://api.irishrail.ie/realtime/realtime.asmx/getAllStationsXML").text
        stations = ET.fromstring(stations_xml)
        for station in stations:
            out_dict[station[0].text.upper()] = station[4].text
        return out_dict[station_name.upper()]
    
    def get_station_lst(self):
        out_lst = []
        stations_xml = requests.get("http://api.irishrail.ie/realtime/realtime.asmx/getAllStationsXML").text
        stations = ET.fromstring(stations_xml)
        for station in stations:
            out_lst.append(station[0].text)
        return out_lst

if __name__ == "__main__":
    st = StationInfo()
    print(st.get_station_lst())


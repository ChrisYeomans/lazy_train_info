import requests
import xml.etree.ElementTree as ET

class StationInfo:
    info_lst = []
    station_code = ""
    station_name = ""

    def __init__(self, station_name: str):
        self.station_name = station_name
        self.station_code = self.station_name_to_code(station_name)
        info_xml = ET.fromstring(requests.get(f"http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML?StationCode={self.station_code}").text)
        
        for i in info_xml:
            tmp_dict = {}
            for j in i:
                tmp_dict[j.tag.split("{http://api.irishrail.ie/realtime/}")[1]] = j.text
            if tmp_dict['Destination'] != self.station_name:
                self.info_lst.append(tmp_dict)
    
        for p in self.info_lst:
            print(p['Traincode'])

        
    
    def station_name_to_code(self, station_name: str):
        #TODO: Make this cached
        out_dict = {}
        stations_xml = requests.get("http://api.irishrail.ie/realtime/realtime.asmx/getAllStationsXML").text
        stations = ET.fromstring(stations_xml)
        for station in stations:
            out_dict[station[0].text.upper()] = station[4].text
        return out_dict[station_name.upper()]

if __name__ == "__main__":
    st = StationInfo("Dublin Connolly")
    #print(st.station_code)


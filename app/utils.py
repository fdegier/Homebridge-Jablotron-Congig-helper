from jablotronpy import Jablotron


def get_homebridge_config(username: str, password: str):
    jablotron = Jablotron(username=username, password=password)
    services = jablotron.get_services()
    service_config = []

    for i in services:
        service_dict = {
            "id": i["id"],
            "name": i["name"],
            "username": username,
            "password": password,
            "pincode": "Enter Your pincode",
            "service_type": i["service_type"],
            "autoRefresh": True,
            "poolInterval": 60,
            "refreshOnStateChange": True,
            "debug": False,
            "sections": [],
            "switches": [],
            "outlets": []
        }

        segment_details = jablotron.get_service_details(service_id=i["id"])

        for segment in segment_details['data']['service_data'][0]['data'][0]['data']['segments']:
            if segment["segment_is_controllable"] is True and segment["segment_status"] == "ready":
                service_dict["sections"].append({
                    "name": segment["segment_name"],
                    "segment_id": segment["segment_id"],
                    "segment_key": segment["segment_key"],
                    "armedMode": "Away"
                })

        for switch in segment_details['data']['service_data'][0]['data'][2]['data']['segments']:
            if switch["segment_is_controllable"] is True and switch["segment_status"] == "ready":
                service_dict["switches"].append({
                    "name": switch["segment_name"],
                    "segment_id": switch["segment_id"],
                    "segment_key": switch["segment_key"]
                })
        service_config.append(service_dict)

    return service_config

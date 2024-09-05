import requests

def geocode_address(address):
    try:
        # Define the endpoint and parameters
        endpoint = "https://nominatim.openstreetmap.org/search"
        params = {
            'q': address,
            'format': 'json',
            'limit': 1
        }

        # Make the request
        response = requests.get(endpoint, params=params)
        data = response.json()

        if not data:
            return {"error": "Address not found"}

        # Extract the first result
        result = data[0]
        latitude = result.get('lat')
        longitude = result.get('lon')
        display_name = result.get('display_name')

        return {
            "address": address,
            "latitude": latitude,
            "longitude": longitude,
            "display_name": display_name
        }
    except Exception as e:
        return {"error": f"Error geocoding address: {e}"}

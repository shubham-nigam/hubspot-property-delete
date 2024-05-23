def main(event):
    # Import necessary libraries
    import requests
    import pprint
    import json
    
    # Define Access Token of your HubSpot Private App and user ID
    access_token = '[your_access_token]'
    user_id = '[your_user_id]'
    
    # Define API endpoint URL
    url = f'https://api.hubapi.com/crm/v3/properties/companies'
    
    # Define timestamp to filter properties
    timestamp_to_filter = "2024-05-06T18:17:40.686Z"
    
    # Define request headers
    headers = {
        "Authorization": "Bearer {}".format(access_token),
        "Content-Type": "application/json",
    }
    
    try:
        # Send GET request to retrieve properties
        response = requests.get(url, headers=headers)
        
        # Check if request was successful
        if response.status_code == 200:
            # Parse JSON response to a Python dictionary
            data = response.json()
            
            # Extract properties from the response
            properties = data.get('results', [])
            
            # Initialize list to store filtered properties
            filtered_properties = []
            
            # Loop through properties and filter by timestamp and user ID
            for prop in properties:
                if prop.get('createdAt') == timestamp_to_filter and prop.get('createdUserId') == user_id:
                    filtered_properties.append(prop)
            
            # Check if any properties were filtered
            if filtered_properties:
                # Print filtered properties
                print("Properties created at", timestamp_to_filter + ":")
                for prop in filtered_properties:
                    print(prop['name'])
                    
                # Count the number of filtered properties
                num_properties = len(filtered_properties)
                pprint.pprint(num_properties)
                
                # Delete filtered properties
                for prop in filtered_properties:
                    # Construct URL for DELETE request
                    property_name = prop['name']
                    delete_url = f"https://api.hubapi.com/crm/v3/properties/companies/"+property_name
                    
                    # Send DELETE request to delete property
                    response = requests.delete(delete_url, headers=headers)
                    
                    # Check if deletion was successful
                    if response.status_code == 204:
                        print(f"Property '{property_name}' deleted successfully.")
                    else:
                        print(f"Failed to delete property '{property_name}'. Status code: {response.status_code}")
            else:
                print("No properties found created at", timestamp_to_filter)
        else:
            print(f"Failed to retrieve properties. Status code: {response.status_code}")
            return None
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except ValueError as val_err:
        print(f"Value error occurred: {val_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

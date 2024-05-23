# Requirements for HubSpot Private App Integration:
- **requests==2.26.0**: This library is used for making HTTP requests to the HubSpot API.

# HubSpot Private App Creation Steps:
1. **Create a Private App in HubSpot**: Log in to your HubSpot account and navigate to "Settings" > "Integrations" > "API". Click on "Private Apps" and then "Create a Private App". Provide a name for your app, select the appropriate scopes, and generate an API key.

2. **Configure Scopes**: Ensure that the following scopes are selected for your Private App to enable access to the necessary endpoints:
   - `contacts:read`: Read access to contacts.
   - `properties:read`: Read access to properties.
   - `properties:write`: Write access to properties (for deletion).

3. **API Key**: Retrieve the API key generated for your Private App and update the `API_KEY` variable in the script with this key.

4. **User ID**: Determine the user ID associated with the properties you want to filter and delete. Update the `user_id` variable in the script with this ID.

5. **Timestamp**: Define the timestamp to filter properties. Update the `timestamp_to_filter` variable in the script with the desired timestamp.

6. **Run the Script**: Follow the instructions in the README to install dependencies and run the script. It will filter and delete properties based on the specified criteria.

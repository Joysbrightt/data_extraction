import time
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Initialize a WebClient instance with your Slack API token
client = WebClient(token='YOUR_SLACK_API_TOKEN')


# Function to get profile information of multiple users
def get_user_profiles(user_ids):
    profiles = []
    batch_size = 100  # Adjust batch size as needed
    for i in range(0, len(user_ids), batch_size):
        batch = user_ids[i:i + batch_size]
        try:
            # Call the users.profile.get API method with the batch of user IDs
            response = client.users_profile_get(user=batch)
            profiles.extend(response['profiles'])
            time.sleep(1)  # Introduce a delay to avoid rate limiting
        except SlackApiError as e:
            print(f"Error fetching user profiles: {e.response['error']}")
    return profiles


# Replace 'USER_IDS' with a list of user IDs whose profiles you want to retrieve
user_ids = ['USER_ID_1', 'USER_ID_2', ...]
profiles = get_user_profiles(user_ids)

# Print the profiles
for profile in profiles:
    print(profile)

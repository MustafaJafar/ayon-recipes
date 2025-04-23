# Create AYON Demo Users

This script helps you create test users on the AYON server. Test users are useful for testing team assignments and making demos.

## Migrate User Between AYON Instances

To migrate users between AYON instances, follow these steps:

1. **Get List of AYON Users**: This can be done via GraphQL.
2. **Download User Info and Avatar**: For each user, download their information and avatar using the following endpoints:
   - User info: `/api/users/{user_name}`
   - User avatar: `/api/users/{user_name}/avatar`
3. **Create Users**: Use the following endpoints to create users and upload their avatars on the new instance. This can be done by [create_users.py](create_users.py).
   - Create user: `[PUT] /api/users/username`
   - Upload avatar: `[PUT] /api/users/{user_name}/avatar`
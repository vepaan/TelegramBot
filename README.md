# telegram-analysis
Tools to analyze Telegram groups and channels

Please note that groups are as same as channels in Telegram. so you can use this code to get users and messages from any public group or channel. Also if you are a member of a private group or channel you can still get users list and messages from that group.

When I was once looking for appointments of a certain organization, the organaization opened appointments on their website.
However, due to high demand of these appointments, any appointments that did open were exhaused within seconds. Furthermore, the org opened appointments randomly without anyone knowing.
To know when the appointments opened, there was a telegram group where people posted updates on appointments 24/7. 
The interesting thing about the group was that you were only allowed to message either "Update" or a time when appointments did open.
When appointments opened, the messages on the group contained numbers (for example: 2024 april 50 slots)
This bot constantly listens for messages in the group and opens the organizations website when it detects numbers in the message, so I could get an edge.

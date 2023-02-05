# You should not hardcode sensitive information such as passwords, client secrets, and other authentication details in your source code. 
# Instead, you should store these values in environment variables or a configuration file and read them from your code.
# The best practice is to create a separate file for configuration data and store the environment variables or configuration values there. 
# Then you can import the configuration data into your main code file. This allows you to easily change the values in the configuration file 
# without having to modify the source code of your main application.

import os
import praw
import config

# export CLIENT_ID=your_client_id

#CLIENT_ID = os.environ.get("pOqf7h1386-EwbhVwUm6hQ")
#CLIENT_SECRET = os.environ.get("XPHRMiHkZFZ1n2NkzliPQ0mwLa9JHQ")
#USERNAME = os.environ.get("Constant-Juggernaut-2")
#PASSWORD = os.environ.get("W!nter2003")
#USER_AGENT = os.environ.get("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36")

# Set the environment variables for your Reddit account
os.environ["CLIENT_ID"] = "pOqf7h1386-EwbhVwUm6hQ"
os.environ["CLIENT_SECRET"] = "XPHRMiHkZFZ1n2NkzliPQ0mwLa9JHQ"
os.environ["USERNAME"] = "Constant-Juggernaut-2"
os.environ["PASSWORD"] = "W!nter2003"
os.environ["USER_AGENT"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"


# Lovable_Python
Python scripts to interact and do various things on Lovable.dev


Project ID: Unique identifier for a given site (not considered secret)

Bearer Token: Unique per Lovable user, it is used for authentication and authorization (very secret, do not share)

[Read my article]([https://medium.com/avi-parshan-studios/stop-leaking-your-api-keys-on-lovable-dev-3117bb3fe2ec](https://medium.com/avi-parshan-studios/stop-leaking-your-api-keys-on-lovable-dev-3117bb3fe2ec?source=social.tw )) on API Tokens that got leaked (also shows how to get project id and bearer tokens)

* remix.py

Remix a project (can also opt to inlcude project history - prompts and code changes) 

* deleter.py

Delete a project you own on lovable (if you transfered the project to GitHub, it will not delete that repository)

* extract_id.py

Given a project or site URL, this will attempt to find the Project ID (may not always work)
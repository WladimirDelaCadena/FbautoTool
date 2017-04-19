# FbautoTool

Facebook user behavior robot.

This small tool allows you to browse automatically through facebook with a known profile and perform the folowing actions:
0. Go to homepage
1. Read notifications
2. Share content of the Feed (randomly chosen)
3. Look photos
4. Visit friend's profile chosen randomly
5. Posting random content
The tool works for now only in Ubuntu with chromium, is writen in python and needs the following dependencies: numpy, selenium and pyautogui

## Example:
1. The tool reads a list of clickstreams, a clickstream is a secuence of coma separated values indicating the actions avobe described. Eg. 0,3,3,2 means the user log in to homepage, visit two pictures and share once something in the feed. One sample of clickstream file is included (each line is a session)
2. Run the file brwosing.py (editing )and look how it browses automatically
3. Resources: For actions 4 and 3 the systems looks within the /res folder to get the links for a picture or profile (sorry! this should be automatically but for now you need a file with those urls.). For posting another .txt with text to be posted is needed also (a sample is provided!)
# Notes:
The clickstreams where generated with a real HMM based on real user behavior so the history, traffic and all generated statistically responds to a real user. 
I hope you can play with it at least to post content easily.


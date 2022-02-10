# CTFd Feedback API

Since I was too lazy to figure out how to get the data into CTFd's database from the plugin, you're going to need to use this Docker container as an intermediary to get the feedback answers into Firebase. Just run this Docker container on port `8090` (or whatever port you want if you change the url in the [ctfd_survey plugin]() I made) and it will submit the survey feedback to Firebase.

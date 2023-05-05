# DockerMiniMail

A simple temp-email integrated with docker.

Temp email, or temporary email, offers a number of advantages for users who want to maintain their privacy and avoid unwanted emails in their inbox. Here are a few benefits of using a temp email service:

* Protect your privacy: By using a temporary email, you can protect your personal email address from being shared or sold to third parties. This can help to reduce the amount of spam and promotional emails you receive in your inbox.

* Avoid unwanted emails: A temp email can be used for one-time registrations or sign-ups, which means that you can avoid receiving future emails from that source. This can be especially useful for avoiding unwanted promotional emails and newsletters.

* Simplify account creation: With a temp email, you can easily create new accounts without having to use your personal email address. This can be helpful for signing up for online services or trying out new apps without risking your personal data.

* Reduce identity theft risk: By using a temporary email, you can limit the amount of personal information that you share online. This can help to reduce the risk of identity theft and protect your personal data.

Overall, temp email offers a convenient and secure way to manage your online identity and protect your privacy.

This project utilizes the 1secmail service API to manage temporary email. The files are automatically saved on the host computer and the application runs in the background, periodically checking the backend after a delay. Additionally, the application has the capability to track multiple emails simultaneously.

### Building the service

```
docker build -t mini-mail .
```

### Runnning the service

```
docker run -d --volume $(pwd)/data:/app/data --name mini-mail mini-mail
```

### Configuring the service

You can include new usernames in the list of emails to track : data/config/emails.


You can change the delay time to check the 1secmail API : data/config/time_seconds.

### Warning

The attached files may not function correctly on occasion, which could potentially be attributed to limitations within the 1secmail API.

The primary purpose of this program is to assist developers and other users in managing temporary emails. It is important to note that this program should not be used for any illegal activities, and we strongly encourage all users to respect the terms and conditions of the 1secmail service.


### teste
teste

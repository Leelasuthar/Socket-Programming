# Socket Programming for Global Client-Server Communication
## Overview

This project demonstrates a simple client-server architecture using socket programming in Python. The server listens for incoming client connections and exchanges messages with the client. The goal is to establish communication between two systems located anywhere in the world over the internet.This guide includes setting up port forwarding and ensuring that both systems (client and server) can communicate globally through the internet.

## Features
Bi-directional communication between client and server.
Uses TCP/IP sockets for reliable message delivery.
Custom messages from the server based on client input.
Setup for global connectivity through port forwarding.

## Client-Server Architecture
Server: The server listens on a specified port for incoming client connections. Once a connection is established, it continuously receives and sends messages to the client.

## Client:
The client connects to the server's public IP address and exchanges messages with the server. The client can send its data, and the server will reply with a custom message.


## Prerequisites
Python 3.x installed on both the client and server systems.
A working internet connection.
Administrative access to the server’s network/router for port forwarding setup.
Global Connectivity Setup

### 1. Configure Port Forwarding (for Server)
To allow global access to your server, you'll need to configure port forwarding on your router:
Log into your router’s configuration page (usually accessed by typing the router's IP address into a web browser).
Locate the Port Forwarding settings (may vary depending on the router model).
Forward TCP traffic on a specific port (e.g., 12345) to your server’s local IP address.
Internal IP: The local IP of the machine where the server is running.
Internal Port: The port on which your server is listening (e.g., 12345).
External Port: The same port number (12345) or another port to be used by the client for external access.

### 2. Check Your Public IP Address
The client needs your public IP address to connect to your server. You can find your public IP by visiting a site like WhatIsMyIP.
Share this public IP with your friend who will run the client program.

### 3. Configure Firewall Settings (for Server)
Ensure that your server's firewall is configured to allow incoming traffic on the port you are using (e.g., 12345):
On Windows: Add a new inbound rule in the Windows Defender Firewall to allow traffic on the specified port.
On Linux: Use iptables or ufw to allow the port:
bash
Copy code
sudo ufw allow 12345/tcp

### 4. Run the Server
Once the port is forwarded and the firewall is set, run the server on your local machine. It will now be accessible via the public IP address and the forwarded port.

### 5. Run the Client
On your friend's system (or any external machine), the client should connect to your public IP address and the forwarded port (e.g., 12345). The client can now exchange messages with the server.
Security Considerations When exposing a server to the internet, take these security measures:
Use firewalls to restrict access to only known IP addresses.
Monitor traffic for any unusual activity.
Consider implementing encryption (e.g., TLS/SSL) for secure communication between client and server.
Steps to Run Locally
## Server:
Run the server code on your local machine.
The server will listen for incoming connections on the specified port.
## Client:
Run the client code on another terminal or a different machine.
The client will connect to the server and send messages.
The server will receive the messages and send custom replies back to the client.
### Example Usage
Client input: John
Server reply: Hello Good morning !!!! ::: John
### Requirements
Python 3.x
Internet connectivity for global client-server communication
### License
This project is licensed under the MIT License - see the LICENSE file for details.

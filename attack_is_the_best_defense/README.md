# attack_is_the_best_defense

### Task 0: ARP Spoofing and Sniffing Unencrypted Traffic
This task involves using `tcpdump` to sniff unencrypted traffic and extract sensitive information (in this case, a password sent over Telnet). The challenge provides a script (`user_authenticating_into_server`) that simulates the authentication steps with a mocked-up server. The goal is to sniff the network using `tcpdump` and find the password sent during the authentication process.

### Task 1: Dictionary Attack
This task aims to showcase the weakness of password-based authentication by performing a dictionary attack on an SSH account. It requires Docker installation, pulling and running a Docker image (`sylvainkalache/264-1`), finding a password dictionary, and using `hydra` to attempt a brute force attack on the SSH account (`sylvain`) within the Docker container.

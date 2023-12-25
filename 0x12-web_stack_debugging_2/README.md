# 0x12-web_stack_debugging_2

### Task 0: Run software as another user
- **Objective**: Run the `whoami` command as a specified user using a Bash script.
- **Solution**: Create a Bash script (`0-iamsomeoneelse`) that accepts a username as an argument and runs the `whoami` command under that user.

### Task 1: Run Nginx as Nginx
- **Objective**: Configure Nginx to run as the `nginx` user rather than as the `root` user.
- **Solution**: Write a Bash script (`1-run_nginx_as_nginx`) that configures Nginx to run as the `nginx` user, listen on all active IPs on port 8080, and ensures it's functioning correctly under this user.

### Task 2: 7 lines or less
- **Objective**: Make the fix for Task 1 concise and within 7 lines in a Bash script.
- **Solution**: Create a Bash script (`100-fix_in_7_lines_or_less`) that resolves the Nginx user issue within 7 lines without using `;`, `&&`, or `wget`.

Each task involves writing Bash scripts to manage users or alter the process execution permissions, ensuring best practices by avoiding running processes like Nginx as the root user, thereby enhancing system security.

# 0x1B-web_stack_debugging_4

# Postmortem: Enhancing Nginx Performance Under Load

## Incident Summary

During a web stack debugging task, I observed a significant number of failed requests while testing the performance of our web server setup featuring Nginx under pressure.
The initial benchmark using ApacheBench (ab) revealed 943 failed requests out of 2000, prompting investigation and remediation.

## Root Cause

The root cause of the failed requests was traced to the default ulimit settings for file descriptors on the Nginx server.
The initial ulimit setting was insufficient to handle the concurrency level and load imposed during the ApacheBench test.

## Incident Timeline

- **0.353 seconds:** Initial benchmarking using ApacheBench completed with 943 failed requests.
  
- **Puppet Configuration (0-the_sky_is_the_limit_not.pp):**
  - The ulimit settings was increased in the Nginx default configuration file (`/etc/default/nginx`) to a more appropriate value (4096).
  - Nginx was then restarted to apply the changes.

- **0.301 seconds:** Subsequent benchmarking after applying the Puppet configuration resulted in zero failed requests, indicating a successful mitigation.

## Remediation Steps

### 1. Puppet Configuration
The main remediation involved adjusting the ulimit settings for file descriptors in the Nginx default configuration file using Puppet.
The configuration file was updated to increase the ulimit from the default value to 4096. Additionally, Nginx was restarted to apply the changes.

```puppet
# Increase the ULIMIT of the default file
file { 'fix-for-nginx':
  ensure  => 'file',
  path    => '/etc/default/nginx',
  content => inline_template('<%= File.read("/etc/default/nginx").gsub(/15/, "4096") %>'),
}

# Restart Nginx
-> exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/',
}
```
### 2. Verification
Following the configuration change, a second round of benchmarking using ApacheBench showed a substantial improvement.
The number of failed requests dropped to zero, and the server demonstrated increased performance, handling the load more efficiently.

## Lessons Learned

1. **Regularly Review and Adjust Ulimits**
   - Ulimits play a crucial role in determining system resource limits.Regularly review and adjust ulimit settings based on the expected load and concurrency levels.

2. **Effective Logging for Debugging**
   - Logs proved invaluable during the debugging process. Ensure thorough logging, especially during performance testing, to quickly identify and address issues.

3. **Automation for Configuration Changes**
   - Leverage automation tools like Puppet for making configuration changes. This ensures consistency and reduces the risk of human error.

4. **Gradual Load Testing**
   - When conducting load testing, consider starting with a lower concurrency level and gradually increasing it.
    This allows for a more controlled approach to identify optimal server configurations.

## Conclusion

The incident highlighted the importance of fine-tuning system parameters, such as ulimit settings, to ensure the web server can handle varying levels of traffic effectively.
By promptly identifying and addressing the root cause, I was able to optimize the Nginx server and improve its performance under pressure.
Ongoing monitoring and periodic reviews of server configurations will be essential to maintaining optimal performance as traffic patterns evolve.


# 1. User limit
## advanced

# Postmortem: Resolving User Holberton Login Errors

## Incident Summary

User Holberton experienced login errors, encountering "Too many open files" messages while trying to open files. The issue was identified as a result of reaching the file limits for the user, leading to login failures and errors when interacting with the system.

## Root Cause

The root cause of the login errors for User Holberton was a low file limit set for the user in the OS configuration. The initial ulimit settings were insufficient for Holberton's operations, leading to errors when attempting to log in and open files.

## Incident Timeline

- **Initial Observation:**
  - Holberton attempts to log in, but errors such as "Too many open files" prevent successful login and file operations.

- **Puppet Configuration (1-user_limit.pp):**
  - Puppet configuration script (`1-user_limit.pp`) was applied to increase both hard and soft file limits for the Holberton user in `/etc/security/limits.conf`.

- **Verification:**
  - After applying the Puppet configuration, a successful login was observed for User Holberton, and file operations were performed without encountering "Too many open files" errors.

## Remediation Steps

### 1. Puppet Configuration
The primary remediation involved adjusting the hard and soft file limits for User Holberton in the `/etc/security/limits.conf` file using Puppet. Both the hard and soft limits were increased to 50,000.

```puppet
# Fix user Holberton login errors

# Increase hard limit for user holberton
exec { 'increase-hard-file-limit-for-holberton-user':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# Increase soft limit for user holberton
exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
```

### 2. Verification
Following the application of the Puppet configuration, a successful login for User Holberton was confirmed. Subsequent operations, including file access, were performed without encountering any "Too many open files" errors.

## Lessons Learned

1. **User-Specific Configurations:**
   - User-specific configurations, such as file limits, should be carefully reviewed and adjusted based on the user's requirements and usage patterns.

2. **Automation for User Configurations:**
   - Leverage automation tools like Puppet for making user-specific configuration changes. This ensures consistency and reduces the risk of manual errors.

3. **Regular User Testing:**
   - Periodically test user accounts, especially those with specific requirements, to identify and address potential issues before they impact operations.

4. **Effective Monitoring and Logging:**
   - Regularly monitor system logs for user-specific errors and implement alerts to detect and address issues promptly.

## Conclusion

By identifying and addressing the low file limits for User Holberton through Puppet automation, we successfully resolved the login errors and file access issues. The incident emphasizes the importance of user-specific configurations and the use of automation tools to maintain consistent and optimized user environments. Ongoing monitoring and periodic reviews of user configurations will be essential for preventing similar issues in the future.

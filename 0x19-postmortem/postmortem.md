Incident Report for 503 Error / Site Outage

![Alt Text](image/README/meme.png)

Summary
On May 10th, 2024 at 2:00 AM, the server access went down, resulting in a 503 error for anyone trying to access the website. The server is based on a LAMP stack.

Timeline
02:00 PST - Users reported a 503 error when attempting to access the website.
02:05 PST - Checked the server status to ensure Apache and MySQL were running.
02:10 PST - The website was not loading properly, even though the server and database were functioning correctly.
02:12 PST - A quick restart of the Apache server resulted in a status of 200 and OK when curling the website.
02:18 PST - Reviewed error logs to identify the source of the error.
02:25 PST - Checked /var/log to find that the Apache server was being prematurely shut down. No error logs for PHP were found.
02:30 PST - Discovered that error logging in php.ini was turned off. Enabled error logging.
02:32 PST - Restarted the Apache server and monitored the error logs for PHP.
02:36 PST - Found errors in the PHP logs indicating a misspelled file name in wp-settings.php.
02:38 PST - Corrected the file name and restarted the Apache server.
02:40 PST - Server resumed normal operation, and the website loaded properly.

Root Cause and Resolution
The issue stemmed from a misspelled file name referenced in the wp-settings.php file, resulting in a 500 error when attempting to access the server. Upon investigation, it was discovered that PHP error logging was disabled, making it difficult to identify the source of the error initially. After enabling error logging and restarting the Apache server, the misspelled file name was identified and corrected. It is possible that this error may have occurred on other servers as well. To prevent similar incidents, a deployment of Puppet code was performed to correct any misspelled file extensions across all servers.

Corrective and Preventive Measures

Ensure that error logging is enabled on all servers to facilitate easy identification of errors.
Conduct thorough testing of servers and websites locally before deployment to a multi-server setup to catch and correct errors before they impact live environments.

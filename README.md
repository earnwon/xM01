Prepared by Ernesto Wong.

Please find enclosed the files requested by Adam Serediuk as part of the assignment for the interview for the QA Engineer for Operations position at xMatters.
Sections
   A. Setup 
   B. Test Cases

A. Setup

- Set up a new GIT account and a repository for this assignment
- Download the latest version of 64-bit CentOS 7 (RHEL 7 Update 1, CentOS-7-x86_64-DVD-1503-01)
- Installed CentOS as a "Basic Web Server" (no GUI) along with the following add ons:
	Dev tools
	Compatibility with earlier versions of RedHat/CentOS
	FTP
	File
	Java
	PHP
	Python
	Guest Agents
	Perf Tools
Auto partitioning

- Tested that git, python (ver. 2.7.5) and php were installed
- Apache: Made sure that it was running.  overrode /usr/share/httpd/noindex/index.html with a new file in the html directory (e.g.    /var/www/html/index.html )
- Turned on port 80 (http) in the firewall
- Installed PIP since it's the preferred method to install django
- Installed Django (ver. 1.8.1) and confirmed its successful installation
	 python -c "import django; print(django.get_version())"
- Installed Fabric (ver. 1.10.1) and  Paramiko (ver.1.15.2)
   No errors encountered, e.g. DistributionNotFound: paramiko>=1.10 error which I've seen before didn't appear)
- Tested if Fabric worked
	python -c "import fabric.version; print(fabric.version.get_version())"
        fab --version
- Installed Puppet and tested installation of Puppet and its module facter
	facter puppetversion
		(ver. 3.7.5)
- Installed boto and tested installation
        print boto.Version
		(ver. 2.38.0)
- Tested connectivity with Amazon using my account as well as the access and secret access keys and keyvalue pair file.

B.  Test Cases
Note that the boot default configuration file (boot.cfg) uses a different format from the one used by LinkOverflow (.aws.settings)

*Test 1 Check if boot  was installed correctly

*Test 2 Check if boto can read the access and secret access keys in boot.cfg

Test 3 Check if the launcher behaves correctly with no parameters
	python launch.py
	Expected: launch.py: error: too few arguments
        usage: launch.py [-h] [--aws-config <file>] [--system-config <file>] <django_proj> <num_servers>

Test 4  Check if the launcher behaves correctly with one parameter, e.g. the AWS config file
	python launch.py	--aws-config aws.py
	Expected:  launch.py: error: too few arguments

Test 5  Check if the launcher behaves correctly with three parameter including the AWS config file, Django project and number of servers
	# python launch.py --aws-config aws.py myblog 1
        Expected: ?
        Actual:  launch.py: error: argument num_servers: invalid int value: 'myblog'

Test 6  Check if the launcher behaves correctly with two parameters but without a config file
	# python launch.py myblog 1
         Expected: Error: AWS settings file (/root/.aws.settings) is missing.

Test 7  Check if the launcher behaves correctly with two parameters but without a proper config file, e.g. use boot.cfg which has a different format
	# python launch.py myblog 1
        Expected:  Error: AWS settings file (/root/.aws.settings): No section: 'EC2'

Test 8  Check if the launcher behaves correctly without a private key file or with one that's misconfigured
	# python launch.py myblog 1
        Expected: Error: SSH private key file (/home/<user>/LinkOverflow-keys.pem) is missing.

Test 9 Use a correct private key file but which is not defined for the zone you are invoking the image on
	# python launch.py myblog 1
        Creating 1 EC2 instances
        - In AWS Availability Zone: us-west-2
        - Using EC2 Instance Image: ami-c7d092f7
        - And EC2 Instance Type: t2.micro
        - Loading Django project from: myblog

        Please wait for EC2 instances to start up... (may take several minutes)

        Expected: A more descriptive error message, the current one used is misleading
        Actual: AWS KeyPair LinkOverflow-keys is not defined. Use the AWS console to create it.

Test 10 Invoke an image that the user doesn't have access to E.g. ami-c7d092f7
	# python launch.py myblog 1
        Expected: A more descriptive error message, the current one used is misleading
        Actual:  Error: Unable to launch EC2 instances.
        Detailed message from server was EC2ResponseError: 400 Bad Request
<?xml version="1.0" encoding="UTF-8"?>
<Response><Errors><Error><Code>InvalidAMIID.NotFound</Code><Message>The image id '[ami-c7d092f7]' does not exist</Message></Error></Errors><RequestID>2faa7d19-2406-40a4-bcd0-4711a4918d2a</RequestID></Response>

SOLUTION: Sign up for the AWS market place. This test case tests a possible change of accounts or environments where things work in one account but not the other.

Test 11 Invoke two images, make sure the IP printed is correct (compare against AWS Console)
	# python launch.py myblog 2
        Expected: E.g.
        [52.24.220.58] Executing task '__installpuppettask__'
        [52.24.220.58] run: sudo rpm -i --force --quiet http://yum.puppetlabs.com/puppetlabs-release-el-7.noarch.rpm

Test 12 Invoke two images, make sure software reacts correctly in the case of timeout
	# python launch.py myblog 2
        Expected: E.g.
        [52.10.85.76] Executing task '__installpuppettask__'
        [52.10.85.76] run: sudo rpm -i --force --quiet http://yum.puppetlabs.com/puppetlabs-release-el-7.noarch.rpm
        Fatal error: Timed out trying to connect to 52.24.43.184 (tried 1 time)

        Underlying exception:
            timed out

        Aborting.
        Timed out trying to connect to 52.10.85.76  (tried 1 time)

        Underlying exception:
            timed out

End.

Prepared by Ernesto Wong.

Please find enclosed the files requested by Adam Serediuk as part of the assignment for the interview for the QA Engineer for Operations position at xMatters.

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



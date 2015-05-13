# Test2: Check connection
import boto.ec2
boto.set_stream_logger('boto')
# credentials could be in
#    a) etc/boto.cfg
#    b) ~/.boto
# You should see the message "Using access key found in config file"
# regardless of whether the values are valid or not
ec2 = boto.ec2.connect_to_region('us-west-2')

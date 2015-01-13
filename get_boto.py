import sys
import boto
import boto.s3

# AWS ACCESS DETAILS
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''

# a bucket associated to the current author
bucket_name = 'boto-demo-1421108796'
conn = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
bucket = conn.create_bucket(bucket_name, location=boto.s3.connection.Location.DEFAULT)


# retrieve a specific bucket
bucket = conn.get_bucket(bucket_name)

# possible key, the file name
key = bucket.get_key('my test file')
# retrieve key value to file named test_elisha.jpg
key.get_contents_to_filename('test_elisha.jpg')

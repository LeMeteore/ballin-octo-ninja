import sys
import boto
import boto.s3

# AWS ACCESS DETAILS
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''

# a bucket per author maybe
bucket_name = 'boto-demo-1421108796'
conn = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
bucket = conn.create_bucket(bucket_name, location=boto.s3.connection.Location.DEFAULT)
uploadfile = sys.argv[1]

print('Uploading %s to Amazon S3 bucket %s' % (uploadfile, bucket_name))

def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()

from boto.s3.key import Key
k = Key(bucket)

# the key, should be the file name
k.key = str(uploadfile)
# the key value
k.set_contents_from_filename(uploadfile, cb=percent_cb, num_cb=10)

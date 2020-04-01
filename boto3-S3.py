#%%
import boto3
from botocore.exceptions import ClientError

# IAM 유저 생성 후 받은 키 입력
my_id = "YOUR_ID"
my_key = "YOUR_KEY"

#%%
s3=boto3.client("s3",aws_access_key_id=my_id,aws_secret_access_key=my_key)


def create_s3_bucket(bucket_name):
    print("Creating a bucket... " + bucket_name)

    s3 = boto3.client(
        's3',  # 사용할 서비스 이름, ec2이면 'ec2', s3이면 's3', dynamodb이면 'dynamodb'
        aws_access_key_id=my_id,    # 액세스 키
        aws_secret_access_key=my_key)    # 비밀 엑세스 키

    try:
        response = s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': 'ap-northeast-2' #Seoul  # us-east-1을 제외한 지역은 LocationConstraint 명시해야함.
            }
        )
        return response
    except ClientError as e:
        if e.response['Error']['Code'] == 'BucketAlreadyOwnedByYou':
            print("Bucket already exists. skipping..")
        else:
            print("Unknown error, exit..")


def main():
    response = create_s3_bucket("myfirstbucket-geeky")
    print("Bucket : " + str(response))


main()
# %%
# 파일 올리기
import os 
import glob
os.getcwd()
input_path = "G:/내 드라이브/"
files        = glob.glob(os.path.join(input_path,'(before)*'))
stored_names =  list(map(lambda x: x.split("\\")[1], files))
# %%
for file,name in zip(files,stored_names):
    s3.upload_file(file,"myfirstbucket-geeky",name)

# %%

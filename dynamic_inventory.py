#!/usr/bin/env python3
import boto3
import json

ec2 = boto3.resource('ec2', region_name='us-east-1')

def get_instances():
    hosts = {"webservers": {"hosts": [], "vars": {}}}
    for instance in ec2.instances.all():
        if instance.state['Name'] == 'running':
            name_tag = next((tag['Value'] for tag in instance.tags if tag['Key'] == 'Name'), '')
            if "Webserver-3" in name_tag or "Webserver-4" in name_tag:
                hosts["webservers"]["hosts"].append(instance.public_ip_address)
    return {"_meta": {"hostvars": {}}, **hosts}

print(json.dumps(get_instances()))

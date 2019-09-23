# ICACT2020

## Environment
- ubuntu-18.04 LTS vCPU 12, 32GB memory
- [CBMC 5.11](http://www.cprover.org/cbmc/download/cbmc-5-11-linux-64.tgz)

## Command
```python
#Connecting to instances
ssh -i ~/.ssh/gcp-key id@ip

#Transferring Files to Instances
scp -i ~/.ssh/gcp-key file.txt id@ip:/path
```
- [GCP: Managing SSH keys in metadata](https://cloud.google.com/compute/docs/instances/adding-removing-ssh-keys)
- [GCP: Transferring Files to Instances](https://cloud.google.com/compute/docs/instances/transfer-files)

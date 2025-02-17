# ICACT2020

## Environment
- ubuntu-18.04 LTS vCPU 12, 32GB memory
- [CBMC 5.11](http://www.cprover.org/cbmc/download/cbmc-5-11-linux-64.tgz)
```command
$ apt install python
$ apt install gcc
```
## Environment Variables
```command
$ vi ~/.bashrc
$ export PATH=$PATH:/path
$ source ~/.bashrc
```
- [EnvironmentVariables](https://help.ubuntu.com/community/EnvironmentVariables)

## GCP Command
```command
# Connecting to instances
$ ssh -i ~/.ssh/gcp-key id@ip

# Transferring Files to Instances
$ scp -i ~/.ssh/gcp-key file.txt id@ip:/path
```
- [GCP: Managing SSH keys in metadata](https://cloud.google.com/compute/docs/instances/adding-removing-ssh-keys)
- [GCP: Transferring Files to Instances](https://cloud.google.com/compute/docs/instances/transfer-files)

## Ubuntu Command
```command
# Compressing files with tar
$ tar -cvf folder.tar ./folder
$ tar -cvf file.tar file.txt

# Extracting the contents of a tar file
$ tar -xvf folder.tar

# Copying a file to another directory
$ cp filename /path

# Running a Python Script in the Background
$ nohup python file.py &

# Displaying the status of jobs that were started in the current shell environment
$ jobs
```
- [How to compress files with tar command on Linux/Unix](https://www.cyberciti.biz/faq/tar-compress-command-on-linux-unix-to-create-tarball/)
- [Linux Copy File Command](https://www.cyberciti.biz/faq/copy-command/)
- [Differences between “<command> & disown” and “nohup <command> & disown”](https://askubuntu.com/questions/611968/differences-between-command-disown-and-nohup-command-disown)
- [Ubuntu Manpage: jobs](http://manpages.ubuntu.com/manpages/trusty/man1/jobs.1posix.html)

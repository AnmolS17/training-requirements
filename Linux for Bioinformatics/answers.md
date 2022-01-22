# Answers to questions from "Linux for Bioinformatics"  

**Q1. What is your home directory?**  

*A1.* `/home/ubuntu`  

**Q2. What is the output of this command?**  
 
*A2.* `my_folder/` `ls`->`"hello_world.txt"`.   

 **Q3. What is the output of each `ls` command?**  

*A3.* 1. For `my_folder/` `ls` -> no output;  
    2. For `my_folder2/` `ls`-> `"hello_world.txt"`.   

**Q4. What is the output of each?**  

*A4.* 1. For `my_folder/` `ls` -> no output;  
    2. For `my_folder2/` `ls` -> no output;  
    3. For `my_folder3/` `ls`-> `"hello_world.txt"`.  
	
**Q5. What editor did you use and what was the command to save your file changes?**    

*A5.* I used `nano`. There are two methods to save:   
	 1. `Ctrl + O`: To save the file changes.   
	 2. `Ctrl + X`: To exit nano, here you are also prompted to save your file. This makes it work as a *save and exit* command.  

**Q6. What is the error?**  

*A6.* After changing the user to `sudouser`, i.e., `sudouser@IPv4/DNS`(Have to change the username to `sudouser` in the `ssh` command) in the shell.    
     *Output*-> `sudouser@ec2-xx-x-xxx-xxx.ap-south-1.compute.amazonaws.com: Permission denied (publickey).` on terminal.  
              `Server refused our key   No supported authentication methods available (server sent: publickey)` using MobaXterm.   
     *Explanation:* After checking the files in both the user directory by using `ls -alh`.  
	 I came to know that user `ubuntu` user had `.ssh` directory, but `sudouser` didn't have the `.ssh` directory.  
	 This meant that `sudouser` couldn't connect by using `ssh` because it didn't have the key pair(private key) to do so, this data exist in `.ssh`.   


**Q7. What was the solution?**  

*A7.* By creating a `.ssh` directory in the `sudouser`. Then add a key-pair(private key) to it.   
    *Steps:*    
    1. Connect using `ubuntu` username -> command: `su - sudouser`   
    2. command: `mkdir .ssh` -> command: `chmod 700 .ssh/`; i.e. create `.ssh` directory -> change its permissions.    
    3. command: `cd .ssh/` -> command: `touch authorized_keys` -> command:`chmod 600 authorized_keys`;  
	   i.e. go to `.ssh/` -> add `authorized_key` as a key -> change its permission.    
    4. Create a new keypair in AWS or use the existing `*.pem` key you have.    
    5. In your host PC -> go to terminal -> command: `ssh-keygen -y` (OpenSSH) -> select the public key -> copy it (It will be a *SSH RSA* key).    
    6. Go to the `sudouser` -> command: `nano authorized_keys` -> paste the key-> save and exit.     
    7. Connect to the `sudouser` -> using terminal : command: `ssh -i "bioinf.pem" sudouser@ec2-xx-x-xxx-xxx.ap-south-1.compute.amazonaws.com`, or using MobaXterm  
    *Reference:*   
    [2FA and SSH](https://aws.amazon.com/blogs/startups/securing-ssh-to-amazon-ec2-linux-hosts/) -> This consist of how how to manage the users,  
	              i.e. the commands and steps used to add key-pair for the `sudouser`. This also consists of adding 2FA for your EC2 instance.    
    [2FA from security group option](https://aws.amazon.com/blogs/security/how-to-enable-mfa-protection-on-your-aws-api-calls/) -> To add 2FA from security group options.   
    [Adding new User accounts](https://aws.amazon.com/premiumsupport/knowledge-center/new-user-accounts-linux-instance/)   
    

**Q8. What does the `sudo docker run` part of the command do? and what does the `salmon swim` part of the command do?**  

*A8.* `sudo docker run`: `sudo` to provide the privilege to run the command as root user/ superuser;  
     `docker run` command first creates a writable container layer over the specified image(here "combinelab/salmon") and then starts it using the specified command.  
     `salmon swim`: `salmon` is a program to produce highly-accurate, transcript-level quantification estimates from RNA-seq data.   
     `swim` command is used to perform a super-secret operation  
    
**Q9. What is the output of this command?**  

*A9.* Command: `sudo ls /root` -> password ->  
    The output: `serveruser is not in the sudoers file.  This incident will be reported.`   

**Q10. What is the output of `flask --version`?**  

*A10.* The output of `flask --version`: 
     ```Python 3.9.5
        Flask 2.0.2
        Werkzeug 2.0.2 ```  

**Q11. What is the output of `mamba -V`?**  

*A11.* The output of `mamba -V` : `conda 4.11.0`   

**Q12. What is the output of `which python`?**  

*A12.* Command: `mamba init` -> restart current shell-> command: `mamba activate py27` ->   
      command: `which python` -> `/home/serveruser/miniconda3/envs/py27/bin/python`  

**Q13. What is the output of `which python` now?**  

*A13:* Command: `mamba deactivate` -> command: `which python` ->  
     `/home/serveruser/miniconda3/bin/python`  

**Q14. What is the output of `salmon -h`?**  

*A14.* The output of `salmon -h` in `salmonEnv` environment:  

``` 
salmon v1.4.0

Usage:  salmon -h|--help or
        salmon -v|--version or
        salmon -c|--cite or
        salmon [--no-version-check] <COMMAND> [-h | options]

Commands:
     index      : create a salmon index
     quant      : quantify a sample
     alevin     : single cell analysis
     swim       : perform super-secret operation
     quantmerge : merge multiple quantifications into a single file 
```

**Q15. What does the `-o athal.fa.gz` part of the command do?**   

*A15.* It writes the output of the `curl ftp://ftp.ensemblgenomes.org/.../Arabidopsis_thaliana.TAIR10.28.cdna.all.fa.gz` into `athal.ga.gz` file.  

**Q16. What is a `.gz` file?**  

*A16.* The `.gz` extension in a file signifies that it is an archive compressed using `Gzip` compression technology.   

**Q17. What does the `zcat` command do?**  

*A17.* Command `zcat` reads one or more files that have been compressed with `gzip` or compress and write them to standard output. Here it is used to read the `athal.ga.gz`.  

**Q18. What does the `head` command do?**  

*A18.* The `head` command prints the top `N` number of data of the given input. By default, it prints the first `10` lines of the file.  

**Q19. what does the number `100` signify in the command?**  

*A19.* The number `100` signifies that the first `100` lines of the given input are to be printed.  

**Q20. What is `|` doing?**  

*A20.* It allows the `stdout`(output) of a command to be connected to `stdin`(input) of another.  
	 This means, that the output of the `zcat` command is taken in as input by the `head` command.  

**Q21. What is a `.fa` file? What is this file format used for?**  

*A21.* A `*.fa` is the file extension related to bioinformatics and biochemistry, they use the `FASTA` format.  
	 `FASTA` format is a text-based format used to store one or many nucleotides or amino acids sequences in a single file.  
	 Each sequence starts with `>` followed by a sequence header in the first line and the sequence in the next line.  

**Q22. What format are the downloaded sequencing reads in?**  

*A22.* The file was downloaded in `SRR074122/` directory.  
     The file name was `SRR074122.sra`. `.sra` stands for **Sequence Read Archeive**.  

**Q23. What is the total size of the disk?**  

*A23.*  7.7 GB  

**Q24. How much space is remaining on the disk?**  

*A24.* 3.0 GB  

**Q25. What went wrong?**  

*A25.* The system storage got exhausted during the conversion of `.sra` to `.fastq`.  

**Q26: What was your solution?**  

*A26.* First, delete the incomplete .fastq file by rm command.  
     Secondly, the solution is to compress the output file to `Gzip`, i.e. `*.gz` format.  
     Final Command: `fastq-dump --gzip SRR074122`  

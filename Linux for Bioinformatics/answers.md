# Answers to questions from "Linux for Bioinformatics"
Q1. What is your home directory?    

A1: /home/ubuntu

Q2. What is the output of this command?   

A2: my_folder/ ls->"hello_world.txt".   

Q3. What is the output of each ls command?   

A3: 1. For my_folder/ ls -> no output;  
    2. For my_folder2/ ls-> "hello_world.txt".   

Q4. What is the output of each?   

A4: 1. For my_folder/ ls -> no output;  
    2. For my_folder2/ ls -> no output;  
    3. For my_folder3/ ls-> "hello_world.txt".

Q5. Why didn't that work?   

A5. After changing the user to sudouser, i.e., sudouser@IPv4/DNS(Have to change the username to sudouser in the ssh command) in shell.   
Output-> "sudouser@ec2-xx-x-xxx-xxx.ap-south-1.compute.amazonaws.com: Permission denied (publickey)."   
 
Explaination: After checking the files in both the user directory by using "ls -alh". I came to know that ubuntu user had ".ssh" directory, but sudouser didn't has the ".ssh" directory. This meant that sudouser coudn't connect by using ssh because it didn't had the key pair(private key) to do so, this data exist in ".ssh".   


Q6. What was the solution?   

A6. By creating an ".ssh" directory in the sudouser. Then adding a key-pair(private key) to it.   

   Steps:    
    1. su - sudouser   
    2. mkdir .ssh -> chmod 700 .ssh/; # create .ssh directory -> change its permissions.   
    3. cd .ssh/ -> touch authorized_keys -> chmod 600 authorized_keys ; go to .ssh/ -> add authorized_key as a key -> change its permission.   
    4. Create a new keypair in AWS or use the existing *.pem key you have.   
    5. In your host PC -> go to terminal -> ssh-keygen -y (OpenSSH) -> select the public key -> copy it (It will be a SSH RSA key).   
    6. Go to the sudouser -> vi authorized_keys -> paste the key-> save and exit.   
    7. Connect to the new user -> ssh -i "bioinf.pem" sudouser@ec2-xx-x-xxx-xxx.ap-south-1.compute.amazonaws.com   
    
   Reference:   
     [2FA and SSH](https://aws.amazon.com/blogs/startups/securing-ssh-to-amazon-ec2-linux-hosts/) -> This consist of how how to manage the users, i.e. the commands and steps used to add key-pair for the sudouser. This also consists of adding 2FA for your EC2 instance.    
    [2FA from security group option](https://aws.amazon.com/blogs/security/how-to-enable-mfa-protection-on-your-aws-api-calls/) -> To add 2FA from security group options.   
    [Adding new User accounts](https://aws.amazon.com/premiumsupport/knowledge-center/new-user-accounts-linux-instance/)  
    
    

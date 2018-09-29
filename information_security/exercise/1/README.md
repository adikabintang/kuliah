# Notes from the exercise 1
## Part A
ssh cloud-user@infosec1.vikaa.fi -p 32957

## Part B
For example:

groupname: project2018

name: alice, bob, carol

### Create a group (requires sudo)
```
groupadd project2018
```
### Delete a group (requires sudo)
```
groupdel project2018
```
### Create a user and add to group project2018 (requires sudo)
```
useradd -m alice -G project2018
useradd -m bob -G project2018
useradd -m carol -G project2018
```
### Set password for user alice, bob, and carol (requires sudo)
```
passwd alice
passwd bob
passwd carol
```
### Set folder ownership of $HOME/project to alice and group project2018
```
sudo chown -R alice:project2018 project/
```
### Move the folder project from $HOME/project to /home/alice/project
```
sudo mv $HOME/project/ /home/alice/
```
### In order to `ls` to be able to execute to alice from another user, set this
```
sudo chmod 701 /home/alice
```
### Switch user to `alice`
```
su - alice
```
### From now on, execute these as `alice`
#### Only the members of project2018 can view and write the `project/code` subdirectory and its files
```
chmod -R 771 project/code
```
#### Any logged-in user can run the project demo. The executable file is called `project/code/poc`
```
chmod 711 project/code/poc
```
#### Only alice, who is the project manager, has access to the confidential directory and its contents
```
chmod -R 700 confidential/
```
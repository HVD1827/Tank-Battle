# Tank Battle
#### This is a tank game including:
* A single server
* Multiple users
* Multiple devices per user
* A password for each device which is used for authentication
* Multiple users can share same device but the only way for authentication is the device password hence it will be same for different users. What can be done to prevent this sharing of password is maybe limiting 1 user per device or creating different passwords for each user-device pair which will be unique across all users.  

#### Running:
* Clone the repository.
* Run `g++ main.cpp Device.cpp User.cpp UserInfo.cpp Server.cpp` on the command line or terminal.
* Run `./a.exe` or `./a.out` to execute the program.

#### How to use:
* You are required to enter N, that is the number of devices available.
* Following next N lines guide you in entering the device id and the corresponding password.
* Then you are required to enter the server name (as per your choice).
* Now you are required to enter the operation you want to perform.
* Three types of operations are supported:
    * **Register** - The command prompt/ terminal will guide you to enter username. To perform this just enter `R` and then command prompt will guide you accordigly.
    * **Sign-in** - For this the you are supposed to enter your password for the device additionally.  To perform this just enter `S` and then command prompt will guide you accordigly.
    * **Print users** - This prints the username of the users registered with the server. This data is not actually open to the users, but is limited to the server. But we can perform this to check the functionality. To perform this just enter `P`. 

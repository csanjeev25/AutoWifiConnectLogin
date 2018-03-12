# AutoWifiConnectLogin
An Python script to automatically connect to a wifi and then automate its login page,fill details and login.
This script allows to automatically connect to my college wifi, automate fills login page for network ssid and you are logged in.

For personal use,
Change network ssid,password,login url fo your preferred network ssid,
download or git clone https://github.com/csanjeev25/AutoWifiConnectLogin.git,
Then to run script at startup,
Open task Scheduler,
Click on create a task,(a dialog appears,
On General tab->give process a name,configure for your macine,and check on run with highest priviledges,
On Trigger tab->new->begin task on startup,
On actions tab->action->start a program,give location to auto_connect_login.pyw file,
On conditions tab ->Uncheck run only on battery

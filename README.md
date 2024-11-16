Step-By-Step guide to installing Poetry on Windows:
Open Windows Powershell: Navigate to your Start menu, type "Powershell", and select "Windows Powershell" from the search results.

Run Installation Command: In the Powershell window, paste the following command and press Enter:

Note: If you've installed Python through the Microsoft Store, replace py with python in the command below.
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
Wait for Installation to Complete: The installation process may take some time depending on your internet connection speed. Let it run until completion.

Copy Installation Path: Once the installation is complete, it will provide you with a path. Copy this path as you'll need to add it to your user environment variables.

Add Path to Environment Variables:

Right-click on the Start button and select "System".
In the System window, click on "Advanced system settings" on the left sidebar.
In the System Properties window, click on the "Environment Variables..." button.
In the Environment Variables window, under "User variables for [YourUsername]", find the "Path" variable and select it.
Click on the "Edit..." button.
In the Edit Environment Variable window, click on "New" and paste the path you copied from the installation process.
Click "OK" on all open windows to save your changes.
Close and Reopen Powershell: Close the Powershell window and open a new one.

Verify Installation: In the new Powershell window, type poetry --version and press Enter. If Poetry has been successfully installed, you should see its version number printed in the terminal.

You have now successfully installed Poetry on your Windows system. You can start using it for managing your Python projects.

//CD into the Folder and Create New Project Named Dashboard

poetry new dashboard --name src


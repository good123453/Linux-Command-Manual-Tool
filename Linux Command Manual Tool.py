# linux commmand Tool 

# 1️⃣ Navigation & Directory Commands


navigation_commands = {
    "pwd": "shows your current working directory",
    "cd": "changes the current directory",
    "ls": "lists files and folders in the current directory",
    "ls -la": "lists all files with detailed information (including hidden files)"
}



# 2️⃣ System & User Information
system_info_commands = {
    "whoami": "shows the current logged-in username",
    "uname -a": "shows system and kernel information",
    "history": "shows previously used commands",
    "clear": "clears the terminal screen"
}




# 3️⃣ Network Commands
network_commands = {
    "ifconfig": "shows network interface information (older systems)",
    "ip a": "shows detailed IP and network information",
    "iwconfig": "shows wireless network information",
    "ping": "checks connectivity to another host or website",
    "traceroute": "shows the route packets take to reach a host"
}






# 4️⃣ File & Directory Management
file_management_commands = {
    "mkdir": "creates a new directory",
    "rmdir": "removes an empty directory",
    "rm": "removes files or folders",
    "rm -rf": "forcefully removes files or folders (dangerous)",
    "cp": "copies files or directories",
    "mv": "moves or renames files or directories"
}






# 5️⃣ File Viewing & Reading
file_view_commands = {
    "cat": "displays file content",
    "less": "views file content page by page",
    "head": "shows the first lines of a file",
    "tail": "shows the last lines of a file"
}





# 6️⃣ Permissions & Ownership
permission_commands = {
    "chmod": "changes file permissions",
    "chown": "changes file ownership"
}





# 7️⃣ Process & Resource Monitoring
process_commands = {
    "ps": "shows running processes",
    "top": "shows live system processes and resource usage",
    "df -h": "shows disk usage in human-readable format",
    "du -sh": "shows size of a directory"
}






# 8️⃣ Admin / Power Commands
admin_commands = {
    "sudo": "runs a command with administrator (root) privileges",
    "sudo -su": "switches to root user shell",
    "reboot": "restarts the system",
    "shutdown": "shuts down the system",
    "exit": "closes the current terminal session"
}


def greeting() -> None:
    print("\nLinux Basic Command Manual Tool\n")


def Instructions():
    print("\n==================== TOOL INSTRUCTIONS ====================\n")

    print("📌 Purpose:")
    print("This tool is a learning-based command reference system.")
    print("It helps users understand Linux terminal commands by category.\n")

    print("📌 How this tool works:")
    print("You will see a list of command categories with numbers.")
    print("Each number represents a group of related commands.")
    print("Enter the number to view commands from that category.\n")

    print("📌 Command Categories:\n")
    print("1  -> Navigation & Directory Commands")
    print("2  -> System & User Information Commands")
    print("3  -> Network Commands")
    print("4  -> File & Directory Management Commands")
    print("5  -> File Viewing & Reading Commands")
    print("6  -> Permissions & Ownership Commands")
    print("7  -> Process & Resource Monitoring Commands")
    print("8  -> Admin / Power Commands\n")

    print("📌 How to use:")
    print("1. Run the program")
    print("2. Read the category list")
    print("3. Enter the number of the category you want to learn")
    print("4. The tool will show commands and their explanations\n")

    print("📌 Safety Notice:")
    print("- This tool does NOT execute any command")
    print("- It is for learning and reference only")
    print("- Some commands are powerful; always understand before using\n")

    print("📌 Tip:")
    print("Practice commands in a safe environment like a virtual machine.\n")

    print("===========================================================\n")





command_menu = {1 :"Navigation & Directory Commands",
                2 :"System & User Information Commands",
                3 :"Network Commands",
                4 :"File & Directory Management Commands",
                5 :"File Viewing & Reading Commands",
                6 :"Permissions & Ownership Commands",
                7 :"Process & Resource Monitoring Commands",
                8 :"Admin / Power Commands",
                9 :"help"}


commmand_list = {1 :navigation_commands,
                2 :system_info_commands,
                3 :network_commands,
                4 :file_management_commands,
                5 :file_view_commands,
                6 :permission_commands,
                7 :process_commands,
                8 :admin_commands,
                9 :"Wrong Choice!"}


def quit(choice):
    if choice == "y":
        return True
    return False

import time


greeting()

while True:
    
    time.sleep(1)
    
    print("\n\n Command Menu\n")
    
    for key , value in command_menu.items():
        print(f"{key}: {value} ")
        
        
    del key , value
    
    try:
        user = int(input("\n\nChoose the number: "))
    
    except ValueError:
        print("Invalid Choice!")
        continue
    
    except NameError:
        print("Invalid Choice!")
        continue
    
    command_category = commmand_list.get(user)
    
    
    print("\n\n Commands You Pick\n")
    if user in [1,2,3,4,5,6,7,8]:
        
        for key , value in command_category.items():
            print(f"{key}: {value}")
            
        print("\n\n")
        
    elif user in [9]:
        Instructions()    
        
        print("\n\n")
        
    else:
        print("Please Select 1 - 9")
        continue
    
    
    choice = input("You want to exit? (y/n): ")
    
    if quit(choice):
        print("THANKS FOR USING MY PROGRAM!")
        break
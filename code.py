import os


os.system("clear")
os.system("tput setaf 3")
print("           WELCOME TO BLOGGERS-CONTAINER WORLD  ")    # an interractive appraoch to run a docker taking input at the run time
print("           ---------------------------------   ")
os.system("tput setaf 7")
image=input("Enter the sqlimage name: ")
#volume=input("Enter the volume u want to mount: ")
mysql_rootpass=input("Enter the mysql root pass: ")
mysql_user=input("Enter the mysql username: ")
mysql_database=input("Enter the database name for joomla: ")
mysql_password=input(f"Enter the mysql password for {mysql_user}: ")

joomlaimage=input("Enter the joomlaimage name: ")
forjoomla_port=input("Enter the port of host to be exposed :")
docker_port=input("Enter the port where ur server is running :")
network=input("Enter the network name :")
os.system("tput setaf 4")

print("   creating a network with driver as bridge")
os.system("tput setaf 7")
os.system(f" docker  network create {network}")


basedock=f"{forjoomla_port}:{docker_port}"     #PAT:    HOST_PORT:SERVER_PORT(on container)



with open(".env","w") as ef:     #here the .env file is created every time when someone config asccording its requirements
                                     #and this .env file is what the docker compose first searches for the values where we have the 
                                      # placeholders in compose.yml file ${}
    ef.write(f"basedock={basedock}\n")
    ef.write(f"networkname={network}:\n")
    ef.write(f"imagename={image.rstrip()}\n")
    ef.write(f"joomlaimage={joomlaimage}\n")
    ef.write(f"mysql_rp={mysql_rootpass}\n")
    ef.write(f"mysql_uname={mysql_user}\n")
    ef.write(f"mysql_dbname={mysql_database}\n")
    ef.write(f"mysql_pass={mysql_password}\n")
os.system("tput setaf 5")
print("============== launching Joomla-Sql containers ===============")
os.system("tput setaf 7")
os.system(" docker-compose up -d")

print(f"JOOMLA Service running at  http://192.168.29.62:{forjoomla_port}")   #here i have hardcoded the value of ipaddress of the docker host as it will be treated as gateway  i must have use 
                                                                                 # ifconfig enp0s3 |grep "[number]{3}.[number]{2-3}.[number]{2-3}.{number]{2-3}"





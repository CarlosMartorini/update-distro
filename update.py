import os
import colorama

print(colorama.Fore.LIGHTGREEN_EX + """
       .ed'''' '''$$$$be.
     -'           ^''**$$$e.
   .'                   '$$$c
  /                      '4$$b
 d  3                      $$$$
 $  *                   .$$$$$$
.$  ^c           $$$$$e$$$$$$$$.
d$L  4.         4$$$$$$$$$$$$$$b
$$$$b ^ceeeee.  4$$ECL.F*$$$$$$$
$$$$P d$$$$F $ $$$$$$$$$- $$$$$$
3$$$F '$$$$b   $'$$$$$$$  $$$$*'
 $$P'  '$$b   .$ $$$$$...e$$
  *c    ..    $$ 3$$$$$$$$$$eF
    %ce''    $$$  $$$$$$$$$$*
     *$e.    *** d$$$$$'L$$
      $$$      4J$$$$$% $$$
     $''$=e....$*$$**$cz$$'
     $  *=%4.$ L L$ P3$$$F
     $   '%*ebJLzb$e$$$$$b
      %..      4$$$$$$$$$$
       $$$e   z$$$$$$$$$$
        '*$c  '$$$$$$$P'
          '''*$$$$$$$'

     #    # #####  #####    ##   ##### ###### 
     #    # #    # #    #  #  #    #   #      
     #    # #    # #    # #    #   #   #####  
     #    # #####  #    # ######   #   #      
     #    # #      #    # #    #   #   #      
      ####  #      #####  #    #   #   ######          ===>    @Martorini \n """)


      
print ("\n") 

def main(): 
	
	print("""
	1 => Ubuntu
	2 => Fedora
	3 => ArchLinux
	99 => Exit""")

	print ("\n") 
	
	choose = int(input("Please Choose The Distribution : ")) 

	if choose == 1: 
		Debian() 
		exit(0)  
	
	elif choose == 2: 
		Fedora() 
		exit(0)  

	elif choose == 3: 
		Arch() 
		exit(0) 
	
	elif choose == 99: 
		print("\n WTF!!! \n GET OUT OF HERE")
		print('''
                      :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~
		''')
		os.system('sleep 5') 
		os.system('clear') 
		exit(0)  

	
	else:
		print("The Value Not Found " + str(choose)) 
		os.system('sleep 5') 
		os.system('clear') 
		exit(0)  
	
def Debian():
	print(colorama.Fore.MAGENTA + "\nSTART UPDATE\n")
	os.system('sudo apt update -y')
	print(colorama.Fore.CYAN + "\nEND UPDATE - 100%\n")
	print(colorama.Fore.MAGENTA + "\nSTART UPGRADE\n")
	os.system('sudo apt upgrade -y')
	print(colorama.Fore.CYAN + "\nEND UPGRADE - 100%\n")
	print(colorama.Fore.MAGENTA + "\nSTART DIST-UPGRADE\n")
	os.system('sudo apt dist-upgrade -y')
	print(colorama.Fore.CYAN + "\nEND DIST-UPGRADE - 100%\n")
	print(colorama.Fore.MAGENTA + "\nSTART AUTOREMOVE\n")
	os.system('sudo apt autoremove -y')
	print(colorama.Fore.CYAN + "\nEND AUTOREMOVE - 100%\n")
	print(colorama.Fore.MAGENTA + "\nALL UPDATE COMPLETED\n")
	print (colorama.Fore.GREEN + "Code By:" + colorama.Fore.WHITE + " Martorini")
	os.system('sleep 7')
	os.system('clear')

def Fedora(): 
	os.system('sudo yum -y update') 
	print("All update completed\n") 
	print (colorama.Fore.RED + "Code By:" + colorama.Fore.WHITE + " Martorini") 
	os.system('sleep 7') 
	os.system('clear') 

	check = input('Do Want Check On Kernels (Y/n) : ') 
	if check ==  'y' or check == 'Y': 
		os.system('yum list installed kernel') 
	elif check == 'n' or check == 'N': 
		exit(0) 

	kernelRemove = input('Do You Want Remove old kernels (Y/n) : ') 
	if kernelRemove == 'y' or kernelRemove == 'Y': 
		kernel = input('Enter Versoin Kernel : ') 
		os.system('yum list installed kernel*' + str(kernel)) 
		os.system('sudo yum -y remove kernel*' +  str(kernel)) 
	elif kernelRemove == 'n' or kernelRemove == 'N': 
		exit(0)

def Arch(): 
	os.system("sudo pacman -Syu") 
	os.system("sudo pacman -Syy") 
	print('All update completed\n') 
	print(colorama.Fore.BLUE + "Code By: " + colorama.Fore.WHITE + " Martorini") 
	os.system("sleep 7") 
	os.system("clear") 

if __name__ == '__main__': 
	main() 

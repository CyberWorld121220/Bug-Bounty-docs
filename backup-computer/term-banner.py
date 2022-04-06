import requests
import re
from prettytable import PrettyTable
import pyfiglet
import argparse
#colors
class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR
    B = "\033[0;34;40m" # Blue
    orange='\033[43m' 
    purple='\033[45m'
    cyan='\033[46m'
    lightgrey='\033[47m'
    lightgrey='\033[37m'
    darkgrey='\033[90m'
    lightred='\033[91m'
    pink='\033[95m'
anonymous = """
                                                     ...',;:cllooodddxdxxxxxxxxxxxxxxxdddollc:;,'...                                                  
                                            .',:codxO0KXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNXK0Oxol:,..                                         
                                     ..;ldk0XNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWX0koc,.                                    
                                  'cx0NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNKx:.                                 
                               'oONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXd,                               
                             'xNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNx'                             
                           .cXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK:                            
                          .dNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXc                           
                         .dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK;                          
                         oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMO.                         
                        ;XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWl                         
                       .xMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMk.                        
                       :XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMX;                        
                      .dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNNNNWWMMMMMMMMMMMMMMMMWl                        
                      '0MMMMMMMMMMMMMMWNXKK000KKXWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNKkdlc:,'''''',:cokXWMMMMMMMMMMMx.                       
                      :NMMMMMMMMMWXOoc;'.........';:lok0NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXOo:'.                 .:kNMMMMMMMMM0'                       
                      oMMMMMMMMNOc'.,coddddlc;..       .';oOXWMMMMMMMMMMMMMMMMMMMMMMMMXx:.       .,:odkO00OOkdo:,..,kWMMMMMMMX;                       
                     .kMMMMMMW0:.,dKWMMMMWXXNNX0ko:'.       .cONMMMMMMMMMMMMMMMMMMMMKo.       .:x0KOdocc::oKMMMMWKkol0WMMMMMMWc                       
                     ,KMMMMMWx;cONMMMMMMMNkl;,,:lxOK0x:.       ;OWMMMMMMMMMMMMMMMMWx.      .;xXXkc'...,:ld0WMMMMMMMMWWMMMMMMMMo                       
                     cNMMMMMNOKWMMMMMMMMMMMWKxc,. ..:xKKx,      .xWMMMMMMMMMMMMMMWx.     .cONXd,.'cx0XWMMMMMMMMMMMMMMMMMMMMMMMx.                      
                     dMMMMMMMMMMMMMMMMMMMMMMMMMW0x:.  .:x0x,     ,KMMMMMMMMMMMMMMWc    .lKN0l'.:kNMMMMMMMMMMMMMMMMMMMMMMMMMMMMO.                      
                    .OMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXkc.  'lkx:.  ,KMMMMMMMMMMMMMMMk,':dXNk:.'oKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK,                      
                    ,KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXx,  .:k0kd0WMMMMMMMMMMMMMMMWNNWNx,.'dXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN:                      
                    :NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNx'   ;OWMMMMMMMMMMMMMMMMMMMNx,.,xNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWc                      
                    oWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXl.  .lXMMMMMMMMMMMMMMMMMK:.,xNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMo                      
                   .xMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNd.   :KMMMMMMMMMMMMMMM0,'xNMMMMMMMMMMMWX0OkkkkO0KNWMMMMMMMMMMMMMMMMx.                     
                   .kMMMMMMMMMMMMMMWKOdlc::;:::cldk0NWMMMMMMWd.   :XMMMMMMMMMMMMMM0o0MMMMMMMMWKxl:,..      ..';cd0WMMMMMMMMMMMMk.                     
                   .OMMMMMMMMMMMNOl,.              ..:o0NMMMMX:   .xMMMMMMMMMMMMMMMMMMMMMMNOl,.                  .;xNMMMMMMMMMMO.                     
                   .OMMMMMMMMMNx,                      .,dXMMMx.   cNMMMMMMMMMMMMMMMMMMMNx,                         ,xNMMMMMMMMO'                     
                   '0MMMMMWKko'                           ,0MM0'   ,KMMMMMMMMMMMMMMMMMMX:                             'lkXWMMMM0'                     
                   '0MMMMWO,                             .;0MMK;   '0MMMMMMMMMMMMMMMMMMNOo:'....    .......'',;:cclodddxkKWMMMM0'                     
                   '0MMMMMWo       .....''',,,;;:::cclodkKWMMMX;   .OMMMMMMMMMMMMMMMMMMMMMMWXK0000O000KKKXXNWWMMMMMMMMMMMMMMMMM0'                     
                   .kMMMMM0:';codk0KKXXNNWWWWWMMMMMMMMMMMMMMMMX;   .OMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMO.                     
                    dMMMMMXKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0'   .OMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMk.                     
                    cWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMk.   .kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMx.                     
                    '0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd    .kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWo                      
                     oWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN:    .kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMX;                      
                     .OMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMO.    .kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMx.                      
                      ;XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWl     .OMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK;                       
                       :KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMk.     '0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMX:                        
                      ..;0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0,      ,KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0;                         
                     ,Ok,.oXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNx'       ;XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNk,                          
                     .kMXc..lkNMMMMMMMMMMMMMMMMMMMMMMMNkl'         cWMMMMMMMMMMMMMMMNkdONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKdoOo.                         
                      :XMNl   .:oxOKXXXXXXXKK0OOkOXMNx'     .      dMMMMMMMMMMMMMMMMWKkxdOWMMMMMMMWNWWWWMMMMMMWWWNK0xl;.;0Mk.                         
                       dWMNl  .c.  .,oxkkOOOOOO00KNMk.    :O0l.   'OMMMMMMMMMMMMMMMMMMMMXx0MMMMMMWKdlc::::::;;,,'.''   ;KMMd                          
                       .kMMNc ,K0;  '0MMMMMMMMMMMMMMk.   :NMM0'   :NMMMMMMMMMMMMMMMMMMMMMNNMMMMMMMMWXK0OOOkx:    ,Ok. ;KMMK,                          
                        ,KMMX:.xMK;  :KMMMMMMMMMMMMMNl  .kMMMx.  .xMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK;  .lXMk.,KMMWo                           
                         :XMMX::KMK;  ,kWMMMMMMMMMMMMNk:oXMMN:   ,KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0;  .dNMNc,0MMWk.                           
                          lNMMXllXM0,  .:ONMMMMMMMMMMMMWWMMMXc   lWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNd.  .kWMWd:OMMM0,                            
                          .dWMMNdlKM0,    ,dKWMMMMMMMMMMMMMMMXk, oMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNx,   ,0WMNd;OMMMK;                             
                           .xWMMNxc0MK:     .:d0NMMMMMMMMMMMMMWd .xXWMMMMMMMMWXxclkNMMMMMMMMMMMMMMMWXx,    cXMMXl,kWMMXc                              
                            .kWMMWx;xNNd.      .,cdOKNWMMMMMWXd.   .:oxO0K00kl.    ;OWMMMMMMMMMMNKxc.    .xNMWO,'kWMMNc                               
                             .kWMMWk,:0WKl.         .',:ccc:;.        .;c,.         .cOXNNNKOxo:'.     .:0WWKl..kWMMNl                                
                              .OMMMWO'.lXWKd;.                      .l0NWO,.           .''..          ;OWMXd. .kWMMXc                                 
                               'OMMMM0, .dXMWKxc,.                 ,0WMMMMX0o.                     'cONMXx'  'OWMMX:                                  
                                'OMMMMK;  'dXMMMWKxl:'.          .oXMMMMMMMMWO,               .,cdONMMMWKd'.:KMMMK;                                   
                                 'OMMMMK;   .l0WMMMMWNKOxoc:;;;cdKWWXXXXKKKKKKk;      ..';coxOXWMMMMMMMMNl.oNMMM0,                                    
                                  'OMMMMX:    .:ONMMMMMMMMMMMMMMMMMNK0OkxdddddddodxkO0KXWMMMMMMMMMMMMMMXc'xWMMWk.                                     
                                   'OWMMMXl      ,xXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK:;0WMMNd.                                      
                                    .kWMMMNo.     .cdOXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWO;cXMMMXl.                                       
                                     .dNMMMWx.    dNK0KNNNNNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWk:dNMMMK;                                         
                                      .oNMMMWx.   dMMMMMWNXXKK0kdllllllllcccclkXMMMMMMMMMMMMMMMMMMNxcOWMMWO'                                          
                                        lNMMMWx.  oWMMMMMMMMMMWN0d,           .oNMMMMMMMMMMMMMMMMNxdKMMMNd.                                           
                                         lNMMMWx. cWMMMMMMMMMMMMMMNc         .dNMMMMMMMMMMMMMMMMXkkNMMMXl.                                            
                                          lNMMMWk.:NMMMMMMMMMMMMMMMk.       .xWMMMMMMMMMMMMMMMMWKXWMMMK;                                              
                                           :KMMMWOdXMMMMMMMMMMMMMMMk.       .OMMMMMMMMMMMMMMMMMWWMMMWO'                                               
                                            ,OWMMMWWMMMMMMMMMMMMMMNc         lNMMMMMMMMMMMMMMMMMMMMNd.                                                
                                             .dNMMMMMMMMMMMMMMMMMXc          .xWMMMMMMMMMMMMMMMMMMK:                                                  
                                               :0MMMMMMMMMMMMMMMNl            ,KMMMMMMMMMMMMMMMMWk'                                                   
                                                .xNMMMMMMMMMMMMM0'            .OMMMMMMMMMMMMMMMXl.                                                    
                                                  :KMMMMMMMMMMMMO'            '0MMMMMMMMMMMMMNk'                                                      
                                                   .dNMMMMMMMMMMK,            cNMMMMMMMMMMMW0:                                                        
                                                     ;OWMMMMMMMMWl           '0MMMMMMMMMMMXo.                                                         
                                                      .:0WMMMMMMM0'         .dWMMMMMMMMMNd'                                                           
                                                        .c0WMMMMMWl         ;XMMMMMMMMXd'                                                             
                                                          .cONMMMMO.       .dMMMMMMNkc.                                                               
                                                             ,oOXWK,      .,kMWNKkl'                                                                  
                                                                .,,.       .,c;'.                                                                     

"""
anonymous_small="""
████▓▓▓▓▓▓▓█████╬╬╬╬╬╬████╬╬╬╬╬╬╬╬╬╬╬╬██
███▓▓▓▓▓▓▓▓▓▓▓██╬╬╬╬╬╬██╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
████▓▓▓▓▓▓▓▓▓▓▓██╬╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
███▓▓▓███████▓▓▓███╬╬╬╬╬╬█████████╬╬╬╬██
███▓▓██████████▓▓██╬╬╬╬╬████████╬╬╬╬╬╬██
███▓▓▓▓▓▓▓▓▓▓▓▓▓▓██╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
████▓▓▓▓▓▓▓▓▓▓▓▓▓██╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
█████▓▓▓▓▓▓▓▓▓▓▓▓██╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
█████▓▓▓▓▓▓▓▓█▓▓▓██╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
█████▓▓▓▓▓▓▓██▓▓▓██╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
█████▓▓▓▓▓████▓▓▓██╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
████▓▓▓▓▓▓██▓▓▓▓███╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
████▓▓█▓▓▓▓▓▓▓▓▓███╬╬╬╬╬╬╬╬╬╬╬╬██╬╬╬╬███
█████▓██▓▓▓▓▓▓▓▓▓██████╬╬╬╬╬╬╬██╬╬╬╬╬███
█████▓▓█████▓▓▓████╬████╬╬╬████╬╬╬╬╬╬███
██████▓▓▓▓████████╬╬╬████████╬╬╬╬╬╬╬████
███████▓▓▓▓▓▓▓▓▓█████████╬╬╬╬╬╬╬╬╬╬╬████
███████▓▓▓▓▓▓▓▓███╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬█████
████████▓▓▓▓▓▓▓▓████╬╬╬╬╬╬╬╬╬╬╬╬╬╬██████
█████████▓▓▓▓▓▓▓▓▓███╬╬╬╬╬╬╬╬╬╬╬╬███████
██████████▓▓▓▓▓▓▓▓▓██╬╬╬╬╬╬╬╬╬╬╬████████
███████████▓▓▓▓▓▓▓███╬╬╬╬╬╬╬╬╬╬█████████
"""
anonymous3="""
░░      ░░      ░░          ██░░░░░░                ░░░░░░██              ░░      ░░  ░░
                      ░░  ██░░                            ░░██    ░░                    
                        ██░░                                ░░██                        
                        ██    ██████                ██████    ██                        
                        ██  ░░░░░░░░████        ████░░░░░░░░  ██                        
                        ██          ░░████    ████░░          ██                        
                        ██            ░░░░    ░░░░            ██                        
                        ██░░  ░░██████░░░░    ░░░░██████░░  ░░██                        
                        ██░░░░██████████░░    ░░██████████░░░░██                        
                        ██░░  ░░░░░░░░  ░░    ░░  ░░░░░░░░  ░░██                        
                        ██              ░░    ░░              ██                        
                        ██  ░░░░░░      ░░    ░░      ░░░░░░  ██                        
                        ██  ░░░░░░    ░░        ░░    ░░░░░░  ██                        
                        ██░░          ░░        ░░          ░░██                        
                        ██░░░░██        ██░░░░██        ██░░░░██                        
                        ██░░  ██████░░████████████░░██████  ░░██                        
                        ██  ░░  ██████████    ██████████  ░░  ██                        
                          ██  ░░░░    ░░░░░░░░░░░░    ░░░░  ██                          
                          ██      ░░                ░░      ██                          
                            ██  ░░  ░░░░░░████░░░░░░  ░░  ██                            
                            ██░░  ░░      ████      ░░  ░░██                            
                              ██░░      ░░████░░      ░░██                              
                                ██░░    ░░████░░    ░░██                                
                                  ██░░░░  ████  ░░░░██                                  
                                    ████░░████░░████                                    
                                        ████████                                        
░░░░░░░░░░░░░░  ░░░░░░░░░░░░░░░░░░░░░░  ░░▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ░░░░░░
"""
anonymous4="""
⠄⠄⠄⠄⠄⠄⣀⣀⣤⣤⣴⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣦⣤⣤⣄⣀⡀⠄⠄⠄⠄⠄
⠄⠄⠄⠄⣴⣿⣿⡿⣿⢿⣟⣿⣻⣟⡿⣟⣿⣟⡿⣟⣿⣻⣟⣿⣻⢿⣻⡿⣿⢿⣷⣆⠄⠄⠄
⠄⠄⠄⢘⣿⢯⣷⡿⡿⡿⢿⢿⣷⣯⡿⣽⣞⣷⣻⢯⣷⣻⣾⡿⡿⢿⢿⢿⢯⣟⣞⡮⡀⠄⠄
⠄⠄⠄⢸⢞⠟⠃⣉⢉⠉⠉⠓⠫⢿⣿⣷⢷⣻⣞⣿⣾⡟⠽⠚⠊⠉⠉⠉⠙⠻⣞⢵⠂⠄⠄
⠄⠄⠄⢜⢯⣺⢿⣻⣿⣿⣷⣔⡄⠄⠈⠛⣿⣿⡾⠋⠁⠄⠄⣄⣶⣾⣿⡿⣿⡳⡌⡗⡅⠄⠄
⠄⠄⠄⢽⢱⢳⢹⡪⡞⠮⠯⢯⡻⡬⡐⢨⢿⣿⣿⢀⠐⡥⣻⡻⠯⡳⢳⢹⢜⢜⢜⢎⠆⠄⠄
⠄⠄⠠⣻⢌⠘⠌⡂⠈⠁⠉⠁⠘⠑⢧⣕⣿⣿⣿⢤⡪⠚⠂⠈⠁⠁⠁⠂⡑⠡⡈⢮⠅⠄⠄
⠄⠄⠠⣳⣿⣿⣽⣭⣶⣶⣶⣶⣶⣺⣟⣾⣻⣿⣯⢯⢿⣳⣶⣶⣶⣖⣶⣮⣭⣷⣽⣗⠍⠄⠄
⠄⠄⢀⢻⡿⡿⣟⣿⣻⣽⣟⣿⢯⣟⣞⡷⣿⣿⣯⢿⢽⢯⣿⣻⣟⣿⣻⣟⣿⣻⢿⣿⢀⠄⠄
⠄⠄⠄⡑⡏⠯⡯⡳⡯⣗⢯⢟⡽⣗⣯⣟⣿⣿⣾⣫⢿⣽⠾⡽⣺⢳⡫⡞⡗⡝⢕⠕⠄⠄⠄
⠄⠄⠄⢂⡎⠅⡃⢇⠇⠇⣃⣧⡺⡻⡳⡫⣿⡿⣟⠞⠽⠯⢧⣅⣃⠣⠱⡑⡑⠨⢐⢌⠂⠄⠄
⠄⠄⠄⠐⠼⣦⢀⠄⣶⣿⢿⣿⣧⣄⡌⠂⠢⠩⠂⠑⣁⣅⣾⢿⣟⣷⠦⠄⠄⡤⡇⡪⠄⠄⠄
⠄⠄⠄⠄⠨⢻⣧⡅⡈⠛⠿⠿⠿⠛⠁⠄⢀⡀⠄⠄⠘⠻⠿⠿⠯⠓⠁⢠⣱⡿⢑⠄⠄⠄⠄
⠄⠄⠄⠄⠈⢌⢿⣷⡐⠤⣀⣀⣂⣀⢀⢀⡓⠝⡂⡀⢀⢀⢀⣀⣀⠤⢊⣼⡟⡡⡁⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠈⢢⠚⣿⣄⠈⠉⠛⠛⠟⠿⠿⠟⠿⠻⠻⠛⠛⠉⠄⣠⠾⢑⠰⠈⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠑⢌⠿⣦⡡⣱⣸⣸⣆⠄⠄⠄⣰⣕⢔⢔⠡⣼⠞⡡⠁⠁⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠑⢝⢷⣕⡷⣿⡿⠄⠄⠠⣿⣯⣯⡳⡽⡋⠌⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⢮⣿⣽⣯⠄⠄⢨⣿⣿⡷⡫⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
"""
ascii_banner_anonymous = pyfiglet.figlet_format(anonymous_small)
print(anonymous4)
ascii_banner = pyfiglet.figlet_format("You are compromised now")
#print(ascii_banner)
print(f"{bcolors.pink}Whoami : Viraj Vaishnav{bcolors.RESET}")
print(f"{bcolors.pink}Head of Network and Security and Department{bcolors.RESET}")
#print(f"{bcolors.pink}Bug-Bounty Hunter{bcolors.RESET}")
#print(f"{bcolors.pink}CTF Player on HTB,tryhafckme,picoctf etc{bcolors.RESET}")
#print(f"{bcolors.pink}Follow on: https://twitter.com/VirajVaishnav16{bcolors.RESET}")

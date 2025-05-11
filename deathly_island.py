game = input("Click 'ON'\n").upper()
if  game == "ON":
    print(r'''
 b                            ,,,,                    ,d
 8b,                       ,(()(()),               ,ad8P
d888b,_                   ,(((""""))),           ,d8888b,
88   `"Ya,_              ,(()<@  @>(()        _a8P"  `888b
Y8ba,a   `"Ya,_          (()(  ..  ))(      _aP"   ad88888b
`8888P       `"Ya,_      ())(\ -- /(()    ,aP'       `Y8888
 Y88P'           `""Ya,_ )(())`--'())  ,adP'   ,@,     Y88P
 `Y8'       ,@,       ""Y((()'|  |`()aP"'      @@@     ,8P'
  `Ybaad    @@@        /'            `\        `@'   ad8'
    8P"     `@'       /    /        \  \              Y8,
   dP'               /    /(  o |    o  \     b,    b  `8
  d'  d     ,P      /   /|  `--' `--/'\  \    `8,  YP  dP
  8,  YP  ,d"      |  /' |         /   | |     `Ya,__,dP'
  `Yb,__,a8P       | |   |       ,'    | |      `88888P'
    "Y88888ba      | |   )     . (     | |      d888P"
      `"Y888'      | |  /         \    | |      `8P"
         `"Yb,     | | (           `.  / \      ,8'
            `Ya    / \ (      `Y'    \|/\ \    b8'
              `b  / /\|`.       `\    \  ||    `8,
               8  ||    8\        `\   \        8b,
               8        8 `\        \   \       888,
              dP        8   `\       \   ),    dP'`8b,
            ,d88       ,P     `\      \  )Y, ,d"   888,
          ,d8' 8,     ,P'       `\     )/ `Yd"     8'`b,
        ,dP'8  `Y,,,aP"          ,)    )   `Y,    8'  `b
       d"   "    `8'            //    /     `Y,        8,
      d'  ,@,     8           /'/    /       `b   ,@,  `b
     d'   @@@    ,P        _,' (    /         8   @@@   8,
     8, a `@'   ,P'       |   (    /          8   `@'   `b
     `b 8      aP'        |  /|   /           Y,         8
      8 `b   ,d"          | / )  /            `Ya,  a,   8
      8 ,8a,aP'           \/ ,' (               "Ya,`P  ,8
      8a888P'                (   \                "Y8b,,d8
      888P'                   `\  \                 "Y888P
      8P'                       `\ |                  Y8P'
      P                           `'                   P'
        ''')
    print("DEATHLY ISLAND is a world where only the strongest and the smartest warriors survive.")
    warrior = input("My name is Lilith Nightshade — your charming guide in this magnificent world. What is your name, warrior? ")
    print(f"Welcome, {warrior}. Your mission is to stay alive until sunrise — it’s your only way back home.")
    direction = input("You stand before two doors: one to your right, one to your left.\n"
                      r'''
   ________.-.                .-.________
  (_______( / \----      ----/ \ )_______)
     (___()\)  )            (  (/()___)
      (__()                      ()__)
       (_()___/----      ----\___()_)
       
       '''
                      "    Type 'LEFT' or 'RIGHT'.\n").upper()
    if direction == "RIGHT":
        first_challenge = input(f"This is your first challenge, {warrior}.\n"
        "Two dark holes lie before you, just large enough to fit a human head.\n"
        "You have to choose one to put your head in, \n"
        "-Hole 'A' looks clean.\n"
        "-Hole 'B' has red stains around the edges — like something splashed out.\n"
        f"Which hole do you choose, {warrior}?\n"
        "           Type 'A' or 'B'.\n").upper()
        if first_challenge == "B":
            print("You put your head in hole B, It's just red paint. No damage taken.")
            second_challenge = input(f"Nice choice, {warrior}. You’ve survived this time.\n"
            "Now, you face another choice:\n"
            "-Option 1: A grand hall filled with beautiful women dancing and singing, beckoning you to join.\n"
            "-Option 2: A filthy hallway filled with high-pitched screams echoing from within.\n"
            "           Type '1' or '2'.\n").upper()
            if second_challenge == "2":
                print(r'''
88888888888888888888888888888888888888888888888888888888888888888888888
88.._|      | `-.  | `.  -_-_ _-_  _-  _- -_ -  .'|   |.'|     |  _..88
88   `-.._  |    |`!  |`.  -_ -__ -_ _- _-_-  .'  |.;'   |   _.!-'|  88
88      | `-!._  |  `;!  ;. _______________ ,'| .-' |   _!.i'     |  88
88..__  |     |`-!._ | `.| |_______________||."'|  _!.;'   |     _|..88
88   |``"..__ |    |`";.| i|_|MMMMMMMMMMM|_|'| _!-|   |   _|..-|'    88
88   |      |``--..|_ | `;!|l|MMoMMMMoMMM|1|.'j   |_..!-'|     |     88
88   |      |    |   |`-,!_|_|MMMMP'YMMMM|_||.!-;'  |    |     |     88
88___|______|____!.,.!,.!,!|d|MMMo * loMM|p|,!,.!.,.!..__|_____|_____88
88      |     |    |  |  | |_|MMMMb,dMMMM|_|| |   |   |    |      |  88
88      |     |    |..!-;'i|r|MPYMoMMMMoM|r| |`-..|   |    |      |  88
88      |    _!.-j'  | _!,"|_|M)(MMMMoMMM|_||!._|  `i-!.._ |      |  88
88     _!.-'|    | _."|  !;|1|MbdMMoMMMMM|l|`.| `-._|    |``-.._  |  88
88..-i'     |  _.''|  !-| !|_|MMMoMMMMoMM|_|.|`-. | ``._ |     |``"..88
88   |      |.|    |.|  !| |u|MoMMMMoMMMM|n||`. |`!   | `".    |     88
88   |  _.-'  |  .'  |.' |/|_|MMMMoMMMMoM|_|! |`!  `,.|    |-._|     88
88  _!"'|     !.'|  .'| .'|[@]MMMMMMMMMMM[@] \|  `. | `._  |   `-._  88
88-'    |   .'   |.|  |/| /                 \|`.  |`!    |.|      |`-88
88      |_.'|   .' | .' |/                   \  \ |  `.  | `._    |  88
88     .'   | .'   |/|  /                     \ |`!   |`.|    `.  |  88
88  _.'     !'|   .' | /                       \|  `  |  `.    |`.|  88
88 vanishing point 888888888888888888888888888888888888888888888 fL 888
                
You bravely entered the terrifying hall —
But it was only an illusion to scare the wicked. 
An old lady offers you shelter and gently wipes the paint from your face.
''')
                third_and_last_challenge = input(f"FINAL CHALLENGE. Choose wisely, {warrior}.\n"
                "Three doors stand before you:\n"
                "1) Red – forged from ancient wood\n"
                "2) Yellow – inlaid with precious metals\n"
                "3) Blue – bound in supple animal hide\n\n"
                "           Type R, Y, or B to choose: ").upper()
                if third_and_last_challenge == "R":
                    print(r'''
     ______
  ,-' ;  ! `-.
 / :  !  :  . \
|_ ;   __:  ;  |
)| .  :)(.  !  |
|"    (##)  _  |
|  :  ;`'  (_) (
|  :  :  .     |
)_ !  ,  ;  ;  |
|| .  .  :  :  |
|" .  |  :  .  |
|mt-2_;----.___|
                     
The door glows and pulls you into a portal — you’re home, safe and sane!
                    
                                              888            
                                              888            
                                              888            
.d8888b .d88b. 88888b.  .d88b. 888d888 8888b. 888888.d8888b  
d88P"   d88""88b888 "88bd88P"88b888P"      "88b888   88K      
888     888  888888  888888  888888    .d888888888   "Y8888b. 
Y88b.   Y88..88P888  888Y88b 888888    888  888Y88b.      X88 
"Y8888P "Y88P" 888  888 "Y88888888    "Y888888 "Y888 88888P' 
                           888                              
                       Y8b d88P                              
                        "Y88P"
                     
✨YOU FINISHED THE GAME ALIVE✨
You survived the myth. You earned your way home.''')
                elif third_and_last_challenge == "Y":
                    print("The moment you step through the door, a ton of gold crashes down and crushes you.\n"
                    "GAME OVER!")
                else:
                    print("Mythical, double-headed wolves devour you as soon as you enter. Brutal.\n"
                    "GAME OVER!")
            elif second_challenge == "1":
                print(r'''The women devour you alive — they were Sirens, terrifying mythical predators luring prey with beauty.
                  ____
                                                 /--. \
                                                 a a!  )
                                                /\-_/  (
                                               (,-! '-. )
                                               /  - -  \(
                                              /,(_ (_ )\\
                                             //__)   / (\\
                                      __..--``   \,_/  ) \\
                                _,--``             /  (_, \\__
                          gnv ,'  _______________,'\___,   \-\\
                             /  ,'   ___
                             | (___,' ,-\
                             \       / 
                              \  `--<___,
                               `._____.'           
GAME OVER!''')
        elif first_challenge == "A":
            print(r'''
               .-"      "-.
              /            \
             |              |
             |,  .-.  .-.  ,|      You gently place your head in the clean hole...
             | )(_o/  \o_)( |
             |/     /\     \|      *CLICK*
             (_     ^^     _)
              \__|IIIIII|__/       GRRRRRRRINNNNNDDDD
               | \IIIIII/ |
               \          /
                `--------`
You’re sucked into the clean hole like a pressed vegetable. Not even a drop of blood remains.
GAME OVER!''')
    else:
        print(fr'''A raging Minotaur was waiting behind the door. You didn’t stand a chance, {warrior}.
                                                                       
                                                                      _( (~\
               _ _                        /                          ( \> > \
           -/~/ / ~\                     :;                \       _  > /(~\/
          || | | /\ ;\                   |l      _____     |;     ( \/ /   /
          _\\)\)\)/ ;;;                  `8o __-~     ~\   d|      \   \  //
         ///(())(__/~;;\                  "88p;.  -. _\_;.oP        (_._/ /
        (((__   __ \\   \                  `>,% (\  (\./)8"         ;:'  i
        )))--`.'-- (( ;,8 \               ,;%%%:  ./V^^^V'          ;.   ;.
        ((\   |   /)) .,88  `: ..,,;;;;,-::::::'_::\   ||\         ;[8:   ;
         )|  ~-~  |(|(888; ..``'::::8888oooooo.  :\`^^^/,,~--._    |88::| |
          \ -===- /|  \8;; ``:.      oo.8888888888:`((( o.ooo8888Oo;:;:'  |
         |_~-___-~_|   `-\.   `        `o`88888888b` )) 888b88888P""'     ;
          ;~~~~;~~         "`--_`.       b`888888888;(.,"888b888"  ..::;-'
           ;      ;              ~"-....  b`8888888:::::.`8888. .:;;;''
         ;    ;    ;                 `:::. `:::OOO:::::::.`OO' ;;;''
           :     ;                     `.      "``::::::''    .'
         ;    ;                         `.   \_              /
            ;    ;                        +:   ~~--  `:'  -';
                                           `:         : .::/
              ;                            ;;+_  :::. :..;;;

GAME OVER!''')

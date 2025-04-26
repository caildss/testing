# WELCOME to childe quizzz

def run_quiz():
    print(""" 

        ,----,                                                                                                
      ,/   .`|       ,--,                                                                 ,----,       ,----, 
    ,`   .'  :     ,--.'|    ,---,.            ,----..                      ,---,       .'   .`|     .'   .`| 
  ;    ;     /  ,--,  | :  ,'  .' |           /   /   \             ,--, ,`--.' |    .'   .'   ;  .'   .'   ; 
.'___,/    ,',---.'|  : ',---.'   |          /   .     :          ,'_ /| |   :  :  ,---, '    .',---, '    .' 
|    :     | |   | : _' ||   |   .'         .   /   ;.  \    .--. |  | : :   |  '  |   :     ./ |   :     ./  
;    |.';  ; :   : |.'  |:   :  |-,        .   ;   /  ` ;  ,'_ /| :  . | |   :  |  ;   | .'  /  ;   | .'  /   
`----'  |  | |   ' '  ; ::   |  ;/|        ;   |  ; \ ; |  |  ' | |  . . '   '  ;  `---' /  ;   `---' /  ;    
    '   :  ; '   |  .'. ||   :   .'        |   :  | ; | '  |  | ' |  | | |   |  |    /  ;  /      /  ;  /     
    |   |  ' |   | :  | '|   |  |-,        .   |  ' ' ' :  :  | | :  ' ; '   :  ;   ;  /  /--,   ;  /  /--,   
    '   :  | '   : |  : ;'   :  ;/|        '   ;  \; /  |  |  ; ' |  | ' |   |  '  /  /  / .`|  /  /  / .`|   
    ;   |.'  |   | '  ,/ |   |    \         \   \  ',  . \ :  | : ;  ; | '   :  |./__;       :./__;       :   
    '---'    ;   : ;--'  |   :   .'          ;   :      ; |'  :  `--'   \;   |.' |   :     .' |   :     .'    
             |   ,/      |   | ,'             \   \ .'`--" :  ,      .-./'---'   ;   |  .'    ;   |  .'       
             '---'       `----'                `---`        `--`----'            `---'        `---'           
                                                                                                              

   Do you know Childe? """)
    score = 0

    questions = [
        {
            "question": "Number what of the fatui harbingers is Childe??",
            "options": ["1. Eleventh", "2. First", "3. Eight", "4. Tenth"],
            "answer": 1
        },
        {
            "question": "Where is Childe's hometown?",
            "options": ["1. Liyue", "2. Snezhnaya", "3. Fontaine", "4. Mondstatd"],
            "answer": 2
        },
        {
            "question": "Childe's signature bow??",
            "options": ["1. Aqua Simulcra", "2. Hunter's Path", "3. Polar Star", "4. Thundering Pulse"],
            "answer": 3
        },
        {
            "question": "what is Childe's Constellation?",
            "options":["1. Lupus Minor", "2. Vulpes Zerda", "3. Umbrabilis Orchis", "4. Monoceros Caeli"],
            "answer": 4
        },
        {
            "question": "Which historical figure that potraits his relation with skirk?",
            "options": ["1. Cú Chulainn", "2. Ajax the Great", "3. Apollo", "4. Lucifer"],
            "answer": 1
        },
        { 
            "question": "What region is childe's book for the talent ascensions from?",
            "options": ["1. Liyue", "2. Mondstadt", "3. Inazuma", "4. Snezhnaya"],
            "answer": 2
        }
    ]

    for i, q in enumerate(questions):
        print(f"\nQuestions {i + 1}: {q['question']}")
        for option in q["options"]:
            print(option)
        try:
            user_answer = int(input("Insert the number of your answ : "))
            if user_answer == q["answer"]:
                print("COREC!")
                score += 1
            else:
                print("Fake childe fan....")
        except ValueError:
            print("Typo? number only! (skip this question cus im too lazy to code the retry)")

    print(f"\nyour score is... {score}/{len(questions)}\n")
    if score == len(questions):
        print("YOU KNOW CHILDE SO WELL YALL SHOULD MARRY FRR!!")
        print("\n\n\n\n\n\n\n\n\n\n")
    elif score == 6:
        print("YOU KNOW CHILDE! but there's someone out there who deserves to marry him more than you.")
        print("\n\n\n\n\n\n\n\n\n\n")
    elif score == 5 or score == 4:
        print("You only know the basics...")
        print("\n\n\n\n\n\n\n\n\n\n")
    elif score <= 3:
        print("Do you even read his lore?")
        print("You should read his lore more often...")
        print("It's peak character, I swear.")
        print("But not that much that you can marry him tho, hehehehehe.")
        print("\n\n\n\n\n\n\n\n\n\n")
    
    

if __name__ == "__main__":
    run_quiz()
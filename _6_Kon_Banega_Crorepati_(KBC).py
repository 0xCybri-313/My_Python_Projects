# Kon Banega Crorepati
player = input("Sugat hy ap ka Kon Banega Crorepati may. Jee hamry darshagon ko apna nam bataye : ")

question = ["World Largest Country?\n", "Who is world best footballer of all time?\n", "What is OSCP?\n"]

option = ["a) Pakistan      b) India\nc) China         d) Russia", "a) Messi        b) Ronaldo  \nc) Mbappay      d) Banzema", "a) Game     b) Cert \nc) Show     d) Virus "]

correct = ["c", "a", "b"]   # Correct answer of question

no = 0

for i in question:
    print("\nTo ye raha question computer screen par:\n\nQ:", i)
    
    for j in option:
        print(f"Option\n\n{option[no]}")    # print option according to value of (no)
        answer = input()
        
        for k in correct:  
            if answer == correct[no]:
                print("\nCorrect Answer")
                
                if question.index(i) == 2: # Limit of Question
                    print(f"\n{player} Ap nay 1 Corer jeet lia hy!!!\n")
                    break
                
                print("\nNext Question")
            
            else:
                print("Wrong Answer!")
                if no == 1:
                    print(f"\n{player} Ap nay 20,50,000 Rs jeet lia hy!!!\n")
                elif no == 2:
                    print(f"\n{player} Ap nay 50,00,000 Rs jeet lia hy!!!\n")
                else:
                    print(f"\n{player} Mubarak ho ap Kon banega Cororepati say kahli hath ja rahy hy\n")
                exit()
            
            break
        
        no += 1 # No aviod the intilization of value of nested loops
        break
    
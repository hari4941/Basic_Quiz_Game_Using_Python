questions=("1. How many Bits make one Byte?",
           "2. Which electronic component was used in the first generation of computers?",
           "3. The first program that runs on a computer when the computer boots up is?",
           "4. What is the full form of VIRUS?",
           "5. The process of transferring files from the Internet to your computer is called?",
           "6. The process of transferring files from your computer to the Internet is called?",
           "7. Buying and selling products and services over the Internet is called?",
           "8. A program that translates High-Level Language to a Machine Level Language is called?",
           "9. The process to find an error in a software code is called?",
           "10. Which was the first web browser?",
           "11. What does BCD stand for?",
           "12. What does SMPS stand for?",
           "13. What does XML stand for?",
           "14. What is the meaning of OSI, in terms of computers?",
           "15.  In the context of Computer Memory, what does DMA stand for?")

options=(("A. 16 bits","B. 32 bits","C. 64 bits","D. 8 bits"),
         ("A. Vaccum tubes","B. Red tubes","C. Abacus","D. Transistors"),
         ("A. Software Program","B. Operating System","C. Utilities","D. None of the above mentioned"),
         ("A. Vital Information Rest Under System","B. Vital Information Rest Under Siege","C. Virtual Information Resources Under Siege","D. Vital Information Resources Under Siege"),
         ("A. Downloading","B. Uploading","C. Storing","D. All of the above"),
         ("A. Downloading","B. Uploading","C. Storing","D. All of the above"),
         ("A. E-Computer","B. F-Commerce","C. E-Commerce","D. None of the above"),
         ("A. Compiler","B. Interpreter","C. Assembler","D. Operating system"),
         ("A. Debugging","B. Compiling","C. Error","D. None of the above"),
         ("A. World Wide Web","B. Mosaic","C. Lynx","D. Netscape Navigator"),
         ("A. Bitwise Code Decimal","B. Binary Coded Decimal","C. Binary Code Deduction","D. Base Conversion Determinant"),
         ("A. Simple Mode Power Supply","B. Single Mode Power Source","C. Switch Mode Power Supply","D. System Mode Power Saver"),
         ("A. Extensible Markup Language","B. Extra Mobile Link","C. Extended Modulation Level","D. Extreme Media Library"),
         ("A. Open Source Interface","B. Operational System Integration","C. Optical Sensor Interface","D. Open Systems Interconnection"),
         ("A. Data Manipulation Algorithm","B. Direct Memory Access","C. Digital Media Adapter","D. Dynamic Memory Allocation"))

answers=("D","A","B","D","A","B","C","A","A","A","B","C","A","D","B")

guesses=[]

score=0
question_num=0

for i in questions:
    print("*****************************************")
    print(i)
    print()
    for j in options[question_num]:
        print(j)
    guess= input("Enter Your Answer(A/B/C/D): ").upper()
    guesses.append(guess)
    if guess==answers[question_num]:
        score+=1
        print("That's Right Answer!!!")
    else:
        print("The Answer is Incorrect!!!")
        print(f"{answers[question_num]} is the correct answer.")
    question_num+=1
print()

print("*****************************************")
print("                RESULTS                  ")
print("*****************************************")
print("Answers: ",end=" ")
for i in answers:
    print(i,end=" ")
print()
print("Guesses: ",end=" ")
for j in guesses:
    print(j,end=" ")
print()
score= int(score/len(questions)*100)
print()
print(f"Your Score is: {score}%")
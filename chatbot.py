def ask_name():
    your_name = input("Hi, what's your name? ")
    return your_name
    input("Hi" + your_name)

ask_name()

chance_of_covid = 0
symptoms = 0
has_cough = symptoms
has_cold = symptoms
has_fever = symptoms

def check_symptom(symptom):
    keep_asking = "yes"

    while keep_asking == "yes":
        answer = input("Do you have " + symptom + "? ")


        if answer == "yes":
            symptom +=1
            keep_asking = "no"
        elif answer == "no":
            keep_asking = "no"
        else:
            print("I didn't understand you, please try again!")


    return answer

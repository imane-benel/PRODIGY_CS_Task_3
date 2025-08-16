import re
def pass_check(password):
    err_upperCharacters= re.search(r"[A-Z]",password) is None
    err_lowerCharacters = re.search(r"[a-z]",password)is None
    err_length= len(password)<8
    err_number= re.search(r"\d",password) is None
    err_specialChar= re.search(r"[!@#$%^&*(),.?\":{}|<>]",password)is None

    errors=[]
    if(err_length):
       errors.append("you password should have at least 8 characters")
    elif(err_number):
        errors.append("you password should have at least 1 number")
    elif(err_upperCharacters):
        errors.append("you password should havee at least one uppercase character")
    elif(err_lowerCharacters):
        errors.append("you password should havee at least one lowercase character")
    elif(err_specialChar):
        errors.append("you password should havee at least one uppercase character")

    strength = 5 - sum([err_length ,err_number,err_upperCharacters,err_lowerCharacters,err_specialChar])
    if strength == 5 :
       efficency ="strong"
    elif 3 <= strength <5 :
       efficency ="medium"
    else :
      efficency ="weak"
    return errors,efficency




Password= input("Entrer votre mot de passe pour accéder a votre plateforme")
errors,efficency= pass_check(Password)
print(f"password strength {efficency}")
if errors:
    print("suggestions")
    for e in errors:
        print(f"-{e}")

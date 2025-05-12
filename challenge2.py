#Amina Diouf worked with Sophie
import urllib.request

url_girl = "http://002-text-files.glitch.me/girl-names.txt"
response_girl = urllib.request.urlopen(url_girl)
data_girl = response_girl.read().decode('utf-8')

url_boy = "http://002-text-files.glitch.me/boy-names.txt"
response_boy =  urllib.request.urlopen(url_boy)
data_boy = response_boy.read().decode('utf-8')
girl_names = data_girl.lower().split("\n")
boy_names = data_boy.lower().split("\n")



# Main method for program execution
def main():
    boy_name = (input("Enter a boy's name: ")).lower()
    if boy_name in boy_names:
        print(boy_name, "is one of the most popular boy's names.")
    else:
        print(boy_name, "is not one of the most popular boy's names.")
        
    girl_name = input("Enter a girl's name: ").lower()
    if girl_name in boy_names:
        print(girl_name, "is one of the most popular girl's names.")
    else:
        print(girl_name, "is not one of the most popular girl's names.")
    
    
main()

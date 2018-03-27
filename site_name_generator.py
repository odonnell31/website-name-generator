import time
import webbrowser

def siteNameGenerator(words):
    num = 0
    text_file = open("WebSiteNames.txt", "w")
    for i in words:
        for j in words:
            if i != j and num < 500:
                #print i+j+".com"
                num = num + 1
                text_file.write(i+j+".com" + '\n')
            elif num >=500:
                print "you entered too many words.."
                break
    print "Combinations made:", num
    text_file.close()
    time.sleep(1)
    webbrowser.open("WebSiteNames.txt")
    time.sleep(2)
    webbrowser.open('https://www.godaddy.com/domains/bulk-domain-search.aspx')
    
# place up to 23 words in this function
siteNameGenerator(["johnny", "jimmy", "frankie", "arty", "stanley",
                   "aloha", "jamaica", "aruba", "carribean", "cuba"])

#Auth

# If Non-Local Multiplayer is to Exist; Store Data on Cloud for True Safety
# Same USRNAME is allowed, Same UUID is Prohibited
import base64
import os
import uuid

auth_path = os.path.join (os.path.dirname(os.path.abspath(__file__)) , 'auth.dat')

def Encryptor(msg):
    return base64.b64encode(msg.encode("utf-8"))

def Decryptor(msg):
    return base64.b64decode(msg.decode("utf-8"))

def RGBToHex(rgb):
    return '#%02x%02x%02x' % rgb

#--For Debugging--
def ViewAcc():
    
    import pickle
    with open(auth_path,  'rb') as authf:        
        try:
            auths = pickle.load(authf)
        except EOFError:
            auths= {}
            
        return auths

    

#--Admin Commands
def CreateAcc():
    
    import pickle    
    auths = ViewAcc()
    
    print("Number of Accounts: ", len(auths))

    usrname = input("Enter Username: ")                                     #Duplicate Username allowed
    usrpass = Encryptor(input("Enter Temp. Pass: "))
    usrcolor = RGBToHex(eval(input("Enter Your RGB Color (3): ")))          #Do Remember the Color is a Temporary Marker

   
    auths[str(uuid.uuid4())] = {'usrname': usrname, 'usrpass': usrpass,'usrcolor': usrcolor}
    
    with open(auth_path,  'wb') as authf:     
        pickle.dump(auths, authf)


def DelAcc():
    
    import pickle
    auths = ViewAcc()
    
    ogname = input("Enter Username: ")
    for uuid in auths:
        if(auths[uuid]['usrname'] == ogname):
            del auths[uuid]
    else:
        print("Non Existing Username")
        
    with open(auth_path,  'wb') as authf:
        pickle.dump(auths, authf)
        
def ForceClear():
    ch = input("Enter 'ForcE' if you are Sure: ")
    if(ch == 'ForcE'):
        with open(auth_path,  'wb') as authf:
            pass




#--User Commands
def LogIn(usrname, usrpass):
    
    usrname = usrname
    usrpass =  Encryptor(usrpass)

    auths = ViewAcc()

    for uuid in auths:
        if(auths[uuid]['usrname']== usrname):
            if(auths[uuid]['usrpass']== usrpass):
                return uuid
    else:
        return False

##def ChangeAuth(usrname, usrpass):
##
##    if( LogIn(usrname, usrpass) ):      
##
##        import pickle
##        with open('auth.dat',  'rb+') as authf:            
##
##            ogname = Encryptor(usrname)
##
##            # SHOULD BE HANDLED VIA GUI
##            usrname = Encryptor(input("Enter New Username: "))
##            usrpass =Encryptor(input("Enter New Password: "))
##
##            del auths[ogname]
##            auths[usrname] = usrpass
##
##            pickle.dump(auths, authf)
#^^- To be Finished. Needs to be connected to GUI to be Properly Implemented and Coded

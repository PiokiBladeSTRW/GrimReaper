#Auth

import base64
import os
auth_path = os.path.join (os.path.dirname(os.path.abspath(__file__)) , 'auth.dat')

def Encryptor(msg):
    return base64.b64encode(msg.encode("utf-8"))

def Decryptor(msg):
    return base64.b64decode(msg.decode("utf-8"))

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

    usrname = Encryptor(input("Enter Username: "))
    usrpass = Encryptor(input("Enter Temp. Pass: "))

    auths[usrname] = usrpass        
    
    with open(auth_path,  'wb') as authf:     
        pickle.dump(auths, authf)
    

def DelAcc():
    
    import pickle
    auths = ViewAcc()
    
    ogname = Encryptor(input("Enter Username: "))

    try:
        del auths[ogname]
    except KeyError:
        print("Non Existing Username")
        
    with open(auth_path,  'wb') as authf:
        pickle.dump(auths, authf)


#--User Commands
def LogIn(usrname, usrpass):
    
    usrname = Encryptor(usrname)
    usrpass =  Encryptor(usrpass)

    auths = ViewAcc()

    if(usrname not in auths.keys()):
        return False
    
    if(auths[usrname] != usrpass):
        return False

    return True

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

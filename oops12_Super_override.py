class A:
    classvar1 = "I am a class varible in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance varible in class A"
        self.special = "Special"

class B(A):
    #classvar2 = "I am in class B"
    classvar1 = "I am in class B"
    def __init__(self):            # Ami iyat class A r constructor tuk override kori dilu.
        super().__init__()
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "Instance varible in class B"
        #super().__init__()
a = A()
b = B ()

print(b.classvar1)        # Python a xodai instance varibale agote sabo
# iyat b a nijor class B t sale, kunu instance variable nai. So, tar parent class A t sale, tat classvar1 namor eta instance  varibale ase, tak access koribo.
# ami jodi class B t u classvar1 namor eta varible bonau, tothapi run nhai, karon class B t instance variable nai.

# class B t eta variable ase special buli, let's try to print it :
print(b.special)    # e run hua nai, karon ami class A r constructor k ovverride kori disu. Amak jodi class A lage tente- super() ue koribo lagibo
print(b.var1)
print(b.classvar1)
import pyotp 


def sendToken(user):
    totp = pyotp.TOTP(pyotp.random_base32(), interval=120)
    
    otp = totp.now()
    
    user.otp = otp
    
    print(f"The OTP is : {otp}")

    return otp 
    
    # send a SMS to User's verified Phone number

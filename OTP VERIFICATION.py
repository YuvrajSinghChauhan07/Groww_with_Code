import pyotp

Private_key= pyotp.random_base32()

OTP = pyotp.TOTP(Private_key)
OTP_SENT= OTP.now()
print("OTP SENT:", OTP_SENT)

Req_OTP= input("Enter OTP: ")

if OTP.verify(Req_OTP):
    print("OTP is correct")
else:
    print("OTP is incorrect")

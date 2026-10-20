import base64

# فرض کن این همون یادداشت رمزنگاری شده است که توی سایت بود
encrypted_note = "VEhNe0hhY2tlZF9ieV9QeXRob259"

# حالا ما با پایتون رمزگشاییش می‌کنیم
decoded_note = base64.b64decode(encrypted_note).decode('utf-8')

print("The decrypted flag is:")
print(decoded_note)

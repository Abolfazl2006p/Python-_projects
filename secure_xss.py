import html

def render_comment(comment):
    print("\n--- Secure Website Output ---")
    
    safe_comment = html.escape(comment)
    
    html_output = f"<div class='comment'>{safe_comment}</div>"
    print(html_output)
    print("-----------------------------\n")
    
    if "<script>" in html_output.lower():
        print("[!] MALICIOUS SCRIPT DETECTED!")
    else:
        print("Comment displayed safely. XSS Neutralized.")

user_input = input("Enter your comment: ")
render_comment(user_input)
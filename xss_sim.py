def render_comment(comment):
    print("\n--- Website Output ---")
    html_output = f"<div class='comment'>{comment}</div>"
    print(html_output)
    print("-----------------------\n")

    if "<script>" in html_output.lower():
        print("[!] MALICIOUS SCRIPT DETECTED!")
        print("[!] Attacker stole the user's cookie: session_id=ABC123XYZ")
    else:
        print("Comment displayed safely.")
user_input = input("Enter your comment: ")
render_comment(user_input)
         
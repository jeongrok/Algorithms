# ecoo19r2p1
for i in range(10):
    n = int(input())
    emails = set()
    for j in range(n):
        email = input()
        at_index = email.find("@")
        plus_index = email.find("+")
        if plus_index > 0:
            email = email[:plus_index] + email[at_index:]
        at_index = email.find("@")
        dot_index = email.find(".")
        while dot_index >= 0 and dot_index < at_index:
            email = email[:dot_index] + email[dot_index + 1:]
            at_index = email.find("@")
            dot_index = email.find(".")
        # # lines 13 through 16 can be rewritten as
        # before_at = ''
        # i = 0
        # while i < at_index:
        #   if email[i] != 'i':
        #       before_at += email[i]
        #   i += 1
        # email = before_at + email[at_index:]
        email = email.lower()
        emails.add(email)
    print(len(emails))

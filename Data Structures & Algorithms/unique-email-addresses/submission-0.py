class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def process(email):
            pre, sfx = email.split('@')
            res = []
            for c in pre:
                if c == '+':
                    break
                elif c!='.':
                    res.append(c)

            return ''.join(res)+'@'+sfx

        res = set()
        for email in emails:
            res.add(process(email))
        # print(res)
        return len(res)
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def parse(s):
            local, domain = s.split("@")
            res = []
            for c in local:
                if c==".":
                    continue
                elif c=="+":
                    break
                else:
                    res.append(c)
            return "".join(res)+"@"+domain

        res = set()
        for email in emails:
            res.add(parse(email))
        print(res)
        return len(res)
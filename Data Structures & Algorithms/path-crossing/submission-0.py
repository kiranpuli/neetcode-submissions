class Solution:
    def isPathCrossing(self, path: str) -> bool:

        def move(pos, d):
            x, y = pos

            if d=='N':
                y+=1
            elif d=='S':
                y-=1
            elif d=='E':
                x+=1
            else:
                x-=1
            
            return (x, y)

        curr = (0, 0)
        vis = set()
        for d in path:
            vis.add(curr)
            curr = move(curr, d)
            if curr in vis:
                return True
        return False

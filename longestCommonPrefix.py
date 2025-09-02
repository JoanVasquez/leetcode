'''
strs = ["computer", "company", "coordination"]
prefix = computer

loop over company, coordination
while company does not starts with computer: prefix = compute
while company does not starts with compute: prefix = comput
while company does not starts with comput: prefix = compu 
while company does not starts with compu: prefix = comp 

while coordination does not starts with comp: prefix = com 
while coordination does not starts with com: prefix = co 

if not prefix return ''
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) --> str:
        if not strs:
            return ""

        prefix = strs[0]

        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                
                if not prefix:
                    return ""

        return prefix

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map1 = [0] * 128  
        map2 = [0] * 128 

        for i in range(len(s)):
            s_ch = s[i]
            t_ch = t[i]

            if map1[ord(s_ch)] == 0 and map2[ord(t_ch)] == 0:
                map1[ord(s_ch)] = ord(t_ch)
                map2[ord(t_ch)] = ord(s_ch)
            elif map1[ord(s_ch)] != ord(t_ch) or map2[ord(t_ch)] != ord(s_ch):
                return False
        return True
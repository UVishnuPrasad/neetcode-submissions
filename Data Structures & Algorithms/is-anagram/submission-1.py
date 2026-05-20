class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      if len(s)==len(t):
        hashmap_s=dict()
        hashmap_t=dict()
        for i in s:
            if i in hashmap_s.keys():
                hashmap_s[i]+=1
            else:
                hashmap_s[i]=1
        for i in t:
            if i in hashmap_t.keys():
                hashmap_t[i]+=1
            else:
                hashmap_t[i]=1
        for i in hashmap_t.keys():
            if i in hashmap_s.keys():
                if hashmap_s[i] == hashmap_t[i]:
                  pass
                else:
                  return False
            else:
                return False
      else:
        return False
      return True 

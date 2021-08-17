from collections import deque

graph = {
    "me": ["parth","naiya","vishva"],
    "parth": ["naiya","krunal", "ronak", "harsh"],
    "naiya": ["ronak","parth"],
    "vishva": ["me"],
    "ronak": ["krunal"],
    "krunal":[],
    "harsh": []
}
def search(name):
    myqueue = deque()
    myqueue += graph
    searched = []
    while myqueue:
      person = myqueue.popleft()
      if not person in searched:
          if nametofind(person):
              print(person + " is in my network")
              return True
          else:
              myqueue += graph[person]
              searched.append(person)
              print(myqueue)
              print(searched)
              print("\n")
             
    return False


def nametofind(name):
    '''Check the specific name is in my friend's list. Here I have considered the name HARSH'''
    if name[-1].lower() == "h":
        return True
    else:
        return False


#print(search(""))
print(nametofind("asr"))
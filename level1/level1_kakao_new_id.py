import re


def solution(new_id):
    answer = ''
    chrs = '[-._a-z0-9]'
    new_id = new_id.lower()
    new_id = re.findall(chrs, new_id)
    for i in range(len(new_id)):
        if i-1 > -1 and new_id[i] == '.':
            if new_id[i-1] == '.':
                new_id[i-1] = ''
    new_id = list(filter(None, new_id))
    # new_id = new_id[0]
    if new_id != [] and new_id[0] == '.':
        del new_id[0]
    if len(new_id) > 15:
        new_id = new_id[:15]
    if new_id != [] and new_id[-1] == '.':
        del new_id[-1]
    new_id = ''.join(new_id)
    if not new_id:
        new_id = 'a'
    if len(new_id) <= 2:
        for i in range(3):
            if len(new_id) < 3:
                new_id += new_id[-1]
    return new_id


def best_solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st


a = solution("...!@BaT#*..y.abcdefghijklm")
print(a)
a = solution(	"z-+.^.")
print(a)
a = solution("=.=")
print(a)
a = solution("123_.def")
print(a)
a = solution("abcdefghijklmn.p")
print(a)

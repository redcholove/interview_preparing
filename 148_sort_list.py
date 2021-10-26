if head == None:
    return None

tmp = []
cur = head

while cur:
    tmp.append(cur.val)
    cur = cur.next

tmp.sort()
cur = head

for i in range(len(tmp)):
    cur.val = tmp[i]
    cur = cur.next

return head

def read_boxes(n):
    boxes = []
    for i in range(n):
        box = input().split()
        box.pop(0)
        for i in range(len(box)):
            box[i] = int(box[i])
        boxes.append(box)
    return boxes

def box_ok(box):
    for i in range(len(box) - 1):
        if box[i] > box[i+1]:
            return False
    return True

def all_boxes_ok(boxes):
    for box in boxes:
        if not box_ok(box):
            return False
    return True

def boxes_endpoints(boxes):
    endpoints = []
    for box in boxes:
        endpoints.append([box[0], box[-1]])
    return endpoints

def all_endpoints_ok(endpoints):
    maximum = endpoints[0][1]
    for i in range(1, len(endpoints)):
        if endpoints[i][0] < maximum:
            return False
        maximum = endpoints[i][1]
    return True

#Main Program

n = int(input())
boxes = read_boxes(n)

if not all_boxes_ok(boxes):
    print("NO")
else:
    endpoints = boxes_endpoints(boxes)
    endpoints.sort()

    if all_endpoints_ok(endpoints):
        print("YES")
    else:
        print("NO")

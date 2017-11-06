from datetime import datetime

class Call(object):
    def __init__(self, unique_id, caller_name, caller_phone, reason, time):
        self.unique_id = unique_id
        self.caller_name = caller_name
        self.caller_phone = caller_phone
        self.time = time
        self.reason = reason
    def display(self):
        print self.unique_id
        print self.caller_name
        print self.caller_phone
        print self.time
        print self.reason
        return self

class Call_center(object):
    def __init__(self):
        self.calls = []
        self.queue_size = 0
    def add(self, call):
        self.calls.append(call)
        self.queue_size = self.queue_size + 1
        return self
    def remove(self, call):
        self.calls.pop(0)
        self.queue_size = self.queue_size - 1
        return self
    def info(self):
        for call in self.calls:
            print ("Name: " + call.caller_name + ", " + "Phone Number: " + call.caller_phone)
        print "Queue Size: " + str(self.queue_size)

call1 = Call("181481", "Tom", "456-458-1125", "help", datetime.now())
call2 = Call("577454", "Joe", "225-846-5418", "login", datetime.now())
call3 = Call("456285", "Sue", "855-457-4451", "new", datetime.now())
call4 = Call("564252", "May", "224-564-8852", "login", datetime.now())
call5 = Call("454252", "Kat", "588-454-5574", "help", datetime.now())

call_center = Call_center()
call_center.add(call1).add(call2).add(call3).remove(call1).add(call4).add(call5).remove(call2).info()

#call = call1.display()
#call = call2.display()
#call = call3.display()
#call = call4.display()
#call = call5.display()

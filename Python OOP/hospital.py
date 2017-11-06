class Patient(object):
    def __init__(self, id_num, name, allergies, bed_num):
        self.name = name
        self.allergies = allergies
        self.id_num = id_num
        self.bed_num = "none"

class Hospital(object):
    def __init__ (self, hosp_name, capacity, current):
        self.patients = []
        self.hosp_name = hosp_name
        self.capacity = capacity
        self.current = current

    def admit(self, patient):
        if self.current < self.capacity:
            self.current = self.current + 1
            self.patients.append(patient)
            for patient in self.patients:
                patient.bed_num = self.current
                print "Patient admitted"
                print "Bed: " + str(patient.bed_num)
                return self
        else:
            print "Reached capacity"
            return self
    def discharge(self, patient):
        self.current = self.current - 1
        self.patients.pop(0)
        self.bed_num = "none"
        print "Discharged patient"
        print "Bed: none"
        print "Current beds full: " + str(self.current)
        return self
    #def display(self):
        #print "Hospital: " + self.hosp_name
        #print "Current Patients: " + str(self.current)
        #print "Capacity: " + str(self.capacity)
        #for patient in self.patients:
            #print "Patient Name: " + patient.name
            #print "Patient ID: " + patient.id_num
            #print "Patient Bed Number: " + str(patient.bed_num)
            #print "Patient Allergies: " + patient.allergies

p1 = Patient("251", "Sarah", "a, b", 0)
p2 = Patient("467", "Bonnie", "a, c", 0)
p3 = Patient("628", "Andrew", "b", 0)

Hospital = Hospital("Regional", 100, 98)
#Hospital.display()
Hospital.admit(p1).admit(p2).admit(p3).discharge(p1).admit(p1)

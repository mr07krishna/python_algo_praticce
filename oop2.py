class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    @staticmethod
    def hello(  ):
        print("hello")

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val

        print("Hii",self.name,"your avg score is :" , sum/3)


s1 = student("harii",[20,30,100])
s1.get_avg()
s1.hello()

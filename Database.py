import os


class Accounts:
    def __init__(self, firstname, lastname, contact, email, question, answer, password):
        self.path = '/Users/tim/PycharmProjects/MVCBANKINGAPP/Accounts'
        self.filename = firstname + '.txt'
        self.complete_name = os.path.join(self.path, self.filename)
        with open(self.complete_name, 'w+') as self.f:
            self.f.write(firstname + '\n')
            self.f.write(lastname + '\n')
            self.f.write(contact + '\n')
            self.f.write(email + '\n')
            self.f.write(question + '\n')
            self.f.write(answer + '\n')
            self.f.write(password + '\n')


    @staticmethod
    def file_save(firstname, lastname, contact, email, question, answer, password):
        path = '/Users/tim/PycharmProjects/MVCBANKINGAPP/Accounts'
        file_name = firstname + ".txt"
        complete_name = os.path.join(path, file_name)
        with open(complete_name, 'w+') as f:
            f.write(firstname + '\n')
            f.write(lastname + '\n')
            f.write(contact + '\n')
            f.write(email + '\n')
            f.write(question + '\n')
            f.write(answer + '\n')
            f.write(password)

    @staticmethod
    def login_check(email, password):
        path = '/Users/tim/PycharmProjects/MVCBANKINGAPP/Accounts/'
        file_list = os.listdir(path)
        for i in file_list:
            if i.endswith(".txt"):
                try:
                    with open(path + i, 'r', encoding='ascii') as f:
                        for line in f:
                            if email and password in line:
                                return email and password

                except Exception as es:
                    print("Error", f'Error due to: str({es})')

    @staticmethod
    def file_session(email, password):
        path = '/Users/tim/PycharmProjects/MVCBANKINGAPP/Accounts/'
        file_list = os.listdir(path)
        for i in file_list:
            if i.endswith(".txt"):
                try:
                    with open(path + i, 'r+', encoding='ascii') as f:
                        for lines in f:
                            if email and password in lines:
                                print("Found in %s !" % i)
                                with open(path + i, 'r') as nf:
                                    line = nf.readlines()[:4]
                                    split = line[0].strip().split(' ')
                                    split1 = line[1].strip().split(' ')
                                    split2 = line[2].strip().split(' ')
                                    split3 = line[3].strip().split(' ')
                                    firstname = [str(x) for x in split]
                                    lastname = [str(x) for x in split1]
                                    contact = [str(x) for x in split2]
                                    email = [str(x) for x in split3]
                                    print(firstname)
                                    print(lastname)
                                    print(contact)
                                    print(email)

                except Exception as es:
                    print("Error", f'Error due to: str({es}')

import os


class Accounts:
    def __init__(self):
        self.path = '/Users/tim/PycharmProjects/MVCBANKINGAPP'
        self.accounts = os.listdir(self.path)

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
    def file_read(email, password):
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

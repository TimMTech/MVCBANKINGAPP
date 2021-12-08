import os


class Accounts:
    def __init__(self):
        self.path = '/Users/tim/PycharmProjects/MVCBANKINGAPP/Accounts'
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
                                    details = nf.read()
                                    account_details = details.split()
                                    firstname = account_details[0]
                                    lastname = account_details[1]
                                    contact = account_details[2]
                                    email = account_details[3]
                                    return firstname, lastname, contact, email
                except Exception as es:
                    print("Error", f'Error due to: str({es}')

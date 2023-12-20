from tabulate import tabulate

data = {"Shandy": ["Basic Plan", 12, "shandy-2134"],
        "Cahya": ["Standard Plan", 24, "cahya-abcd"],
        "Ana": ["Premium Plan", 5, "ana-2f9g"],
        "Bagus": ["Basic Plan", 11, "bagus-9f92"]}

class User:
    def __init__(self, username, duration_plan, current_plan):
        self.username = username
        self.current_plan = current_plan
        self.duration_plan = duration_plan

    def check_benefit(self):
        table = [['Bisa Stream', True, True, True],
                 ['Bisa Download', True, True, True],
                 ['Kualitas SD', True, True, True],
                 ['Kualitas HD', False, True, True],
                 ['Kualitas UHD', False, False, True],
                 ['Jumlah Perangkat', 1, 2, 4],
                 ['Konten', '3rd Party Movie', 'Basic Plan + Sport', 'Basic + Standard Plan + Original PacFlix']]
        header = ['Services', 'Basic Plan', 'Standard Plan', 'Premium Plan']
        
        print('PacFlix Plan List\n')
        print(tabulate(table, header))

    def check_plan(self, username):
        for key, value in data.items():
            if key == self.username:
                print(f'Halo {key}!')
                print(f'Anda sedang menggunakan {value[0]}')
                print(f'Total durasi yang tersisa selama {value[1]} Bulan')
            
                try:
                    if value[0] == 'Basic Plan':
                        table = [['Bisa Stream', True],
                                 ['Bisa Download', True],
                                 ['Kualitas SD', True],
                                 ['Kualitas HD', False],
                                 ['Kualitas UHD', False],
                                 ['Jumlah Perangkat', 1],
                                 ['Konten', '3rd Party Movie'],
                                 ['Harga', 120_000]]
                        header = ['Services', 'Basic Plan']

                        print(f'{value[0]} PacFlix Benefit List\n')
                        print(tabulate(table, header))

                    elif value[0] == 'Standard Plan':
                        table = [['Bisa Stream', True],
                                 ['Bisa Download', True],
                                 ['Kualitas SD', True],
                                 ['Kualitas HD', True],
                                 ['Kualitas UHD', False],
                                 ['Jumlah Perangkat', 2],
                                 ['Konten', 'Basic Plan + Sport'],
                                 ['Harga', 160_000]]
                        header = ['Services', 'Standard Plan']

                        print(f'{value[0]} PacFlix Benefit List\n')
                        print(tabulate(table, header))

                    elif value[0] == 'Premium Plan':
                        table = [['Bisa Stream', True],
                                 ['Bisa Download', True],
                                 ['Kualitas SD', True],
                                 ['Kualitas HD', True],
                                 ['Kualitas UHD', True],
                                 ['Jumlah Perangkat', 4],
                                 ['Konten', 'Basic + Standard Plan + Original PacFlix'],
                                 ['Harga', 200_000]]
                        header = ['Services', 'Premium Plan']

                        print(f'{value[0]} PacFlix Benefit List\n')
                        print(tabulate(table, header))

                    else:
                        raise Exception('Plan tidak tersedia')

                except:
                    print('Terjadi error')

    def upgrade_plan(self, current_plan, new_plan):
        valid_plan = ['Basic Plan', 'Standard Plan', 'Premium Plan']
        index_current_plan = valid_plan.index(self.current_plan)
        index_new_plan = valid_plan.index(new_plan)

        if index_current_plan < index_new_plan:
            if self.duration_plan > 12:
                if new_plan == 'Basic Plan':
                    total_price = 120_000 - (120_000 * (5/100))
                    return total_price
                elif new_plan == 'Standard Plan':
                    total_price = 160_000 - (160_000 * (5/100))
                    return total_price
                elif new_plan == 'Premium Plan':
                    total_price = 200_000 - (200_000 * (5/100))
                    return total_price
                else:
                    raise Exception('Plan tidak tersedia')
            
            else:
                if new_plan == "Basic Plan":
                    total_price = 120_000
                    return total_price
                elif new_plan == "Standard Plan":
                    total_price = 160_000
                    return total_price
                elif new_plan == "Premium Plan":
                    total_price = 200_000
                    return total_price
                else:
                    raise Exception('Plan tidak tersedia')
            
        else:
            raise Exception('User hanya boleh untuk upgrade plan')
        
class New_User:
    def __init__(self, username):
        self.username = username

    def check_benefit(self):
        table = [['Bisa Stream', True, True, True],
                 ['Bisa Download', True, True, True],
                 ['Kualitas SD', True, True, True],
                 ['Kualitas HD', False, True, True],
                 ['Kualitas UHD', False, False, True],
                 ['Jumlah Perangkat', 1, 2, 4],
                 ['Konten', '3rd Party Movie', 'Basic Plan + Sport', 'Basic + Standard Plan + Original PacFlix']]
        header = ['Services', 'Basic Plan', 'Standard Plan', 'Premium Plan']
        
        print('PacFlix Plan List\n')
        print(tabulate(table, header))

    def pick_plan(self, new_plan, code_referral):
        list_referral = []

        for key, value in data.items():
            list_referral.append(value[2])
        
        if code_referral in list_referral:
            if new_plan == 'Basic Plan':
                total_price = 120_000 - (120_000 * (4/100))
                return total_price
            elif new_plan == 'Standard Plan':
                total_price = 160_000 - (160_000 * (4/100))
                return total_price
            elif new_plan == 'Premium Plan':
                total_price = 200_000 - (200_000 * (4/100))
                return total_price
            else:
                raise Exception('Plan tidak tersedia')
            
        else:
            raise Exception('Referral code tidak tersedia')
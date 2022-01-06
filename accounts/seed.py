from . import models
from faker import Faker

def generate_random_data(nums = 30):
    pass
    f = Faker()
    model_list = [models.ReferalSource, models.SchoolClass, models.Parent, models.Student, models.Teacher]

    for model in model_list:
        for n in range(nums):
            m = model()
            m.seed_func(f)
            m.save()

if __name__ == '__main__':
    generate_random_data()
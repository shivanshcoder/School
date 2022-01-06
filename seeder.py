from django_seed import Seed

seeder = Seed.seeder()

from accounts import Parent,Teacher, Student
seeder.add_entity(Student, 5)
# seeder.add_entity(Player, 10)

inserted_pks = seeder.execute()
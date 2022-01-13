from constants import PupilEnum
from models import Employee, Pupil, Person


def run():
    worker_1 = Employee(first_name='Gerald', last_name='fromRivia', sex='male', grade_class=11, specialization='Witcher',
                        position='Hunter')
    worker_2 = Employee(first_name='Alexandra', last_name='Cherba', sex='female', grade_class=10, specialization='SmartOne',
                        position='Librarian')
    worker_3 = Employee(first_name='Roman', last_name='Barkov', sex='male', grade_class=6, specialization='IT',
                        position='Clown')
    worker_1.append(worker_2)
    worker_1.append(worker_3)
    worker_1.show_colleagues()

    employee = Employee(first_name='Roman', last_name='Barkov', sex='male', grade_class=6, specialization='IT',
                        position='Clovn')
    pupil = Pupil(first_name='Valentina', last_name='Novoseltseva', sex='female', grade_class=8, specialization='Person')
    person = Person(first_name='Vova', last_name='Vist', sex='Male')

    print('*' * 8)

    worker_1.sort(PupilEnum.GRADE_CLASS.value)
    worker_1.show_colleagues()

    print('*' * 8)

    worker_1.pop()
    worker_1.show_colleagues()

    print('*' * 8)
    print(f'Size of: worker_1 is: {employee.__sizeof__()}')
    print(f'Size of: worker_2 is: {pupil.__sizeof__()}')
    print(f'Size of: worker_3 is: {person.__sizeof__()}')


if __name__ == '__main__':
    run()

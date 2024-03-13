
# def what's_kwargs(**kwargs):
#     print(kwargs, type(kwargs))
    
# que_es_kwargs(name='Juanfra', age=36, score=18.5)


# def calculate_final_score(**kwargs):
#     final_score = kwargs['score'] * 0.3 + kwargs['test_score'] * 0.7
#     print('Su nota es: {}'.format(final_score))
    
# calculate_final_score(score=18, test_score=14)
# calculate_final_score(score=20, test_score=11)


def person_description(**characteristics ):
    print('Person characteristics: ')
    for key,value in characteristics.items():
        print(' -{a}: {b}'.format(a=key,b=value))
        
person_description(
    name = 'Sebas',
    surname = 'Silva',
    age = 36,
    profession = 'Ing. Software',
    country = 'German'
)
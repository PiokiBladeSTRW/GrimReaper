

def NameGenerator():
    import random
    import os
    
    fn_path = os.path.join (os.path.dirname(os.path.abspath(__file__)) , 'first_names.txt')
    ln_path = os.path.join (os.path.dirname(os.path.abspath(__file__)) , 'last_names.txt')

    with open(fn_path, 'r') as first_nf, open(ln_path, 'r') as last_nf:
        first_names = first_nf.read().split('\n')
        last_names = last_nf.read().split('\n')
        
    first_n = random.randint(0, len(first_names) - 1)
    last_n = random.randint(0, len(last_names) - 1)

    name = first_names[first_n]+' '+last_names[last_n]

    return name


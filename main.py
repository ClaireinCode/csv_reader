import csv
search_animal = input('Please enter the type of animal you are looking for: ')
search_animal = search_animal.lower()
try:
    if search_animal == 'cat' or search_animal == 'cats':
        csv_file = 'cats'
    elif search_animal == 'dog' or search_animal == 'dogs':
        csv_file = 'dogs'
        

    with open(f"data/{csv_file}.csv",'r') as file:
        reader = csv.DictReader(file, skipinitialspace=True)
        for row in reader:
            print(f"{row['name'].title()} is {row['age']} years old and is a {row['breed']}.")

except:
    print(f'{search_animal.title()} does not exist.')
        
        

    ##check valid input either cat or dog
    ##if its cat -> read from cat file
    ##if its dog -> read from dog file
    ##Except - Print 'This animal doesn't exist'
##function to open up fil


#with open('cats.csv', 'r',) as file:
#    reader = csv.reader
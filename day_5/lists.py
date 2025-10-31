#syntax
empty_space = " "
empty_list = list()
print(empty_list)

proper_list = ["apples", "oranges", "grapes", "mango", "durian", "kiwi"]
print(proper_list)
print(len(proper_list))

fruit_first = proper_list[0]
fruit_middle = proper_list[2]
fruit_last = proper_list[5]
print(fruit_first+ empty_space + fruit_middle+ empty_space + fruit_last)

mixed_data_types =["John", "18", "1.83", "Single", "123 Charlie Road"]
print(mixed_data_types)

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)
it_companies_first = it_companies[0]
it_companies_middle = it_companies[3]
it_companies_last = it_companies[6]

print(it_companies_first + empty_space + it_companies_middle + empty_space + it_companies_last)

it_companies[0] = "Tesla"
print(it_companies)

it_companies.append("IT_COMPANY")
print(it_companies)

it_companies.insert(3,"IT_COMPANY1")
print(it_companies)

it_companies(str.upper(it_companies_first))
print(it_companies)

print("#; ".join(it_companies))

if "Facebook" in it_companies:
    print("Facebook is present")
else:
    print("Facebook is not present")

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

print(it_companies[:3])

print(it_companies[-3:])

print(it_companies[(len(it_companies)//2)+1])

it_companies.remove(it_companies[-1])
print(it_companies)

it_companies.clear()
print(it_companies)

del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
web_technologies = front_end + back_end
print(web_technologies)

full_stack = web_technologies.copy()
full_stack.extend(["Python", "SQL", "Redux"])
print(full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(f"Min is {ages[0]} and Max is {ages[-1]}")

ages.extend([ages[0], ages[-1]])
print(ages)

if len(ages) % 2 == 0:
    item1 = ages[len(ages)//2]
    item2 = ages[(len(ages)//2)-1]
    median = (item1+item2) / 2
else:
    median = ages[(len(ages)//2)+1]
print(median)

result = sum(ages)
average = result/len(ages)
print(average)

minn = ages[0]
maxx = ages[-1]
print(maxx - minn)

if abs(minn-average) > abs(maxx-average):
    print("1")
else:
    print("2")

countries = [
    'Afghanistan',
    'Albania',
    'Algeria',
    'Andorra',
    'Angola',
    'Antigua and Barbuda',
    'Argentina',
    'Armenia',
    'Australia',
    'Austria',
    'Azerbaijan',
    'Bahamas',
    'Bahrain',
    'Bangladesh',
    'Barbados',
    'Belarus',
    'Belgium',
    'Belize',
    'Benin',
    'Bhutan',
    'Bolivia',
    'Bosnia and Herzegovina',
    'Botswana',
    'Brazil',
    'Brunei',
    'Bulgaria',
    'Burkina Faso',
    'Burundi',
    'Cambodia',
    'Cameroon',
    'Canada',
    'Cape Verde',
    'Central African Republic',
    'Chad',
    'Chile',
    'China',
    'Colombi',
    'Comoros',
    'Congo (Brazzaville)',
    'Congo',
    'Costa Rica',
    "Cote d'Ivoire",
    'Croatia',
    'Cuba',
    'Cyprus',
    'Czech Republic',
    'Denmark',
    'Djibouti',
    'Dominica',
    'Dominican Republic',
    'East Timor (Timor Timur)',
    'Ecuador',
    'Egypt',
    'El Salvador',
    'Equatorial Guinea',
    'Eritrea',
    'Estonia',
    'Ethiopia',
    'Fiji',
    'Finland',
    'France',
    'Gabon',
    'Gambia, The',
    'Georgia',
    'Germany',
    'Ghana',
    'Greece',
    'Grenada',
    'Guatemala',
    'Guinea',
    'Guinea-Bissau',
    'Guyana',
    'Haiti',
    'Honduras',
    'Hungary',
    'Iceland',
    'India',
    'Indonesia',
    'Iran',
    'Iraq',
    'Ireland',
    'Israel',
    'Italy',
    'Jamaica',
    'Japan',
    'Jordan',
    'Kazakhstan',
    'Kenya',
    'Kiribati',
    'Korea, North',
    'Korea, South',
    'Kuwait',
    'Kyrgyzstan',
    'Laos',
    'Latvia',
    'Lebanon',
    'Lesotho',
    'Liberia',
    'Libya',
    'Liechtenstein',
    'Lithuania',
    'Luxembourg',
    'Macedonia',
    'Madagascar',
    'Malawi',
    'Malaysia',
    'Maldives',
    'Mali',
    'Malta',
    'Marshall Islands',
    'Mauritania',
    'Mauritius',
    'Mexico',
    'Micronesia',
    'Moldova',
    'Monaco',
    'Mongolia',
    'Morocco',
    'Mozambique',
    'Myanmar',
    'Namibia',
    'Nauru',
    'Nepal',
    'Netherlands',
    'New Zealand',
    'Nicaragua',
    'Niger',
    'Nigeria',
    'Norway',
    'Oman',
    'Pakistan',
    'Palau',
    'Panama',
    'Papua New Guinea',
    'Paraguay',
    'Peru',
    'Philippines',
    'Poland',
    'Portugal',
    'Qatar',
    'Romania',
    'Russia',
    'Rwanda',
    'Saint Kitts and Nevis',
    'Saint Lucia',
    'Saint Vincent',
    'Samoa',
    'San Marino',
    'Sao Tome and Principe',
    'Saudi Arabia',
    'Senegal',
    'Serbia and Montenegro',
    'Seychelles',
    'Sierra Leone',
    'Singapore',
    'Slovakia',
    'Slovenia',
    'Solomon Islands',
    'Somalia',
    'South Africa',
    'Spain',
    'Sri Lanka',
    'Sudan',
    'Suriname',
    'Swaziland',
    'Sweden',
    'Switzerland',
    'Syria',
    'Taiwan',
    'Tajikistan',
    'Tanzania',
    'Thailand',
    'Togo',
    'Tonga',
    'Trinidad and Tobago',
    'Tunisia',
    'Turkey',
    'Turkmenistan',
    'Tuvalu',
    'Uganda',
    'Ukraine',
    'United Arab Emirates',
    'United Kingdom',
    'United States',
    'Uruguay',
    'Uzbekistan',
    'Vanuatu',
    'Vatican City',
    'Venezuela',
    'Vietnam',
    'Yemen',
    'Zambia',
    'Zimbabwe',
]
print(f"middle element of countries is {countries[(len(countries)//2)+1]}")

if len(countries) % 2 == 0:
    countries1 = countries[0:len(countries)/2]
    countries2 = countries[len(countries)/2:]
else:
    countries1 = countries[0:(len(countries)//2)+1]
    countries2 = countries[(len(countries)//2)+1:]
print(countries1)
print(countries2)

first, second, third, *scandic = ['China', 'Russia',
                                  'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(first, second, third)
print(scandic)
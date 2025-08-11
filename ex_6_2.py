deaths = {"Venezuela" : 1830,
          "El Salvador": 1704,
          "Syria": 819,
          "Philippines": 557,
          "Nicaragua": 523}

for key, value in deaths.items():
  print(f"The rate of killings by law enforcement officers in {key} is {value}")

  


incarceration_rates = {"Venezuela": 199,
                       "El Salvador": 1659,
                       "Syria": 60,
                       "Phillipines": 162,
                       "Nicaragua": 332}

for key, value in incarceration_rates.items():
  print(f"{key} has an incarceration rate of {value}.")
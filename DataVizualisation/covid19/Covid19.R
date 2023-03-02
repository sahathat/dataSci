library(DescTools)
library(readr)
library(dplyr)
library(ggplot2)
confirmed <- read_csv("time_series_covid_19_confirmed.csv")
death <- read_csv("time_series_covid_19_deaths.csv")
View(confirmed)
View(death)

# Replace state missing value with "None"
confirmed$State <- replace(confirmed$State, is.na(confirmed$State),"None")

is.na(head(confirmed$State))

# Add death column in confirmed
confirmed <- confirmed %>% mutate(death_4_2020=death$'4_1_2020',death_12_2020 = death$'12_1_2020',death_4_2021 = death$'4_1_2021')

View(confirmed)

# select sd
confirmed %>% summarise(sd_4_2020 = sd(confirmed$'4_1_2020'),var_4_2020 = var(confirmed$'4_1_2020'),
                        sd_12_2020 = sd(confirmed$'12_1_2020'),var_12_2020 = var(confirmed$'12_1_2020'),
                        sd_4_2021 = sd(confirmed$'4_1_2021'),var_4_2021 = var(confirmed$'4_1_2021'))

# filter data and show count
confirmed %>% group_by(Country) %>% 
  select(april = '12_1_2020') %>%
  summarise(infected = sum(april)) %>% 
  filter(infected == 0) %>% count()

# show top 10
confirmed %>% select(State,Country,death = 'death_4_2021') %>% arrange(desc(death)) %>% head(10)

# show top 10
confirmed %>% select(State,Country,infected = '4_1_2021') %>% arrange(desc(infected)) %>% head(10)

# plot histogram
hist(confirmed$'4_1_2021', binwidth = 10)

# Basic histogram
comfirmed %>% select('4_1_2021') %>% filter('4_1_2021' < 10000000) %>% ggplot(confirmed, aes(x=)) + geom_histogram(binwidth = 100000)

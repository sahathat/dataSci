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
  select(december = '12_1_2020') %>%
  summarise(infected = sum(december)) %>% 
  filter(infected == 0) %>% count()

# show top 10
confirmed %>% select(State,Country,death = 'death_4_2021') %>% arrange(desc(death)) %>% head(10)

# show top 10
confirmed %>% select(State,Country,infected = '4_1_2021') %>% arrange(desc(infected)) %>% head(10)

# plot histogram
hist(confirmed$'4_1_2021', binwidth = 10)

# Basic histogram
ggplot(confirmed, aes(x=confirmed$'4_1_2021')) + geom_histogram(binwidth = 1000) + 
xlim(c(0, 100000))

# Linear regression

chinaConfirmed <- confirmed %>% group_by(Country) %>% 
  select(april2020 = '4_1_2020', dec2020 = '12_1_2020', april2021 = '4_1_2021') %>%
  summarise(april2020 = sum(april2020),dec2020 = sum(dec2020),april2021 = sum(april2021)) %>% 
  filter(Country == "China")
chinaConfirmed

df <- list(date = c(4,12,16), infected  = c(82361,92993,101754))

lmInfect = lm(infected~date, data = df) # Create the linear regression
summary(lmInfect) # Review the results
pred <- 75568.6 + 1575.1*24
pred
